import werkzeug
import pandas as pd
from joblib import load
from flask import Flask, request, render_template

# Creating app object

app = Flask(__name__)

# Predicting Test data
# Checking the model with single data point from test dataset
# Loading required models

# Loading the saved model
full_model_pipeline = load('udf_full_pipeline')

# Using the html template
@app.route('/')
def home():
    return render_template('index.html')

# Exposing the below code to localhost:5000
@app.route('/api', methods=['POST'])
def pred_testquery():

    # content = request.json
    Sales_Velocity = float(request.form['Sales Velocity'])
    Sales_Stage_Iterations = float(request.form['Sales Stage Iterations'])
    Opportunity_Size = float(request.form['Opportunity Size (USD)'])
    Business_from_Client_Last_Year = float(request.form['Business from Client Last Year'])
    Opportunity_Sizing = float(request.form['Opportunity Sizing'])

    datapoint = [Sales_Velocity, Sales_Stage_Iterations, Opportunity_Size,
                 Business_from_Client_Last_Year, Opportunity_Sizing]

    def y_pred(X_data=datapoint, model=full_model_pipeline):

        # Creating a dataframe out of input
        df = pd.DataFrame(index=[0])
        df['Sales Velocity'] = X_data[0]
        df['Sales Stage Iterations'] = X_data[1]
        df['Opportunity Size (USD)'] = X_data[2]
        df['Business from Client Last Year'] = X_data[3]
        df['Opportunity Sizing'] = X_data[4]

        # Fitting classifier model
        pred = model.named_steps.model_fitting.predict(df)

        return pred

    prediction = y_pred()
    if prediction == 1:
        opportunity = "Yes"
    else:
        opportunity = "No"
    response = {'This client will provide opportunity?': opportunity}

    return str(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, use_reloader=False)