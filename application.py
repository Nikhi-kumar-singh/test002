from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
import  pickle

application=Flask(__name__)
app=application

model1=pickle.load(
    open("models\pipeline_StandardScaler_LinearRegression.pkl","rb")
)

@app.route("/")
def hello_world():
    return render_template("home.html",result=0)

@app.route("/predict_data",methods=["GET","POST"])
def predict_data():
    if request.method=="POST":
        temperature=float(request.form.get("temperature"))
        rh=float(request.form.get("rh"))
        ws=float(request.form.get("ws"))
        rain=float(request.form.get("rain"))
        ffmc=float(request.form.get("ffmc"))
        dmc=float(request.form.get("dmc"))
        dc=float(request.form.get("dc"))
        isi=float(request.form.get("isi"))
        classes=float(request.form.get("classes"))
        region=float(request.form.get("region"))

        x=[[temperature,rh,ws,rain,ffmc,dmc,dc,isi,classes,region]]
        result=model1.predict(x)
        
        return render_template("home.html",result=result[0])

        					
    else :
        return render_template("index.html")



if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)