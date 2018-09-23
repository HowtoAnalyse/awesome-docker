# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:55:47 2018

@author: sara.zeng
"""

from tpot import TPOTClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import os

ckpt_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), "runs")
if not os.path.isdir(ckpt_folder):
    os.makedirs(ckpt_folder)
print("Check point folder: %s" % ckpt_folder)

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data.astype(np.float64),
    iris.target.astype(np.float64), train_size=0.75, test_size=0.25)

tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2,periodic_checkpoint_folder=ckpt_folder)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
tpot.export(ckpt_folder+'/tpot_iris_pipeline.py')
