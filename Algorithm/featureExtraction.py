from sklearn.decomposition import PCA

# Load the data
X = sampled_Data

# Create a PCA object
pca = PCA(n_components=2)

# Fit the PCA model to the data
pca.fit(X)

# Transform the data using the PCA model
X_pca = pca.transform(X)
