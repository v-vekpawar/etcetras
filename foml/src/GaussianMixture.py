import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# 1. Generate and split data
np.random.seed(42)
X, y = make_blobs(n_samples=200, centers=2, n_features=2, random_state=42, cluster_std=1.5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 2. Standardize data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Fit GMM
gmm = GaussianMixture(n_components=2, covariance_type='full', random_state=42)
gmm.fit(X_train_scaled)

# 4. Predict and adjust labels
train_labels = gmm.predict(X_train_scaled)
test_labels = gmm.predict(X_test_scaled)

# Flip labels if needed
if accuracy_score(y_train, train_labels) < 0.5:
    train_labels = 1 - train_labels
    test_labels = 1 - test_labels

# 5. Evaluate
accuracy = accuracy_score(y_test, test_labels)
print(f"GMM Classification Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, test_labels))
print("Confusion Matrix:")
print(confusion_matrix(y_test, test_labels))

# 6. Plotting function
def plot_decision_boundary(X, y, model, scaler, title):
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # Flatten grid and scale it
    grid = np.c_[xx.ravel(), yy.ravel()]
    grid_scaled = scaler.transform(grid)
    Z = model.predict(grid_scaled)
    Z = Z.reshape(xx.shape)

    # Plot
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.tight_layout()

# 7. Plot
plt.figure(figsize=(6, 5))
plot_decision_boundary(X_test, test_labels, gmm, scaler, 'GMM Decision Boundary (Original Scale)')
plt.show()
