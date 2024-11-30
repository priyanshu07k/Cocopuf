import numpy as np
import sklearn
from scipy.linalg import khatri_rao
from sklearn import LogisticRegression

# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y0_train, y1_train ):
################################
#  Non Editable Region Ending  #
################################

	train_features = my_map(X_train)
    # responses0 = train_responses[:, 0]
    # responses1 = train_responses[:, 1]

	C_value = 11
	max_iter_value = 10000
	tol_value = 0.001
	model_SVC0 = LogisticRegression( tol=tol_value, C=C_value, max_iter=max_iter_value)   # Using Linear SVC model for classification
	model_SVC0.fit(train_features,y0_train)
	w0 = model_SVC0.coef_.flatten()    # Flattening the original weights extracted from the SVC model
	b0 = model_SVC0.intercept_

	model_SVC1 = LogisticRegression(tol=tol_value, C=C_value, max_iter=max_iter_value)   # Using Linear SVC model for classification
	model_SVC1.fit(train_features,y1_train)
	w1 = model_SVC1.coef_.flatten()    # Flattening the original weights extracted from the SVC model
	b1 = model_SVC1.intercept_

	# Use this method to train your models using training CRPs
	# X_train has 32 columns containing the challenge bits
	# y0_train contains the values for Response0
	# y1_train contains the values for Response1
	
	# THE RETURNED MODELS SHOULD BE TWO VECTORS AND TWO BIAS TERMS
	# If you do not wish to use a bias term, set it to 0
	return w0, b0, w1, b1


################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	n_samples, n_features = X.shape
	feat = np.zeros((n_samples, 2*n_features - 1))

	x_terms = np.zeros((n_samples, n_features-1))
        
	for k in range(n_features - 1):
		product = np.ones((n_samples, 1))
		sum_xk = np.zeros((n_samples, 1))
		for j in range(k, n_features - 1):
			product[:, 0] = np.multiply(product[:, 0], 1 - 2 * X[:, j])
			sum_xk[:, 0] += np.multiply(X[: ,j + 1] , product[:, 0])
		x_terms[:, k] = sum_xk[:, 0]
        
        # Combine into final feature vector
	feat[:, :n_features] = X
	feat[:, n_features:] = x_terms

	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points
	
	return feat
