import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import KBinsDiscretizer
from matplotlib.colors import ListedColormap
import networkx as nx


class AssociationRuleClassifier:
    def __init__(self, min_support=0.01, min_confidence=0.5, max_rules=100):
        """
        Initialize the classifier.
        
        Parameters:
        -----------
        min_support : float, default=0.01
            Minimum support threshold for rules.
        min_confidence : float, default=0.5
            Minimum confidence threshold for rules.
        max_rules : int, default=100
            Maximum number of rules to keep.
        """
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.max_rules = max_rules
        self.rules = []
        self.class_column = None
        self.default_class = None
        self.feature_names = None
        
    def _count_itemsets(self, data, items):
        """Count occurrences of an itemset in the data."""
        count = 0
        for _, row in data.iterrows():
            match = True
            for col, val in items:
                if row[col] != val:
                    match = False
                    break
            if match:
                count += 1
        return count
    
    def _generate_candidate_rules(self, data):
        """Generate candidate rules from the data."""
        n_samples = len(data)
        rules = []
        
        # Generate rules from individual feature values
        for feature in data.columns:
            if feature == self.class_column:
                continue
                
            for feature_val in data[feature].unique():
                # Antecedent: feature=value
                antecedent = [(feature, feature_val)]
                antecedent_count = self._count_itemsets(data, antecedent)
                
                # Skip if antecedent support is too low
                antecedent_support = antecedent_count / n_samples
                if antecedent_support < self.min_support:
                    continue
                
                # Generate rules for each class value
                for class_val in data[self.class_column].unique():
                    # Full itemset: feature=value AND class=value
                    full_itemset = antecedent + [(self.class_column, class_val)]
                    full_count = self._count_itemsets(data, full_itemset)
                    
                    # Calculate metrics
                    support = full_count / n_samples
                    confidence = full_count / antecedent_count if antecedent_count > 0 else 0
                    
                    # Check thresholds
                    if support >= self.min_support and confidence >= self.min_confidence:
                        rules.append({
                            'antecedent': antecedent,
                            'consequent': [(self.class_column, class_val)],
                            'support': support,
                            'confidence': confidence,
                            'lift': confidence / (data[self.class_column] == class_val).mean() if (data[self.class_column] == class_val).mean() > 0 else 0
                        })
        
        return rules
    
    def fit(self, X, y):
        """
        Fit the classifier to the training data.
        
        Parameters:
        -----------
        X : DataFrame
            Feature data.
        y : Series
            Target labels.
        
        Returns:
        --------
        self : object
        """
        # Store feature names
        self.feature_names = X.columns
        
        # Prepare data
        data = X.copy()
        self.class_column = y.name if hasattr(y, 'name') else 'class'
        data[self.class_column] = y
        
        # Set default class (most frequent)
        self.default_class = y.value_counts().idxmax()
        
        # Generate candidate rules
        rules = self._generate_candidate_rules(data)
        
        # Sort rules by confidence, support, and then by number of conditions (simpler rules first)
        rules.sort(key=lambda x: (-x['confidence'], -x['support'], len(x['antecedent'])))
        
        # Keep only the top rules
        self.rules = rules[:self.max_rules]
        
        print(f"Generated {len(self.rules)} classification rules")
        return self
    
    def predict(self, X):
        """
        Predict class labels for samples in X.
        
        Parameters:
        -----------
        X : DataFrame
            The samples to predict.
            
        Returns:
        --------
        y_pred : ndarray
            The predicted classes.
        """
        if not self.rules:
            raise ValueError("Model has not been fitted yet.")
        
        y_pred = []
        
        for _, instance in X.iterrows():
            # Try to find a matching rule
            matched_class = None
            
            for rule in self.rules:
                antecedent = rule['antecedent']
                
                # Check if rule matches
                match = True
                for col, val in antecedent:
                    if instance[col] != val:
                        match = False
                        break
                
                if match:
                    # Rule matches, get the class
                    matched_class = rule['consequent'][0][1]
                    break
            
            # If no rule matched, use default class
            if matched_class is None:
                matched_class = self.default_class
                
            y_pred.append(matched_class)
        
        return np.array(y_pred)
    
    def get_top_rules(self, n=10):
        """Return the top n rules by confidence."""
        return self.rules[:min(n, len(self.rules))]
    
    # Visualization methods
    def plot_rule_metrics(self, n=10):
        """Plot support vs confidence for top n rules."""
        if not self.rules:
            raise ValueError("Model has not been fitted yet.")
        
        top_rules = self.get_top_rules(n)
        
        # Extract metrics
        confidences = [rule['confidence'] for rule in top_rules]
        supports = [rule['support'] for rule in top_rules]
        lifts = [rule['lift'] for rule in top_rules]
        
        # Create labels for each rule
        rule_labels = []
        for i, rule in enumerate(top_rules):
            ant_str = " AND ".join([f"{col}={val}" for col, val in rule['antecedent']])
            cons_str = " AND ".join([f"{col}={val}" for col, val in rule['consequent']])
            rule_labels.append(f"R{i+1}: IF {ant_str} THEN {cons_str}")
        
        # Create a bubble chart
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(supports, confidences, s=[l*100 for l in lifts], alpha=0.6)
        
        # Add labels
        for i, label in enumerate(rule_labels):
            plt.annotate(f"R{i+1}", (supports[i], confidences[i]), 
                         xytext=(5, 5), textcoords='offset points')
        
        plt.xlabel('Support')
        plt.ylabel('Confidence')
        plt.title('Rule Metrics: Support vs Confidence (bubble size = lift)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Add legend for rule descriptions
        plt.figtext(0.1, -0.05, "\n".join(rule_labels), wrap=True, horizontalalignment='left')
        
        return plt
    
    def plot_feature_importance(self):
        """Plot feature importance based on rule participation."""
        if not self.rules:
            raise ValueError("Model has not been fitted yet.")
        
        # Count feature occurrences in rules
        feature_counts = defaultdict(int)
        for rule in self.rules:
            for feature, _ in rule['antecedent']:
                feature_counts[feature] += 1
        
        # Convert to DataFrame for plotting
        feature_df = pd.DataFrame({
            'Feature': list(feature_counts.keys()),
            'Count': list(feature_counts.values())
        }).sort_values('Count', ascending=False)
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Count', y='Feature', data=feature_df)
        plt.title('Feature Importance (Rule Participation Count)')
        plt.xlabel('Number of Rules')
        plt.ylabel('Feature')
        plt.tight_layout()
        
        return plt
    
    def plot_rule_network(self, n=10):
        """Plot network representation of top n rules."""
        if not self.rules:
            raise ValueError("Model has not been fitted yet.")
        
        top_rules = self.get_top_rules(n)
        
        # Create a network graph
        G = nx.DiGraph()
        
        # Add nodes for features and class values
        for rule in top_rules:
            # Add feature nodes
            for feature, value in rule['antecedent']:
                node_id = f"{feature}={value}"
                if node_id not in G:
                    G.add_node(node_id, type='feature')
            
            # Add class node
            class_feature, class_value = rule['consequent'][0]
            class_node = f"{class_feature}={class_value}"
            if class_node not in G:
                G.add_node(class_node, type='class')
            
            # Add edges from features to class
            for feature, value in rule['antecedent']:
                feature_node = f"{feature}={value}"
                G.add_edge(feature_node, class_node, weight=rule['confidence'])
        
        # Set up the plot
        plt.figure(figsize=(12, 10))
        
        # Define node colors
        node_colors = ['skyblue' if G.nodes[n]['type'] == 'feature' else 'lightcoral' for n in G.nodes]
        
        # Define edge weights for thickness
        edge_weights = [G[u][v]['weight'] * 3 for u, v in G.edges]
        
        # Define layout
        pos = nx.spring_layout(G, k=0.3, iterations=50)
        
        # Draw the graph
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800, alpha=0.8)
        nx.draw_networkx_edges(G, pos, width=edge_weights, alpha=0.6, edge_color='gray', arrows=True, arrowsize=20)
        nx.draw_networkx_labels(G, pos, font_size=10)
        
        plt.title('Rule Network (edge thickness = confidence)')
        plt.axis('off')
        plt.tight_layout()
        
        return plt
    
    def plot_confusion_matrix(self, X_test, y_test):
        """Plot confusion matrix for test data."""
        y_pred = self.predict(X_test)
        
        cm = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                    xticklabels=np.unique(y_test), 
                    yticklabels=np.unique(y_test))
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        
        return plt
    
    def plot_decision_boundary_2d(self, X, y, feature1_idx=0, feature2_idx=1, resolution=100):
        """
        Plot 2D decision boundary using two selected features.
        
        Parameters:
        -----------
        X : DataFrame
            Feature data.
        y : Series
            Target labels.
        feature1_idx, feature2_idx : int
            Indices of the two features to use for plotting.
        resolution : int
            Resolution of the grid.
        """
        # Extract the two features
        features = list(self.feature_names)
        feature1 = features[feature1_idx]
        feature2 = features[feature2_idx]
        
        # Create a mesh grid
        x_min, x_max = X[feature1].min() - 0.5, X[feature1].max() + 0.5
        y_min, y_max = X[feature2].min() - 0.5, X[feature2].max() + 0.5
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, resolution),
                             np.linspace(y_min, y_max, resolution))
        
        # Create a DataFrame with the mesh grid values
        mesh_df = pd.DataFrame({
            feature1: xx.ravel(),
            feature2: yy.ravel()
        })
        
        # Fill in other features with median values
        for feat in features:
            if feat not in [feature1, feature2]:
                mesh_df[feat] = X[feat].median()
        
        # Make predictions
        Z = self.predict(mesh_df)
        Z = np.array([list(np.unique(y)).index(z) for z in Z])
        Z = Z.reshape(xx.shape)
        
        # Plot the decision boundary
        plt.figure(figsize=(10, 8))
        
        # Create a color map
        cmap = ListedColormap(['#FF9999', '#66B2FF', '#99FF99'])
        
        # Plot the decision boundary
        plt.contourf(xx, yy, Z, alpha=0.3, cmap=cmap)
        
        # Plot the training points
        scatter = plt.scatter(X[feature1], X[feature2], c=[list(np.unique(y)).index(cls) for cls in y], 
                             cmap=cmap, edgecolor='k', s=60)
        
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.title(f'Decision Boundary ({feature1} vs {feature2})')
        plt.colorbar(scatter)
        plt.tight_layout()
        
        return plt


# Load data
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target_names[iris.target], name='species')

# Discretize continuous features (association rules work better with categorical data)
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
X_disc = pd.DataFrame(discretizer.fit_transform(X), columns=X.columns)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_disc, y, test_size=0.3, random_state=42)

# Train classifier
classifier = AssociationRuleClassifier(min_support=0.05, min_confidence=0.7)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

# Display top rules
print("\nTop Classification Rules:")
for i, rule in enumerate(classifier.get_top_rules(5)):
    ant_str = " AND ".join([f"{col}={val}" for col, val in rule['antecedent']])
    cons_str = " AND ".join([f"{col}={val}" for col, val in rule['consequent']])
    print(f"Rule {i+1}: IF {ant_str} THEN {cons_str} (conf={rule['confidence']:.2f}, supp={rule['support']:.2f})")

# Create visualizations
plt.figure(figsize=(15, 10))

# 1. Visualize rule metrics
plt.subplot(2, 2, 1)
classifier.plot_rule_metrics(10)
plt.tight_layout()

# 2. Feature importance visualization
plt.subplot(2, 2, 2)
classifier.plot_feature_importance()
plt.tight_layout()

# 3. Confusion matrix
plt.subplot(2, 2, 3)
classifier.plot_confusion_matrix(X_test, y_test)
plt.tight_layout()

# 4. Decision boundary (for the first two features)
plt.subplot(2, 2, 4)
classifier.plot_decision_boundary_2d(X_disc, y)
plt.tight_layout()

plt.savefig('association_rule_classifier_visualizations.png', dpi=300, bbox_inches='tight')
plt.show()

# Rule network visualization (separate figure due to size)
plt.figure(figsize=(12, 10))
classifier.plot_rule_network(10)
plt.savefig('rule_network_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

# Display interpretable rules in a heatmap
def plot_rule_heatmap(classifier, n=10):
    """Visualize top rules as a heatmap."""
    top_rules = classifier.get_top_rules(n)
    
    # Prepare data for heatmap
    features = list(set([col for rule in top_rules for col, _ in rule['antecedent']]))
    features.sort()
    
    # Create rule matrix
    rule_matrix = np.zeros((len(top_rules), len(features)))
    
    # Fill the matrix
    for i, rule in enumerate(top_rules):
        class_val = rule['consequent'][0][1]
        for j, feature in enumerate(features):
            for col, val in rule['antecedent']:
                if col == feature:
                    rule_matrix[i, j] = val + 1  # +1 to avoid 0 (which would be interpreted as missing)
    
    # Create a DataFrame for the heatmap
    rule_df = pd.DataFrame(rule_matrix, columns=features)
    
    # Get class values for each rule
    class_values = [rule['consequent'][0][1] for rule in top_rules]
    
    # Add confidence and support
    confidences = [f"{rule['confidence']:.2f}" for rule in top_rules]
    supports = [f"{rule['support']:.2f}" for rule in top_rules]
    
    # Create row labels
    row_labels = [f"R{i+1} ({class_values[i]})" for i in range(len(top_rules))]
    
    # Plot heatmap
    plt.figure(figsize=(12, 8))
    ax = sns.heatmap(rule_df, cmap="YlGnBu", annot=True, fmt=".0f", linewidths=.5, 
                     yticklabels=row_labels, cbar_kws={'label': 'Feature Value'})
    
    plt.title("Rule Heatmap (Rules vs Features)")
    plt.ylabel("Rules (Class)")
    plt.xlabel("Features")
    
    # Add a second axis for confidence and support
    ax2 = ax.twinx()
    ax2.set_yticks(np.arange(0.5, len(top_rules) + 0.5))
    ax2.set_yticklabels([f"C={c}, S={s}" for c, s in zip(confidences, supports)])
    ax2.set_ylabel("Confidence, Support")
    
    plt.tight_layout()
    return plt

# Plot rule heatmap
plot_rule_heatmap(classifier)
plt.savefig('rule_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()