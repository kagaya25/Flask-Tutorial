from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
 
if __name__ == '__main__':
   app.debug = True
   app.run(port=4000)
   
   
   