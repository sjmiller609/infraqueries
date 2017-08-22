from flask import Flask, request, abort
from flask_cors import CORS, cross_origin

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

def main():
	# EB looks for an 'application' callable by default.
	application = Flask(__name__)
	CORS(application)

	from route_functions.get_state import get_state
	@application.route('/state',methods=["GET"])
	def givestate():
	    access = request.args.get('access_key',None,type=str)
	    secret = request.args.get('secret_key',None,type=str)
	    payload = get_state(access,secret)
	    if not payload:
		abort(403)
	    return payload

	from route_functions.get_vm_status import get_vm_status
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

