import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

class SimpleKMeans:
    def __init__(self, n_clusters=3, max_iter=100, random_state=None):
        self.k = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state

    def fit(self, X):
        np.random.seed(self.random_state)
        self.centroids = X[np.random.choice(len(X), self.k, replace=False)]
        for _ in range(self.max_iter):
            labels = self._assign(X)
            new_centroids = np.array([X[labels==i].mean(axis=0) for i in range(self.k)])
            if np.allclose(self.centroids, new_centroids): break
            self.centroids = new_centroids
        self.labels = labels

    def _assign(self, X):
        dists = np.linalg.norm(X[:, None] - self.centroids, axis=2)
        return np.argmin(dists, axis=1)

    def predict(self, X):
        return self._assign(X)

def plot_clusters(X, model, title):
    plt.scatter(X[:, 0], X[:, 1], c=model.labels, cmap='viridis', s=50, alpha=0.7)
    plt.scatter(model.centroids[:, 0], model.centroids[:, 1], c='red', s=200, marker='X')
    plt.title(title); plt.xlabel("Feature 1"); plt.ylabel("Feature 2")
    plt.tight_layout(); plt.show()

# Generate and cluster data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)
kmeans = SimpleKMeans(n_clusters=4, random_state=42)
kmeans.fit(X)
plot_clusters(X, kmeans, "K-Means Clustering (k=4)")
