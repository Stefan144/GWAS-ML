import os
import sys
import pandas as pd
from bioinfokit import visuz
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from config import gwas_results_path

if __name__ == "__main__":
    p_line = 1e-9
    gwas_results = pd.read_csv(gwas_results_path)
    markernames = dict(zip(gwas_results[gwas_results['p_val'] < p_line]['snp'], 
                           gwas_results[gwas_results['p_val'] < p_line]['snp']))
    visuz.marker.mhat(df=gwas_results, 
                      chr='chr',
                      pv='p_val',
                      show=False,
                      gwas_sign_line=True,
                      gwasp=p_line, 
                      dim=(16,6),
                      markernames=markernames, 
                      markeridcol='snp', 
                      gfont=12, 
                      gstyle=1, 
                      ar=45, 
                      axlabelfontsize=15, 
                      figtype="png")