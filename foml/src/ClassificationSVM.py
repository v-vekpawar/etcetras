import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Generate sample data
np.random.seed(42)
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=42, cluster_std=1.2)
# Make it a bit harder by adjusting class labels
y = 2 * y - 1  # Convert to -1 and 1

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale features (important for SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Method 1: Simple linear SVM implementation (gradient descent)
def linear_svm_train(X, y, learning_rate=0.01, lambda_param=0.01, epochs=1000):
    """
    A simplified implementation of linear SVM using gradient descent.
    This is not a full implementation but demonstrates the core concept.
    """
    # Initialize weights and bias
    n_features = X.shape[1]
    w = np.zeros(n_features)
    b = 0
    
    # Gradient descent
    for epoch in range(epochs):
        for i, x_i in enumerate(X):
            # Check if the point is classified correctly
            condition = y[i] * (np.dot(x_i, w) + b) >= 1
            
            if condition:
                # Correctly classified, update only for regularization
                w = w - learning_rate * (2 * lambda_param * w)
            else:
                # Incorrectly classified, update based on the loss gradient
                w = w - learning_rate * (2 * lambda_param * w - np.dot(x_i, y[i]))
                b = b - learning_rate * (-y[i])
    
    return w, b

def linear_svm_predict(X, w, b):
    """Predict using the simple linear SVM model"""
    return np.sign(np.dot(X, w) + b)

# Train simple linear SVM
w, b = linear_svm_train(X_train_scaled, y_train)
y_pred_manual = linear_svm_predict(X_test_scaled, w, b)
accuracy_manual = accuracy_score(y_test, y_pred_manual)
print(f"Simple linear SVM accuracy: {accuracy_manual:.4f}")
print(f"Weights: {w}, Bias: {b}")

# Method 2: Using scikit-learn
# Linear SVM
linear_svm = svm.SVC(kernel='linear', C=1.0)
linear_svm.fit(X_train_scaled, y_train)
y_pred_linear = linear_svm.predict(X_test_scaled)
accuracy_linear = accuracy_score(y_test, y_pred_linear)
print(f"Scikit-learn linear SVM accuracy: {accuracy_linear:.4f}")
print(f"Coefficients: {linear_svm.coef_[0]}, Intercept: {linear_svm.intercept_[0]}")

# Non-linear SVM with RBF kernel
rbf_svm = svm.SVC(kernel='rbf', C=1.0, gamma='scale')
rbf_svm.fit(X_train_scaled, y_train)
y_pred_rbf = rbf_svm.predict(X_test_scaled)
accuracy_rbf = accuracy_score(y_test, y_pred_rbf)
print(f"Scikit-learn RBF kernel SVM accuracy: {accuracy_rbf:.4f}")

# Print classification report for the best model
best_model = rbf_svm if accuracy_rbf > accuracy_linear else linear_svm
best_pred = y_pred_rbf if accuracy_rbf > accuracy_linear else y_pred_linear
print("\nClassification Report:")
print(classification_report(y_test, best_pred))

# Print confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, best_pred))

# Function to plot decision boundary
def plot_decision_boundary(X, y, model, title):
    h = 0.02  # Step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # For simple linear model
    if isinstance(model, tuple):
        w, b = model
        Z = np.sign(np.dot(np.c_[xx.ravel(), yy.ravel()], w) + b)
    # For sklearn model
    else:
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')
    
    # If it's an SVM model from sklearn, plot support vectors
    if hasattr(model, 'support_vectors_'):
        plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], 
                    s=100, linewidth=1, facecolors='none', edgecolors='red')
    
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')

# Visualize the results
plt.figure(figsize=(15, 5))

# Plot 1: Simple Linear SVM
plt.subplot(1, 3, 1)
plot_decision_boundary(X_test_scaled, y_test, (w, b), 'Simple Linear SVM')

# Plot 2: Scikit-learn Linear SVM
plt.subplot(1, 3, 2)
plot_decision_boundary(X_test_scaled, y_test, linear_svm, 'Scikit-learn Linear SVM')

# Plot 3: Scikit-learn RBF Kernel SVM
plt.subplot(1, 3, 3)
plot_decision_boundary(X_test_scaled, y_test, rbf_svm, 'Scikit-learn RBF Kernel SVM')

plt.tight_layout()
plt.show()