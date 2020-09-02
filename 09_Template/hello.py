from flask import Flask ,redirect, url_for, request,render_template
from markupsafe import escape
app = Flask(__name__)
@app.route('/')
def hello_world():
   return render_template('login.html')

"""
The jinja2 template engine uses the following delimiters for escaping from HTML.

{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements

"""
@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)
   
if __name__ == '__main__':
   app.run(debug = True,port=4000)
   
   
   