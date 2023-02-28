from flask import Flask ,jsonify,render_template,request
import config
from utils import Diabetes

app = Flask(__name__)
@app.route("/")
def get_homeapi():
    return "welcome to home api"

@app.route("/D",methods=["POST","GET"])
def  get_prediction():
    if request.method =="POST":
        data=request.form
        Pregnancies                =  eval(data["Pregnancies"])
        Glucose                    =  eval(data["Glucose"])
        BloodPressure              =  eval(data["BloodPressure"])
        SkinThickness              =  eval(data["SkinThickness"])
        Insulin                    =  eval(data["Insulin"])
        BMI                        =  eval(data["BMI"])
        DiabetesPedigreeFunction   =  eval(data["DiabetesPedigreeFunction"])
        Age                        =  eval(data["Age"])
    diabetes_pred =Diabetes( Pregnancies ,  Glucose ,  BloodPressure ,  SkinThickness ,  Insulin ,BMI ,  DiabetesPedigreeFunction ,  Age )
    classification =diabetes_pred.get_prediction()
    return jsonify({"result":f"Class of diabetes {classification}"})

if __name__ =="__main__":
    app.run(host="0.0.0.0")