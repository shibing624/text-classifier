# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief:

from mlxtend.classifier import EnsembleVoteClassifier, StackingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


def get_model(model_type):
    if model_type == "logistic_regression":
        model = LogisticRegression()  # 快，准确率一般。val mean acc:0.91
    elif model_type == "random_forest":
        model = RandomForestClassifier(n_estimators=300)  # 速度还行，准确率一般。val mean acc:0.93125
    elif model_type == "decision_tree":
        model = DecisionTreeClassifier()  # 速度快，准确率低。val mean acc:0.62
    elif model_type == "knn":
        model = KNeighborsClassifier()  # 速度一般，准确率低。val mean acc:0.675
    elif model_type == "bayes":
        model = MultinomialNB()  # 速度快，准确率低。val mean acc:0.62
    elif model_type == "xgboost":
        model = XGBClassifier()  # 速度慢，准确率高。val mean acc:0.95
    elif model_type == "svm":
        model = SVC(kernel='linear', probability=True)  # 速度慢，准确率高，val mean acc:0.945
    elif model_type == 'mlp':
        model = MLPClassifier()  # 速度一般，准确率一般。val mean acc:0.89125
    elif model_type == 'ensemble':
        clf1 = LogisticRegression(random_state=0)
        clf2 = XGBClassifier(random_state=0)
        clf3 = SVC(random_state=0, kernel='linear', probability=True)
        clf4 = MLPClassifier(random_state=0)
        model = EnsembleVoteClassifier(clfs=[clf1, clf2, clf3, clf4],
                                       weights=[1, 2, 2, 1], voting='soft', verbose=2)
    elif model_type == 'stack':
        clf1 = XGBClassifier(random_state=0)
        clf2 = SVC(random_state=0, kernel='linear', probability=True)
        clf3 = MLPClassifier(random_state=0)
        lr = LogisticRegression()
        model = StackingClassifier(classifiers=[clf1, clf2, clf3],
                                   use_probas=True,
                                   average_probas=False,
                                   meta_classifier=lr)
    return model
