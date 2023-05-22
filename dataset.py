import pandas as pd
import joblib

# Load data using openpyxl engine
df = pd.read_excel('nba_data.xlsx', engine='openpyxl')

# Check if the required columns are in the DataFrame
required_columns = ['Pos', 'Tm', 'Age', 'G', 'GS', '3P']
print("Required columns:", required_columns)
print("Columns in DataFrame:", df.columns)

missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print("Missing columns:", missing_columns)
else:
    print("All required columns are present.")

# Define target variable
target = 'PTS'

# Define feature columns
feature_cols = ['GP', 'MIN', 'FGM']

# Split data into X and y
X = df[feature_cols]
y = df[target]

# Create and train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Evaluate the model's performance using R-squared
r_squared = model.score(X, y)
print('R-squared:', r_squared)

# Save the model to a file
joblib.dump(model, 'linear_regression_model.joblib')
print("Model saved as linear_regression_model.joblib")
