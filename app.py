"""from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return "hello worldd"

@app.route('/head')
def head():
    return "head file"

@app.route('/tail')
def tail():
    return "Tail"

if __name__=='__main__':
    app.run(debug=False)

from flask import Flask
app=Flask(__name__)

@app.route('/')
def first():
    return"a+B"

if __name__=='__main__':
    app.run(debug=False)

from flask import Flask
app=Flask(__name__)
@app.route('/')
def head():
    return "HEAD"

if __name__=='__main__':
    app.run(debug=False)

from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def fun1():
    return render_template("index.html")
@app.route('/name',methods=["POST"])
def name():
    return "Hello Lakshman"

if __name__=='__main__':
    app.run(debug=True)

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def start():
    return render_template("indexx.html")
@app.route('/next',methods=["POST"])
def next():
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)

from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def first():
    return render_template("indexxx.html")
@app.route('/abc', methods=["POST"])
def rep():
    return "HELLO LAKSHMAN"

@app.route('/user')
def use():
    return "WELCOME USER" 
if __name__=='__main__':
    app.run(debug=True)  """

from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def fun1():
    return render_template("indexxx.html")
@app.route('/acom', methods=["POST"])

def fun2():
    p=request.form["a"]
    #print(p)
    return render_template("indexxx.html",y=p)

if __name__=='__main__':
    app.run(debug=False)
 