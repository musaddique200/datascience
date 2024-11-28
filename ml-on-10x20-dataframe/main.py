import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Create the dataset
np.random.seed(1)

data = {
    "Hours_Studied": np.random.randint(5, 15, 20),
    "Attendance": np.random.randint(50, 100, 20),
    "Assignments_Completed": np.random.randint(5, 15, 20),
    "Quiz_Score": np.random.randint(50, 100, 20),
    "Participation": np.random.randint(50, 100, 20),
    "Previous_Grade": np.random.randint(60, 100, 20),
    "Extra_Activities": np.random.randint(0, 5, 20),
    "Sleep_Hours": np.random.uniform(6, 9, 20).round(1),
    "Stress_Level": np.random.randint(1, 10, 20),
    "Internet_Usage": np.random.uniform(2, 6, 20).round(1),
}

# Create the target variable
data["Final_Grade"] = (
    0.4 * data["Hours_Studied"] +
    0.3 * data["Attendance"] +
    0.2 * data["Assignments_Completed"] +
    0.2 * data["Quiz_Score"] +
    0.1 * data["Participation"] +
    0.3 * data["Previous_Grade"] -
    0.1 * data["Stress_Level"] +
    np.random.normal(0, 5, 20)  # Adding small noise
).astype(int)

df = pd.DataFrame(data)

# Step 2: Define features (X) and target (y)
X = df.drop(columns=["Final_Grade"])
y = df["Final_Grade"]

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Step 6: Display results
print("Dataset:")
print(df)
print("Mean Squared Error:", mse)

