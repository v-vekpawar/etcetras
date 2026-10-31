import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class GaussianNB:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.means = {c: X[y==c].mean(axis=0) for c in self.classes}
        self.vars = {c: X[y==c].var(axis=0) + 1e-10 for c in self.classes}
        self.priors = {c: np.mean(y==c) for c in self.classes}

    def _pdf(self, x, mean, var):
        return np.exp(-0.5 * ((x - mean)**2) / var) / np.sqrt(2 * np.pi * var)

    def _posterior(self, x):
        return max(self.classes, key=lambda c: np.log(self.priors[c]) + 
                   np.sum(np.log(self._pdf(x, self.means[c], self.vars[c]))))

    def predict(self, X):
        return np.array([self._posterior(x) for x in X])

# Load and split data
iris = load_iris()
X, y = iris.data[:, :2], iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate
model = GaussianNB()
model.fit(X_train, y_train)
print(f"Accuracy: {accuracy_score(y_test, model.predict(X_test)):.4f}")

# Plot decision boundary
def plot_decision_boundary(X, y, model):
    x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
    y_min, y_max = X[:,1].min()-1, X[:,1].max()+1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)
    colors = ['red', 'green', 'blue']
    for i, c in enumerate(colors):
        plt.scatter(*X[y==i].T, c=c, label=iris.target_names[i], edgecolor='k', alpha=0.7)
    plt.xlabel('Sepal length'); plt.ylabel('Sepal width')
    plt.title('Naive Bayes Decision Boundary'); plt.legend()

plt.figure(figsize=(8, 5))
plot_decision_boundary(X_train, y_train, model)
plt.tight_layout()
plt.show()
