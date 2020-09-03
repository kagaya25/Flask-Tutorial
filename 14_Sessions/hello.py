from flask import Flask ,redirect, url_for, request,render_template,make_response,session
from markupsafe import escape
import secrets
generated_key = secrets.token_urlsafe(25)
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = generated_key

@app.route('/')
def index():
   
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"
@app.route('/login', methods = ['GET', 'POST'])

def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return '''
   <form action = "/login" method = "POST">
      <p>Enter Name:</p>
      <p><input type = "text" name = "username" /></p>
      <p><input type = "submit" value = "submit" /></p>
   </form>
   '''
   
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
if __name__ == '__main__':
   app.run(debug = True,port=4000)
   
   
   