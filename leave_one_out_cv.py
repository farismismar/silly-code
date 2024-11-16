#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:34:05 2024

@author: farismismar
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, LeaveOneOut


seed = 42
df_true = pd.read_csv('3gpp_mcs_table_2.csv')

np_random = np.random.RandomState(seed=42)

y_label = 'I_MCS'

mask = np_random.binomial(n=1, p=0.75, size=df_true.shape[0])
df_available = df_true.loc[mask == 1, :].sample(frac=1, replace=False, random_state=np_random).reset_index(drop=True)
df_missing = df_true.loc[mask == 0, :].reset_index(drop=True)

X_train = df_available.drop(y_label, axis=1).values
y_train = df_available[y_label].values

X_test = df_missing.drop(y_label, axis=1).values
y_test_true = df_missing[y_label].values

rfc = RandomForestClassifier(random_state=seed)

# Define grid space
param_grid = dict(max_depth=[3,5,10,None],
                  n_estimators=[10,100,200],
                  max_features=[1,2,3])

# Cannot use GridSearch since each row has one unique class.
loo = LeaveOneOut()
clf = GridSearchCV(rfc, param_grid, cv=loo)
clf.fit(X_train, y_train)

rfc = clf.best_estimator_

y_test_pred = rfc.predict(X_test)

print(y_test_true)
print(y_test_pred)