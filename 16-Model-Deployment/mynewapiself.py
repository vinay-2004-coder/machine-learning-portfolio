from flask import Flask,request,jsonify
import joblib
import pandas as pd

# CREATING FLASK APP

app=Flask(__name__)


# CONNECT POST API CALL ---> predict() function

@app.route('/predict',methods = ['POST'])

def predict():

    # GET JSON REQUEST
    feat_data= request.json
    # CONVERT JSON TO PANDAS DF (COL NAMES)
    
    df=pd.DataFrame(feat_data)
    df=df.reindex(columns=col_names)
    
    # PREDICT
    
    prediction=list(model.predict(df))
    
    return  jsonify({'prediction':str(prediction)})       #PREDICTION


# LOAD MY MODEL and LOAD COLUMN NAMES

if __name__ == '__main__':
    model  = joblib.load('final_model.pkl')
    col_names = joblib.load('column_names.pkl')

    app.run(debug=True)
