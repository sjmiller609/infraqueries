# -*- coding: utf-8 -*-
import json

def authenticate(event):
    print(event)
    passed = False
    try:
      access = event["queryStringParameters"]['access_key']
      secret = event["queryStringParameters"]['secret_key']
      if access == "0000" and secret == "0000": passed = True
    except:
      if event["access_key"] == "0000" and event["access_key"] == "0000": passed = True
    finally:
      return passed

def handler(event, context):
    if not authenticate(event):
      payload = json.dumps(event)
      return {"statusCode":403,
             "headers": {"Content-Type": "application/text"},
             "body": "wrong keys"}

    # === === === === === === === === === === === === === === ===
    # === === === === === === === === === === === === === === ===

    # to change what the api returns, modify this payload.
    payload = """\
       [
          {"name":"vm1","az":"us-west-2"},
          {"name":"vm2","az":"us-west-1"},
          {"name":"vm3","az":"us-west-2"},
          {"name":"vm4","az":"us-east-2"},
          {"name":"vm5","az":"us-east-1"},
          {"name":"vm6","az":"ca-central-1"}
        ]"""

    # === === === === === === === === === === === === === === ===
    # === === === === === === === === === === === === === === ===


    return {"statusCode":200,
            "headers": {"Content-Type": "application/json"},
            "body": payload}