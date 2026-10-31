import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from scipy.optimize import minimize

# Generate sample data for binary classification
np.random.seed(42)
X = np.random.randn(100, 2)  # 100 samples with 2 features
# Create two clusters
X[:50, :] = X[:50, :] - 2  # First cluster centered at (-2, -2)
X[50:, :] = X[50:, :] + 2  # Second cluster centered at (2, 2)
y = np.zeros(100)
y[50:] = 1  # Labels: 0 for first cluster, 1 for second cluster

# Method 1: Manual implementation
def sigmoid(z):
    """Sigmoid function"""
    return 1 / (1 + np.exp(-z))

def cost_function(theta, X, y):
    """Logistic regression cost function"""
    m = len(y)
    h = sigmoid(X.dot(theta))
    cost = -1/m * (y.dot(np.log(h)) + (1-y).dot(np.log(1-h)))
    return cost

def predict(theta, X):
    """Predict class labels"""
    return sigmoid(X.dot(theta)) >= 0.5

# Add a column of ones for the intercept term
X_b = np.c_[np.ones((100, 1)), X]

# Initial theta values
initial_theta = np.zeros(3)

# Minimize the cost function
result = minimize(cost_function, initial_theta, args=(X_b, y), method='BFGS')
theta_best = result.x

# Make predictions
y_pred_manual = predict(theta_best, X_b)
accuracy_manual = np.mean(y_pred_manual == y)
print(f"Manual implementation accuracy: {accuracy_manual:.4f}")
print(f"Manual implementation coefficients: {theta_best}")

# Method 2: Using scikit-learn
model = LogisticRegression(random_state=42)
model.fit(X, y)
y_pred_sklearn = model.predict(X)
accuracy_sklearn = accuracy_score(y, y_pred_sklearn)
print(f"Scikit-learn implementation accuracy: {accuracy_sklearn:.4f}")
print(f"Scikit-learn coefficients: {model.intercept_[0]:.4f}, {model.coef_[0][0]:.4f}, {model.coef_[0][1]:.4f}")

# Print classification report
print("\nClassification Report:")
print(classification_report(y, y_pred_sklearn))

# Print confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y, y_pred_sklearn))

# Visualize the results
plt.figure(figsize=(12, 5))

# Plot 1: Data points and decision boundary for manual implementation
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')

# Create a grid to plot decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))
Z = predict(theta_best, np.c_[np.ones(xx.ravel().shape), xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contour(xx, yy, Z, colors='red', levels=[0.5])
plt.title("Manual Logistic Regression")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Plot 2: Data points and decision boundary for scikit-learn
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')

# Create a grid to plot decision boundary
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contour(xx, yy, Z, colors='red', levels=[0.5])
plt.title("Scikit-learn Logistic Regression")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.tight_layout()
plt.show()