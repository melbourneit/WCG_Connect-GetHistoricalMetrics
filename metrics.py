HistoricalMetrics = [
    {
        "MetricName" : "ABANDON_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "AFTER_CONTACT_WORK_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "API_CONTACTS_HANDLED",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CALLBACK_CONTACTS_HANDLED",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_ABANDONED",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_AGENT_HUNG_UP_FIRST",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_CONSULTED",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_HANDLED",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_HANDLED_INCOMING",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_HANDLED_OUTBOUND",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_HOLD_ABANDONS",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_MISSED",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_QUEUED",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_TRANSFERRED_IN",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_TRANSFERRED_IN_FROM_QUEUE",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_TRANSFERRED_OUT",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "CONTACTS_TRANSFERRED_OUT_FROM_QUEUE",
        "Unit" : "COUNT",
        "Statistic" : "SUM"
    },
    {
        "MetricName" : "HANDLE_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "HOLD_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "INTERACTION_AND_HOLD_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "INTERACTION_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "OCCUPANCY",
        "Unit" : "PERCENT",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "QUEUE_ANSWER_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "QUEUED_TIME",
        "Unit" : "SECONDS",
        "Statistic" : "MAX"
    }
]

ServiceLevelMetrics = [
    {
        "MetricName" : "SERVICE_LEVEL",
        "Threshold" : {
                "Comparison": "LT",
                "ThresholdValue": 30
            },
        "Unit" : "PERCENT",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "SERVICE_LEVEL",
        "Threshold" : {
                "Comparison": "LT",
                "ThresholdValue": 60
            },
        "Unit" : "PERCENT",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "SERVICE_LEVEL",
        "Threshold" : {
                "Comparison": "LT",
                "ThresholdValue": 90
            },
        "Unit" : "PERCENT",
        "Statistic" : "AVG"
    },
    {
        "MetricName" : "SERVICE_LEVEL",
        "Threshold" : {
                "Comparison": "LT",
                "ThresholdValue": 300
            },
        "Unit" : "PERCENT",
        "Statistic" : "AVG"
    }
]

ConnectInstanceMetrics = [
    {
        "NameSpace" : "AWS/Connect",
        "MetricName" : "ToInstancePacketLossRate",
        "Unit" : "Percent",
        "Period" : 3600,
        "Dimensions" : [
            {
                "Name" : "Participant",
                "Value" : "Agent"
            },
            {
                "Name" : "Type of Connection",
                "Value" : "WebRTC"
            },
            {
                "Name": "Stream Type",
                "Value": "Voice"
            }
        ]
    },
        {
        "NameSpace" : "AWS/Connect",
        "MetricName" : "ConcurrentCalls",
        "Unit" : "Count",
        "Period" : 300,
        "Dimensions" : [
            {
                "Name" : "MetricGroup",
                "Value" : "VoiceCalls"
            }
        ]
    }
]
