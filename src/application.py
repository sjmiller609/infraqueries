from flask import Flask, request, abort
import json
from flask_cors import CORS, cross_origin

def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
CORS(application)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

def get_state(access,secret):
    if access == "0000" and secret == "0000":
        payload = {
                  "vm1":{"az":"us-west-2"},
                  "vm2":{"az":"us-west-1"},
                  "vm3":{"az":"us-west-2"},
                  "vm4":{"az":"us-east-2"},
                  "vm5":{"az":"us-east-1"},
                  "vm6":{"az":"ca-central-1"}
                  }
        return json.dumps(payload)
    return None

@application.route('/state',methods=["GET"])
def givestate():
    access = request.args.get('access_key',None,type=str)
    secret = request.args.get('secret_key',None,type=str)
    payload = get_state(access,secret)
    if not payload:
        abort(403)
    return payload
   

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = False
    application.run(host="0.0.0.0")
