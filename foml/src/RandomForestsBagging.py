import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Generate sample data
np.random.seed(42)
X, y = make_classification(n_samples=300, n_features=4, n_informative=2, 
                           n_redundant=0, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Method 1: Simple manual implementation of Random Forest
class SimpleDecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2, max_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.feature_indices = None
        self.threshold = None
        self.left = None
        self.right = None
        self.value = None
        self.feature_idx = None
    
    def _gini(self, y):
        """Calculate Gini impurity"""
        m = len(y)
        if m == 0:
            return 0
        counts = Counter(y)
        impurity = 1.0
        for label in counts:
            prob_of_label = counts[label] / m
            impurity -= prob_of_label**2
        return impurity
    
    def _best_split(self, X, y):
        """Find the best split for a node"""
        m, n = X.shape
        if m <= self.min_samples_split:
            return None, None, None
        
        # Consider only a random subset of features
        if self.max_features:
            feature_indices = np.random.choice(n, self.max_features, replace=False)
        else:
            feature_indices = range(n)
        
        best_gain = -float('inf')
        best_feature, best_threshold = None, None
        
        parent_gini = self._gini(y)
        
        for feature_idx in feature_indices:
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                left_indices = X[:, feature_idx] <= threshold
                right_indices = ~left_indices
                
                if sum(left_indices) == 0 or sum(right_indices) == 0:
                    continue
                
                left_gini = self._gini(y[left_indices])
                right_gini = self._gini(y[right_indices])
                n_left, n_right = sum(left_indices), sum(right_indices)
                
                gini_gain = parent_gini - (n_left/m * left_gini + n_right/m * right_gini)
                
                if gini_gain > best_gain:
                    best_gain = gini_gain
                    best_feature = feature_idx
                    best_threshold = threshold
        
        return best_feature, best_threshold, best_gain
    
    def _build_tree(self, X, y, depth=0):
        """Recursively build the decision tree"""
        num_samples_per_class = [np.sum(y == i) for i in np.unique(y)]
        predicted_class = np.argmax(num_samples_per_class)
        node = SimpleDecisionTree(max_depth=self.max_depth, 
                                  min_samples_split=self.min_samples_split,
                                  max_features=self.max_features)
        node.value = predicted_class
        
        # Stop splitting if depth is reached or node is pure
        if (self.max_depth is not None and depth >= self.max_depth) or len(np.unique(y)) == 1:
            return node
        
        feature_idx, threshold, gain = self._best_split(X, y)
        
        if feature_idx is None:
            return node
        
        node.feature_idx = feature_idx
        node.threshold = threshold
        
        # Split the node
        left_indices = X[:, feature_idx] <= threshold
        right_indices = ~left_indices
        
        node.left = self._build_tree(X[left_indices], y[left_indices], depth + 1)
        node.right = self._build_tree(X[right_indices], y[right_indices], depth + 1)
        
        return node
    
    def fit(self, X, y):
        """Build the decision tree"""
        self.n_classes = len(np.unique(y))
        self.n_features = X.shape[1]
        self.tree = self._build_tree(X, y)
        return self
    
    def _predict_sample(self, x, node):
        """Predict class for a single sample"""
        if node.feature_idx is None:
            return node.value
        
        if x[node.feature_idx] <= node.threshold:
            return self._predict_sample(x, node.left)
        else:
            return self._predict_sample(x, node.right)
    
    def predict(self, X):
        """Predict classes for samples in X"""
        return np.array([self._predict_sample(x, self.tree) for x in X])

class SimpleRandomForest:
    def __init__(self, n_estimators=100, max_depth=None, min_samples_split=2, max_features=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.trees = []
    
    def fit(self, X, y):
        """Build the random forest"""
        n_samples, n_features = X.shape
        
        # Set max_features if not specified
        if self.max_features is None:
            self.max_features = int(np.sqrt(n_features))
        
        # Create n_estimators decision trees
        for _ in range(self.n_estimators):
            # Bootstrap sampling
            indices = np.random.choice(n_samples, n_samples, replace=True)
            X_bootstrap = X[indices]
            y_bootstrap = y[indices]
            
            # Create and train a decision tree
            tree = SimpleDecisionTree(max_depth=self.max_depth, 
                                      min_samples_split=self.min_samples_split,
                                      max_features=self.max_features)
            tree.fit(X_bootstrap, y_bootstrap)
            self.trees.append(tree)
        
        return self
    
    def predict(self, X):
        """Predict classes for samples in X"""
        # Get predictions from all trees
        predictions = np.array([tree.predict(X) for tree in self.trees])
        
        # Return majority vote for each sample
        return np.array([Counter(predictions[:, i]).most_common(1)[0][0] for i in range(X.shape[0])])

# Train simplified random forest (with fewer trees for demonstration)
simple_rf = SimpleRandomForest(n_estimators=10, max_depth=5)
simple_rf.fit(X_train, y_train)
y_pred_manual = simple_rf.predict(X_test)
accuracy_manual = accuracy_score(y_test, y_pred_manual)
print(f"Manual Random Forest accuracy: {accuracy_manual:.4f}")

# Method 2: Using scikit-learn
# For comparison, also train a single decision tree
single_tree = DecisionTreeClassifier(random_state=42)
single_tree.fit(X_train, y_train)
y_pred_tree = single_tree.predict(X_test)
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print(f"Single Decision Tree accuracy: {accuracy_tree:.4f}")

# Train Random Forest
sklearn_rf = RandomForestClassifier(n_estimators=100, random_state=42)
sklearn_rf.fit(X_train, y_train)
y_pred_sklearn = sklearn_rf.predict(X_test)
accuracy_sklearn = accuracy_score(y_test, y_pred_sklearn)
print(f"Scikit-learn Random Forest accuracy: {accuracy_sklearn:.4f}")

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_sklearn))

# Print confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_sklearn))

# Visualize feature importance
plt.figure(figsize=(10, 6))
importances = sklearn_rf.feature_importances_
indices = np.argsort(importances)[::-1]

plt.title("Feature Importances from Random Forest")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.tight_layout()
plt.show()

# Visualize predictions (for 2D data, using first two features)
def plot_decision_boundaries(X, y, models, model_names):
    # Reduce to first two dimensions for visualization
    X_2d = X[:, :2]
    
    # Set up the figure
    n_models = len(models)
    fig, axes = plt.subplots(1, n_models, figsize=(n_models*5, 4))
    if n_models == 1:
        axes = [axes]
    
    # Define mesh grid
    h = 0.02  # Step size
    x_min, x_max = X_2d[:, 0].min() - 1, X_2d[:, 0].max() + 1
    y_min, y_max = X_2d[:, 1].min() - 1, X_2d[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # Plot decision boundaries and scatter plot for each model
    for idx, (model, name, ax) in enumerate(zip(models, model_names, axes)):
        # For simplified model
        if hasattr(model, 'trees'):
            # Create dummy features for unused dimensions
            if X.shape[1] > 2:
                dummy_features = np.zeros((xx.ravel().shape[0], X.shape[1]-2))
                mesh_points = np.column_stack([xx.ravel(), yy.ravel(), dummy_features])
            else:
                mesh_points = np.c_[xx.ravel(), yy.ravel()]
            Z = model.predict(mesh_points)
        else:
            # For scikit-learn models
            if X.shape[1] > 2:
                # Use feature means for the other dimensions
                feature_means = X[:, 2:].mean(axis=0)
                dummy_features = np.tile(feature_means, (xx.ravel().shape[0], 1))
                mesh_points = np.column_stack([xx.ravel(), yy.ravel(), dummy_features])
            else:
                mesh_points = np.c_[xx.ravel(), yy.ravel()]
            Z = model.predict(mesh_points)
        
        # Reshape Z for contour plot
        Z = Z.reshape(xx.shape)
        
        # Plot decision boundary
        ax.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
        ax.scatter(X_2d[:, 0], X_2d[:, 1], c=y, cmap='viridis', edgecolors='k')
        ax.set_title(name)
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
    
    plt.tight_layout()
    plt.show()

# Visualize decision boundaries
plot_decision_boundaries(
    X_test, 
    y_test, 
    [single_tree, sklearn_rf], 
    ["Single Decision Tree", "Random Forest"]
)