#import all required libraries and modules
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

#load csv dataset
data = pd.read_csv("student_performance_prediction_datasets.csv")

#Input and Output
X = data[["weekly_self_study_hours"]]
y = data["final_score"]

#train model
model = LinearRegression()
model.fit(X, y)
predicted_scores = model.predict(X)

#valid regression metrics
mae = mean_absolute_error(y, predicted_scores)
mse = mean_squared_error(y, predicted_scores)
rmse = np.sqrt(mse)
r2 = r2_score(y, predicted_scores)

#show result
print("Mean Absolute ERROR (MAE):", round(mae, 2))
print("Mean Squared ERROR (MSE):", round(mse, 2))
print("Root Mean Squared ERROR (RMSE):", round(rmse, 2))
print("R^2 Score (Model Accuracy):", round(r2, 4))   #closer to 1 is better

#histogram
plt.figure(figsize=(10,6))
plt.hist(data["final_score"], bins=30, color="skyblue", edgecolor="black")
plt.title("Distribution of final exam scores")
plt.xlabel("Final exam score")
plt.ylabel("Number of students")
plt.grid(True)
plt.show()

#Scatter + Regression line
plt.figure(figsize=(10,6))
plt.scatter(X, y, color="blue", label="Actual Score")
plt.plot(X, predicted_scores, color='red', label='Predicted Line')
plt.title("Model Prediction VS Actual Score")
plt.xlabel("Self Study hours per week")
plt.ylabel("Final Output")
plt.legend()
plt.grid(True)
plt.show()

#New student study hours
new_hours = pd.DataFrame({
    "weekly_self_study_hours": [9]
})
predicted_new_score = model.predict(new_hours)
print(f"Predicted Final Score for {new_hours['weekly_self_study_hours'][0]} Hours is {predicted_new_score[0]} Score")

