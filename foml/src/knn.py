import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Generate sample data
np.random.seed(42)
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, 
                           n_informative=2, random_state=42, n_clusters_per_class=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Method 1: Manual implementation
def euclidean_distance(x1, x2):
    """Calculate Euclidean distance between two points"""
    return np.sqrt(np.sum((x1 - x2) ** 2))

def knn_predict(X_train, y_train, X_test, k=3):
    """KNN classification algorithm"""
    y_pred = []
    
    for test_point in X_test:
        # Calculate distances to all training points
        distances = []
        for i, train_point in enumerate(X_train):
            dist = euclidean_distance(test_point, train_point)
            distances.append((dist, y_train[i]))
        
        # Sort distances and get top k neighbors
        distances.sort(key=lambda x: x[0])
        neighbors = distances[:k]
        
        # Get most common class among neighbors
        neighbor_classes = [label for _, label in neighbors]
        most_common = Counter(neighbor_classes).most_common(1)
        y_pred.append(most_common[0][0])
    
    return np.array(y_pred)

# Make predictions using manual implementation
k = 3
y_pred_manual = knn_predict(X_train, y_train, X_test, k)
accuracy_manual = accuracy_score(y_test, y_pred_manual)
print(f"Manual KNN accuracy with k={k}: {accuracy_manual:.4f}")

# Method 2: Using scikit-learn
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
y_pred_sklearn = knn.predict(X_test)
accuracy_sklearn = accuracy_score(y_test, y_pred_sklearn)
print(f"Scikit-learn KNN accuracy with k={k}: {accuracy_sklearn:.4f}")

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_sklearn))

# Print confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_sklearn))

# Visualize the results
plt.figure(figsize=(15, 5))

# Plot 1: Training data points
plt.subplot(1, 3, 1)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', edgecolors='k', s=50)
plt.title("Training Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Plot 2: Manual KNN predictions
plt.subplot(1, 3, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_manual, cmap='viridis', marker='s', s=50, alpha=0.8)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', edgecolors='k', s=20)
plt.title(f"Manual KNN (k={k})")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# Plot 3: Scikit-learn KNN predictions with decision boundary
plt.subplot(1, 3, 3)

# Create a grid for plotting decision boundary
h = 0.02  # Step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict class for each point in the mesh
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')

# Plot test points
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', edgecolors='k', s=50)
plt.title(f"Sklearn KNN (k={k}) with Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.tight_layout()
plt.show()