import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate some sample data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Method 1: Manual implementation using NumPy
# Add a column of ones for the intercept term
X_b = np.c_[np.ones((100, 1)), X]

# Normal equation: θ = (X^T X)^(-1) X^T y
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Get the intercept and slope
intercept = theta_best[0][0]
slope = theta_best[1][0]
print(f"Manual: Intercept = {intercept:.4f}, Slope = {slope:.4f}")

# Make predictions
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta_best)

# Method 2: Using scikit-learn
model = LinearRegression()
model.fit(X, y)
print(f"Scikit-learn: Intercept = {model.intercept_[0]:.4f}, Slope = {model.coef_[0][0]:.4f}")

# Make predictions with scikit-learn
y_pred = model.predict(X)

# Calculate performance metrics
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.7)
plt.plot(X_new, y_predict, 'r-', linewidth=2, label='Manual Regression')
plt.plot(X, y_pred, 'g--', linewidth=2, label='Scikit-learn Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression Example')
plt.show()