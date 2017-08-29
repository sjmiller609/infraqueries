# -*- coding: utf-8 -*-
import json


def handler(event, context):
    try:
      access = event["queryStringParameters"]['access_key']
      secret = event["queryStringParameters"]['secret_key']
    except KeyError:
      access = event.get('access_key')
      secret = event.get('secret_key')

    if not (access == "0000" and secret == "0000"):
        payload = json.dumps(event)
        return {"statusCode":403,
               "headers": {"Content-Type": "application/json"},
               "body": payload}

    payload = """\
	[
          {"name":"vm1","az":"us-west-2"},
          {"name":"vm2","az":"us-west-1"},
          {"name":"vm3","az":"us-west-2"},
          {"name":"vm4","az":"us-east-2"},
          {"name":"vm5","az":"us-east-1"},
          {"name":"vm6","az":"ca-central-1"}
        ]"""
    return {"statusCode":200,
            "headers": {"Content-Type": "application/json"},
            "body": payload}
