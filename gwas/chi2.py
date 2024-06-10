import os
import sys
import pandas as pd
import numpy as np
from tqdm import tqdm
from scipy.stats import chi2_contingency
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from config import features_names_path, features_path, targets_path,\
                   snp_to_chr_path, gwas_results_path

def perform_gwas(features, phenotypes, features_names, name_to_chr):
    data = []
    for i in tqdm(range(features.shape[1])):
        snp = features[:, i]
        pval = chi2_contingency(pd.crosstab(snp, phenotypes))[1]
        snp_name = features_names[i]
        data.append((snp_name, pval, name_to_chr[snp_name]))
    df = pd.DataFrame(data, columns=["snp", "p_val", "chr"])
    df.to_csv(gwas_results_path, index=False)

if __name__ == "__main__":
    features = np.load(features_path)
    features_names = np.load(features_names_path, allow_pickle=True)
    phenotypes = np.array(np.load(targets_path, allow_pickle=True)) - 1 # (1, 2) -> (0, 1)
    name_to_chr = np.load(snp_to_chr_path, allow_pickle=True).item()
    perform_gwas(features, phenotypes, features_names, name_to_chr)