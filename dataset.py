import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Import the necessary libraries

# Step 2: Load the Excel data into a Pandas DataFrame
data = pd.read_excel('nba_league_leaders.xlsx', engine='openpyxl')

# Step 3: Split the data into input features (X) and the target variable (y)
X = data.drop(['oreb', 'dreb', 'reb'], axis=1)  # Remove the target variables from the features
y = data[['oreb', 'dreb', 'reb']]  # Select the target variables

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create and train a predictive model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model's performance using a suitable metric
mse = mean_squared_error(y_test, y_pred)
