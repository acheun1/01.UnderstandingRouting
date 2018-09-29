#Understanding Routing
#2018 09 20
#Cheung Anthony

# Create a server file that generates 5 different http responses for the following 5 url requests:

# localhost:5000 - have it say "Hello World!" - Hint: If you have only one route that your server is listening for, it must be your root route ("/")

# localhost:5000/dojo - have it say "Dojo!"

# localhost:5000/say/flask - have it say "Hi Flask".  Have function say() handle this routing request.

# localhost:5000/say/michael - have it say "Hi Michael" (have the same function say() handle this routing request)

# localhost:5000/say/john - have it say "Hi John!" (have the same function say() handle this routing request)

# localhost:5000/repeat/35/hello - have it say "hello" 35 times! - You will need to convert a string "35" to an integer 
# 35.  To do this use int().  For example int("35") returns 35.  If the user request localhost:5000/repeat/80/hello, it should say "hello" 80 times.

# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times! (have this be handled by the same route function as #6)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return("hello world")

@app.route('/coding')
def dojo():
    return("<h1>Coding Dojo<h1>")

@app.route('/say/<name>')
def say(name):
    print(name)
    return("Hi" + name +" !")

@app.route('/repeat/<cnt>/hello')
def repeat(cnt):
    cnt_int=int(cnt)
    return("hello"*cnt_int)

@app.route('/repeat/<cnt>/<word>')
def repeatany(cnt,word):
    cnt_int=int(cnt)
    return(word*cnt_int)

app.run(debug=True)


