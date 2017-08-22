import json
from random import randint

def get_vm_status(request):
    access = request.args.get('access_key',None,type=str)
    secret = request.args.get('secret_key',None,type=str)
    vm = request.args.get('vm_name',None,type=str)
    if not (access == "0000" and secret == "0000"): return None
    states = ["rebooting","running","stopping","stopped","terminated","shutting-down","pending"]
    rand = randint(0,len(states))
    return states[rand]

