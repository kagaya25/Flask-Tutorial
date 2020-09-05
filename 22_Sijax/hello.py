import os
from flask import Flask, g,render_template
import flask_sijax 
#pip pip install flask-sijax

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

# Initialization code for Flask and Flask-Sijax
# See above..

# Functions registered with @app.route CANNOT use Sijax
@app.route('/')
def index():
    return 'Index'

# Functions registered with @flask_sijax.route can use Sijax
@flask_sijax.route(app, '/hello')
def hello():
    # Every Sijax handler function (like this one) receives at least
    # one parameter automatically, much like Python passes `self`
    # to object methods.
    # The `obj_response` parameter is the function's way of talking
    # back to the browser
    def say_hi(obj_response):
        obj_response.alert('Hi there!')

    if g.sijax.is_sijax_request:
        # Sijax request detected - let Sijax handle it
        g.sijax.register_callback('say_hi', say_hi)
        return g.sijax.process_request()

    # Regular (non-Sijax request) - render the page template
    return render_template('index.html')
 
if __name__ == '__main__':
   app.run(debug = True)