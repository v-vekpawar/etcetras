import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature, self.threshold = feature, threshold
        self.left, self.right, self.value = left, right, value

class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.root = self._grow(X, y)

    def _grow(self, X, y, depth=0):
        if depth >= self.max_depth or len(set(y)) == 1:
            return Node(value=np.bincount(y).argmax())
        feat, thresh = self._best_split(X, y)
        if feat is None:
            return Node(value=np.bincount(y).argmax())
        left = X[:, feat] <= thresh
        return Node(feat, thresh,
                    self._grow(X[left], y[left], depth+1),
                    self._grow(X[~left], y[~left], depth+1))

    def _best_split(self, X, y):
        best_gini, best_feat, best_thresh = 1.0, None, None
        for i in range(X.shape[1]):
            for t in np.unique(X[:, i]):
                left = y[X[:, i] <= t]
                right = y[X[:, i] > t]
                if len(left) == 0 or len(right) == 0: continue
                gini = self._gini(left, right)
                if gini < best_gini:
                    best_gini, best_feat, best_thresh = gini, i, t
        return best_feat, best_thresh

    def _gini(self, left, right):
        def score(y): return 1 - sum((np.sum(y == c)/len(y))**2 for c in np.unique(y))
        total = len(left) + len(right)
        return (len(left)/total)*score(left) + (len(right)/total)*score(right)

    def predict(self, X):
        return np.array([self._traverse(x, self.root) for x in X])

    def _traverse(self, x, node):
        if node.value is not None: return node.value
        return self._traverse(x, node.left if x[node.feature] <= node.threshold else node.right)

# Load data
iris = load_iris()
X, y = iris.data[:, :2], iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate
dt = DecisionTree()
dt.fit(X_train, y_train)
print(f"Accuracy: {np.mean(dt.predict(X_test) == y_test):.4f}")

# Plotting
def plot_boundary(model, X, y):
    xx, yy = np.meshgrid(np.arange(X[:,0].min()-1, X[:,0].max()+1, 0.02),
                         np.arange(X[:,1].min()-1, X[:,1].max()+1, 0.02))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.rainbow, alpha=0.3)
    for i in np.unique(y):
        plt.scatter(*X[y==i].T, label=iris.target_names[i], edgecolors='k')
    plt.xlabel(iris.feature_names[0]); plt.ylabel(iris.feature_names[1])
    plt.title("Decision Tree Boundary"); plt.legend(); plt.tight_layout()

plot_boundary(dt, X, y)
plt.show()
