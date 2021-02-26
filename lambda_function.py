import boto3, json, os 
from datetime import datetime, timedelta
from instances import *
from metrics import *
from connectqueue import NRGCareQueues
from splunk import send_single_event

def lambda_handler(event, context):
    token = os.environ['SPLUNK_HEC_TOKEN']
    endpoint = os.environ['SPLUNK_HEC_URL']
    endtime = datetime.now().replace(microsecond=0, second=0, minute=0)
    starttime = endtime - timedelta(hours=1)
    payload=  {}
    

    session = boto3.Session()

    for instance in Instances:
        for queue in NRGCareQueues:
            for metric in HistoricalMetrics:
                connect = session.client('connect',region_name='ap-southeast-2')
                response = connect.get_metric_data(
                    InstanceId=instance["InstanceId"],
                    StartTime=starttime,
                    EndTime=endtime,
                    Filters={
                        'Queues': [
                            queue["QueueId"]
                        ],
                        'Channels': [
                            'VOICE'
                        ]
                    },
                    Groupings=[
                        'QUEUE'
                    ],
                    HistoricalMetrics=[
                    {
                        'Name': metric["MetricName"],
                        'Unit': metric["Unit"],
                        'Statistic' : metric["Statistic"]
                    },
                    ]
                )
                
                if response['MetricResults'] != []:
                #Build event
                    event = {}
                    event["InstanceId"] = instance["InstanceId"]
                    event["QueueId"] =  response['MetricResults'][0]['Dimensions']['Queue']['Id']
                    event["QueueName"] = queue["QueueName"]
                    event["MetricName"] = metric["MetricName"]
                    event["Unit"] = metric["Unit"]
                    event["Statistic"] = metric["Statistic"]
                    event["Value"] = response['MetricResults'][0]['Collections'][0]['Value']
                    event["Period"] = "60m"
                    payload.update(event)
                    print(payload)
                    send_single_event(token,endpoint,starttime,event=payload)
            
            for metric in ServiceLevelMetrics:
                connect = session.client('connect',region_name='ap-southeast-2')
                response = connect.get_metric_data(
                    InstanceId=instance["InstanceId"],
                    StartTime=starttime,
                    EndTime=endtime,
                    Filters={
                        'Queues': [
                            queue["QueueId"]
                        ],
                        'Channels': [
                            'VOICE'
                        ]
                    },
                    Groupings=[
                        'QUEUE'
                    ],
                    HistoricalMetrics=[
                    {
                        'Name': metric["MetricName"],
                        'Unit': metric["Unit"],
                        'Threshold': {
                            'Comparison': 'LT',
                            'ThresholdValue': metric["Threshold"]["ThresholdValue"]
                        },
                        'Statistic' : metric["Statistic"]
                    },
                    ]
                )
                print(response)
                if response['MetricResults'] != []:
                #Build event
                    event = {}
                    event["InstanceId"] = instance["InstanceId"]
                    event["QueueId"] =  response['MetricResults'][0]['Dimensions']['Queue']['Id']
                    event["QueueName"] = queue["QueueName"]
                    event["MetricName"] = metric["MetricName"]+"_"+str(metric["Threshold"]["ThresholdValue"])
                    event["Unit"] = metric["Unit"]
                    event["Statistic"] = metric["Statistic"]
                    event["Value"] = response['MetricResults'][0]['Collections'][0]['Value']
                    event["Period"] = "60m"
                    payload.update(event)
                    print(payload)
                    send_single_event(token,endpoint,starttime,event=payload)
