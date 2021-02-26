""" really terrible splunk event pusher """

from json import dumps as json_dumps
import requests
import os
from datetime import datetime

def send_single_event(token,endpoint,starttime,**kwargs, ):
    """ pass it the endpoint, token and a string, and it'll submit the event """
    if 'event' not in kwargs:
        raise ValueError("need to have at least an event value")
    headers = {
        'Authorization' : 'Splunk {}'.format(token)
    }
    payload = kwargs
    payload['index'] = os.environ['SPLUNK_INDEX']
    payload['sourcetype'] = os.environ['SPLUNK_SOURCETYPE']
    payload['host'] = os.environ['SPLUNK_HOST']
    payload['time'] = starttime.timestamp()

    try:
        req = requests.post(url=endpoint, json=payload, headers=headers)
        req.raise_for_status()
    except requests.exceptions.HTTPError as error_message:
        print("HTTPError: {error_message}")
        print(req.text)