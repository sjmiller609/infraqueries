# -*- coding: utf-8 -*-


def handler(event, context):
    access = event.get('access_key')
    secret = event.get('secret_key')

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
