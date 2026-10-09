import numpy as np
# import matplotlib.pyplot as plt
np.random.seed(0)

Xtrain = np.load("train_features.npy")
Xtest = np.load("test_features.npy")
ytrain = np.load("train_labels.npy")
ytest = np.load("test_labels.npy")

feature_names = np.load("feature_names.npy", allow_pickle=True)
print("First feature name: ", feature_names[0])
print("Lot frontage for first train sample:", Xtrain[0,0])
print("Feature names: ", feature_names)
