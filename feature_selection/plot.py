import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from config import data_path

def create_plot(data_path):
    # collect results
    STEP_SIZE = 1000
    f1_class_0 = []
    for idx in range(STEP_SIZE, 30*STEP_SIZE+1, STEP_SIZE):
        with open(data_path+f"feature_selection/res_{idx}") as f:
            res = []
            for fold in json.load(f):
                res.append(fold['0']['f1-score'])
            res.append(np.mean(res))
            f1_class_0.append(res)
    f1_class_0 = np.array(f1_class_0)
    # create a plot
    plt.figure(figsize=(16, 6))
    plt.title("f1 score for class 0 per number of features used", fontdict = {'fontsize' : 30})
    x = [idx for idx in range(STEP_SIZE, 30*STEP_SIZE+1, STEP_SIZE)]
    plt.plot(x, f1_class_0[:, 0], label='fold #1', linestyle='--')
    plt.plot(x, f1_class_0[:, 1], label='fold #2', linestyle='--')
    plt.plot(x, f1_class_0[:, 2], label='fold #3', linestyle='--')
    plt.plot(x, f1_class_0[:, 3], label='fold #4', linestyle='--')
    plt.plot(x, f1_class_0[:, 4], label='fold #5', linestyle='--')
    plt.plot(x, f1_class_0[:, 5], label='average', linewidth=5)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.legend(fontsize=20)
    plt.savefig('feature_selection/logreg_f1_class0.png')

if __name__ == "__main__":
    create_plot(data_path)