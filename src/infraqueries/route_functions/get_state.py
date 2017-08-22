import json

def get_state(access,secret):
    if access == "0000" and secret == "0000":
        payload = [
                  {"name":"vm1","az":"us-west-2"},
                  {"name":"vm2","az":"us-west-1"},
                  {"name":"vm3","az":"us-west-2"},
                  {"name":"vm4","az":"us-east-2"},
                  {"name":"vm5","az":"us-east-1"},
                  {"name":"vm6","az":"ca-central-1"}
                  ]
        return json.dumps(payload)
    return None

