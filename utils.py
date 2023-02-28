import config
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score,roc_curve
from  sklearn.neighbors import KNeighborsClassifier
import warnings 
warnings.filterwarnings("ignore")
import json
import pickle


class Diabetes():
    def __init__(self, Pregnancies ,  Glucose ,  BloodPressure ,  SkinThickness ,  Insulin ,BMI ,  DiabetesPedigreeFunction ,  Age ):
        self.Pregnancies                =  Pregnancies
        self.Glucose                    =  Glucose
        self.BloodPressure              =  BloodPressure
        self.SkinThickness              =  SkinThickness
        self.Insulin                    =  Insulin
        self.BMI                        =  BMI
        self.DiabetesPedigreeFunction   =  DiabetesPedigreeFunction
        self.Age                        =  Age
            
    def load_model(self):
        with open(config.json_file_path,"rb")as f:
            self.json_file = json.load(f)
        with open(config.knn_model_path,"rb")as f:
            self.model =pickle.load(f)
        with open(config.std_scalar_file_path,"rb")as f:
            self.std_scalar =pickle.load(f)

    def get_prediction(self):
        self.load_model()
        array = np.zeros(len(self.json_file["columns"]))
        array[0] = self.Pregnancies
        array[1] = self.Glucose 
        array[2] = self.BloodPressure         
        array[3] = self.SkinThickness        
        array[4] = self.Insulin     
        array[5] = self.BMI                      
        array[6] = self.DiabetesPedigreeFunction 
        array[7] = self.Age
        array[3]   =self.json_data["aspiration_values"][self.aspiration] 
        std_array = self.std_scalar.transform([array])
        prediction = self.model.predict(std_array)
        # print("Predict accuracy of Diabetes >>>>> ",prediction)
        return prediction

if __name__ == "__main__":
    Pregnancies               =  1.000
    Glucose                   =  89.000
    BloodPressure             =  66.000
    SkinThickness             =  23.000
    Insulin                   =  94.000
    BMI                       =  28.100
    DiabetesPedigreeFunction  =  0.167
    Age                       =  21.000
                
#creating object of class
    diabetes_pred = Diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age)
    result= diabetes_pred.get_prediction()
    print("predicted class for dibetes >>>",result)
       


