from sklearn import tree
from learner import Learner
import numpy as np


class DTLearner(Learner):

    def __init__(self, criterion='gini', min_samples_leaf=1, max_depth=None, class_weight=None):
        self.estimator = tree.DecisionTreeClassifier(random_state=78, criterion=criterion,
                                                     min_samples_leaf=min_samples_leaf, max_depth=max_depth,
                                                     class_weight=class_weight)

    def fit_predict_score(self, x_train, y_train, x_test, y_test):

        print(np.unique(y_train))
        print(np.unique(y_test))
        return super(DTLearner, self).fit_predict_score(self.estimator, x_train, y_train, x_test, y_test)

    def draw_tree(self, tree_id=''):
        tree.export_graphviz(self.estimator, out_file = 'tree{0}.dot'.format(tree_id))




