# Student Score Prediction using Machine Learning

## Project Overview
This project is a **Supervised Machine Learning** project that predicts student final exam scores using **Linear Regression**.
The model uses **weekly self-study hours** as an input feature and predicts the total score of students.

---
## Machine Learning Algorithm
- Linear Regression

## Type of Learning
- Supervised Machine Learning

## Features Used
- Weekly Self-Study Hours

## Libraries Used
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Model Evaluation Metrics
The model performance is evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
---

## Model Performance
The Linear Regression model achieved the following results:

| Evaluation Metric | Value |
|-------------------|------:|
| Mean Absolute Error (MAE) | 7.17 |
| Mean Squared Error (MSE) | 81.04 |
| Root Mean Squared Error (RMSE) | 9.00 |
| R² Score | 0.6597 |

**Performance Summary**
The model achieved an **R² score of 0.6597**, meaning it explains approximately **66% of the variation** in students' final exam scores based on **weekly self-study hours**.
This indicates **moderately good predictive performance**. The model can provide useful predictions, but it is **not a perfect prediction model** because student performance is influenced by many factors beyond study hours.


## Data Visualization
The project includes:
- Distribution of Final Exam Scores using Histogram
- Actual Score vs Predicted Score using Linear Regression

### 1. Distribution of Final Exam Scores
The histogram displays how final exam scores are distributed among students. Most students achieved scores between **80 and 100**, indicating that a large portion of the dataset contains high-performing students.

<img width="699" height="425" alt="image" src="https://github.com/user-attachments/assets/d0c3179e-7f15-4ec2-ae44-dcfb0ad45cfe" />

### 2. Model Prediction vs Actual Score
The blue dots represent the **actual student scores**, while the **red regression line** represents the scores predicted by the Linear Regression model. The upward trend indicates a positive relationship between **weekly self-study hours** and **final exam scores**.

<img width="667" height="420" alt="image" src="https://github.com/user-attachments/assets/1a10847d-1372-4122-b50f-c8a670d82389" />
