import os
import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from config import RANDOM_STATE, N_SPLITS,\
                   features_path, targets_path, gwas_results_path, data_path

def cv_logreg(features, phenotypes):
    res = []
    skf = StratifiedKFold(n_splits=N_SPLITS, random_state=RANDOM_STATE, shuffle=True)
    for train_index, test_index in skf.split(features, phenotypes):
        X_train, X_test = features[train_index], features[test_index]
        y_train, y_test = phenotypes[train_index], phenotypes[test_index]
        clf = LogisticRegression(verbose=0)
        clf.fit(X_train, y_train)
        pred = clf.predict(X_test)
        metrics = classification_report(y_test, pred, output_dict=True)
        res.append(metrics)
    return res

def greedy(features, phenotypes, pvals):
    STEP_SIZE = 1000
    idx = np.argsort(pvals)
    for n_features in tqdm(range(30*STEP_SIZE, STEP_SIZE-1, -STEP_SIZE)):
        res = cv_logreg(features[:, idx[:n_features]], phenotypes)
        with open(data_path+f"feature_selection/res_{n_features}", "w") as f:
            json.dump(res, f)

if __name__ == "__main__":
    features = np.load(features_path)
    phenotypes = np.array(np.load(targets_path, allow_pickle=True)) - 1 # (1, 2) -> (0, 1)
    pvals = pd.read_csv(gwas_results_path)["p_val"].to_numpy()
    greedy(features, phenotypes, pvals)