from flask import Flask, url_for,render_template,redirect,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import requests




app=Flask(__name__)
app.secret_key="aishadarvesh"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///writing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.app_context().push()
db=SQLAlchemy(app)
Bootstrap(app)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prompt')
def prompt_generator():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    return render_template("prompt.html",quote=quote)


@app.route('/typing_speed', methods=['POST','GET'])
def typing_speed():
    if request.method=='POST':
       request.form.get('text')
       return redirect(url_for('typing_speed'))
    return render_template('typing.html')


if __name__=="__main__":
    app.run(debug=True)

