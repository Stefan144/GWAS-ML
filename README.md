# Genome-Wide Association Studies of Ischemic Stroke Based on Interpretable Machine Learning


## Description
This repo contains the scripts used for the experiments presented in the article:

Nikolić S., Ignatov D., Khvorykh G., Limborska S., and Khrunin A., Genome-Wide Association Studies of Ischemic Stroke Based on Interpretable Machine Learning, PeerJ Computer Science, 2024 (in press).
 
    
# Overview

## Requirements
- ```requirements.txt```

## Code sections
- ```feature_selection``` contains the scripts for performing the procedure to obtain figure 1 in paper
- ```gwas``` contains the scripts for performing GWAS and obtaining manhattan plot used in figure 2 in paper
- ```logistic_regression``` contains the scripts for performing the experiments with logistic regression
- ```gbdt``` contains the scripts for performing the experiments with different gradient boosting on decision trees libraries
- ```tabnet``` contains the scripts for performing the experiments with tabular deep learning model tabnet
- ```pareto``` contains the scripts to select pareto optimal SNPs

## Other files
- ```dbgap-data-preprocessing.docx``` contains the description of preprocessing dbGaP data used in the research.

## Hyperparameters
- Logistic Regression: {'C': 0.01, 'class_weight': 'balanced', 'fit_intercept': True, 'max_iter': 1000, 'penalty': 'l2', 'random_state': 42, 'solver': 'lbfgs'} 
- GBDT: {'importance_type': 'gain', 'learning_rate': 0.01, 'max_depth': 2, 'n_estimators': 100, 'scale_pos_weight': 0.13212540716612378}
- TabNet: {'n_a': 8, 'n_d': 8, 'lr': 0.02, 'n_steps': 3, 'cat_dims': [3]*cat_count, 'cat_emb_dim': [4]*cat_count, 'optimizer_fn': torch.optim.adam.Adam, 'batch_size': 256, 'epsilon': 1e-15, 'gamma': 1.3, 'momentum': 0.02}