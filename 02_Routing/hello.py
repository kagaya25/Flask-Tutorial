from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
   return 'Hello World'
@app.route('/login')
def login():
   return 'login page'
@app.route('/about')
def about():
   return 'about page'

if __name__ == '__main__':
   app.debug = True
   app.run(port=4000)
   
   
   