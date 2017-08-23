from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
import json
from random import randint

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

def get_state(request):
    access = request.args.get('access_key',None,type=str)
    secret = request.args.get('secret_key',None,type=str)
    if not (access == "0000" and secret == "0000"): return None
    payload = [
              {"name":"vm1","az":"us-west-2"},
              {"name":"vm2","az":"us-west-1"},
              {"name":"vm3","az":"us-west-2"},
              {"name":"vm4","az":"us-east-2"},
              {"name":"vm5","az":"us-east-1"},
              {"name":"vm6","az":"ca-central-1"}
              ]
    return json.dumps(payload)

def get_vm_status(request):
    access = request.args.get('access_key',None,type=str)
    secret = request.args.get('secret_key',None,type=str)
    vm = request.args.get('vm_name',None,type=str)
    if not (access == "0000" and secret == "0000"): return None
    states = ["rebooting","running","stopping","stopped","terminated","shutting-down","pending"]
    rand = randint(0,10000)
    return states[rand % len(states)]

def main():
    # EB looks for an 'application' callable by default.
    application = Flask(__name__)
    CORS(application)

    @application.route('/state',methods=["GET"])
    def givestate():
        payload = get_state(request)
        if not payload:
            abort(403)
        return payload

    @application.route('/vmstatus',methods=["GET"])
    def givevmstate():
        payload = get_vm_status(request)
        if not payload:
            abort(403)
        return payload


    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run(host="0.0.0.0")  

# run the app.
if __name__ == "__main__":
    main()

