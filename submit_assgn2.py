import numpy as np
from sklearn.tree import DecisionTreeClassifier

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT PERFORM ANY FILE IO IN YOUR CODE

# DO NOT CHANGE THE NAME OF THE METHOD my_fit or my_predict BELOW
# IT WILL BE INVOKED BY THE EVALUATION SCRIPT
# CHANGING THE NAME WILL CAUSE EVALUATION FAILURE

# Decision tree class without hyperparameter tuning
class DecisionTree(DecisionTreeClassifier):
    def __init__(self, 
                 criterion="entropy", 
                 splitter="best", 
                 max_depth=None, 
                 min_samples_split=6, 
                 min_samples_leaf=5, 
                 min_weight_fraction_leaf=0.0, 
                 max_features="log2", 
                 random_state=None, 
                 max_leaf_nodes=None, 
                 min_impurity_decrease=0.001, 
                 class_weight="balanced", 
                 ccp_alpha=0.01):
        super().__init__(
            criterion=criterion, 
            splitter=splitter, 
            max_depth=max_depth, 
            min_samples_split=min_samples_split, 
            min_samples_leaf=min_samples_leaf, 
            min_weight_fraction_leaf=min_weight_fraction_leaf, 
            max_features=max_features, 
            random_state=random_state, 
            max_leaf_nodes=max_leaf_nodes, 
            min_impurity_decrease=min_impurity_decrease, 
            class_weight=class_weight, 
            ccp_alpha=ccp_alpha
        )
        self.tree = {}

    def my_fit(self, words):
        for word in words:
            # Generate bigrams from the word
            bigrams = [''.join(pair) for pair in zip(word, word[1:])]
            bigrams = tuple(sorted(set(bigrams)))[:5]
            self._insert(word, bigrams)
        return self

    def _insert(self, word, bigrams):
        node = self.tree
        for bigram in bigrams:
            if bigram not in node:
                node[bigram] = {}
            node = node[bigram]
        if 'words' not in node:
            node['words'] = []
        node['words'].append(word)

    def my_predict(self, bigram_list):
        node = self.tree
        while True:
            found = False
            for bigram in bigram_list:
                if bigram in node:
                    node = node[bigram]
                    found = True
                    break
            if not found:
                break
        # If exact match is not found, return the most frequent words from the current node
        if 'words' in node:
            word_counts = {}
            for word in node['words']:
                word_counts[word] = word_counts.get(word, 0) + 1
            sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
            return [word for word, count in sorted_words][:5]
        return []



# You may define any new functions, variables, classes here
# For example, classes to create the Tree, Nodes etc

################################
# Non Editable Region Starting #
################################
def my_fit( words ):
################################
#  Non Editable Region Ending  #
################################
	model = DecisionTree()
    
	# Do not perform any file IO in your code
	# Use this method to train your model using the word list provided
	
	return model.my_fit(words)			# Return the trained model


################################
# Non Editable Region Starting #
################################
def my_predict( model, bigram_list ):
################################
#  Non Editable Region Ending  #
################################
	
	# Do not perform any file IO in your code
	# Use this method to predict on a test bigram_list
	# Ensure that you return a list even if making a single guess
	
	return model.my_predict(bigram_list)					# Return guess(es) as a list
