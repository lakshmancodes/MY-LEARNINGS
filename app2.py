from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def first():
    return render_template("indexxx.html")
@app.route('/acom',methods=["POST"])
def rep():
    return render_template("indexxx.html")

@app.route('/user')
def use():
    return "WELCOME USER "

if __name__=='__main__':
    app.run(debug=True)