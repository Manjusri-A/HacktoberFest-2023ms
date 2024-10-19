import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Fetch the dataset
df = pd.read_csv('FoodTruck.csv')

# Check for necessary columns
if 'city_population' not in df.columns or 'food_truck_profit' not in df.columns:
    raise ValueError("The required columns are not in the dataset.")

# Split the dataset into train and test sets
X = df[['city_population']]  # Use double brackets to create a DataFrame
y = df['food_truck_profit']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=69, test_size=0.25)

# Load the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict for the test set
y_pred = model.predict(X_test)

# Plot for visualization
plt.scatter(X_test, y_test, color='blue', label='Test Data')
plt.scatter(X_train, y_train, color='green', label='Train Data')
plt.plot(X_test, y_pred, color='red', label='Predicted Line')
plt.xlabel('City Population')
plt.ylabel('Food Truck Profit')
plt.legend()
plt.title('Food Truck Profit Prediction')
plt.show()
