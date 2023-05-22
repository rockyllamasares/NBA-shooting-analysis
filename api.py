import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model
loaded_model = joblib.load('nba_linear_regression_model.pkl')

# Define feature columns
cat_cols = ['Pos', 'Tm']
num_cols = ['Age', 'G', 'GS', '3P']

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    input_df = pd.DataFrame(input_data, index=[0])

    # Apply preprocessing steps to input_df
    preprocessor = loaded_model.named_steps['preprocessing']
    cat_preprocessor = preprocessor.named_transformers_['cat']
    num_preprocessor = preprocessor.named_transformers_['num']

    cat_input_df = cat_preprocessor.transform(input_df[cat_cols]).toarray()  # Convert to 2D array
    num_input_df = num_preprocessor.transform(input_df[num_cols])

    input_df_processed = np.hstack([cat_input_df, num_input_df])

    # Make a prediction with the processed input data
    prediction = loaded_model.named_steps['linear_regression'].predict(input_df_processed)

    # Normalize the prediction to get a percentage
    # max_points = 200
    percentage_prediction = prediction

    return jsonify({'prediction': f'{percentage_prediction.tolist()[0]:.2f}%'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
