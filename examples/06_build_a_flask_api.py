# Usage:
# First we imported the Flask class.
from flask import Flask, escape, url_for, render_template, jsonify, request
import os

# Next we create an instance of this class. The first argument is the name of the application’s module or package.
# If you are using a single module (as in this example), you should use __name__ because depending on if it’s started
# as application or imported as module the name will be different ('__main__' versus the actual import name).
# This is needed so that Flask knows where to look for templates, static files, and so on.
# For more information have a look at the Flask documentation.
app = Flask(__name__)


# We then use the route() decorator to tell Flask what URL should trigger our function.
# The function is given a name which is also used to generate URLs for that particular function,
# and returns the message we want to display in the user’s browser.
# Navigate to http://127.0.0.1:8081/
@app.route('/')
def index():
    return 'Index Page'


# VARIABLES

# Navigate to http://127.0.0.1:8081/hello
@app.route('/hello')
def hello():
    return 'Hello, World'


# Navigate to http://127.0.0.1:8081/parameter
@app.route('/route_with_parameter/<parameter>')
def route_with_parameter(parameter):
    return 'We got a parameter: %s' % escape(parameter)


# Navigate to http://127.0.0.1:8081/user/123456
# Try to navigate to http://127.0.0.1:8081/user/stringID
@app.route('/user/<int:user_id>')
def show_user(user_id):
    # Assignment: create a dict and show the user with the given id, the url only resolves if the id is an integer
    user_id_dict = {123456: 'Herman'}
    return f'user {user_id_dict[user_id]}'


# Navigate to http://127.0.0.1:8081/path/subpath/123123/subsubsubpath
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

# TEMPLATES
# http://127.0.0.1:8081/linkit/
@app.route('/linkit/')
@app.route('/linkit/<name>')
def linkit(name=None):
    # Assignment: make this function accept and pass a name variable (see template)
    return render_template('linkit.html', name=name)


# AUTHENTICATION
# curl -i -H 'x-api-key: linkitbootcamp' http://localhost:8000
@app.route('/supersecret')
def supersecret():
    # Assignment: access the supersecret route through Postman and curl
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == 'linkitbootcamp':
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

####
####   ______                               _
####  |  ____|                             (_)
####  | |__    __  __   ___   _ __    ___   _   ___    ___
####  |  __|   \ \/ /  / _ \ | '__|  / __| | | / __|  / _ \
####  | |____   >  <  |  __/ | |    | (__  | | \__ \ |  __/
####  |______| /_/\_\  \___| |_|     \___| |_| |___/  \___|
####
####  Now it's time to do something real!!!
####
#### 1) Go to the Flask documentation
#### 2) Try the existing endpoints, access s
#### 3) Add some endpoints to your app, try out all the basic http methods (POST, PUT, DELETE)


# Set environment variables and run Flask
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8081))
    app.run(host='127.0.0.1', port=port, debug=True)
