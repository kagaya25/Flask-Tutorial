from flask import Flask ,redirect, url_for, request,render_template
from markupsafe import escape
app = Flask(__name__)
@app.route('/')
def hello_world():
   return render_template('login.html')


   
if __name__ == '__main__':
   app.debug = True
   app.run(port=4000)
   
   
   