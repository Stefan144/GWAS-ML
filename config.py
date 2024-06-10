# paths
features_path = "../stroke_data/features"
features_names_path = "../stroke_data/features_names"
features_p_values_path = "../stroke_data/features_p_values.npy"
targets_path = "../stroke_data/targets"
snp_to_chr_path = "../stroke_data/snp_chr"
gwas_results_path = "../stroke_data/gwas_results.csv"
data_path = "../stroke_data/"

# constants
RANDOM_STATE = 42
N_SPLITS = 5

# helper functions
def hello(): print("hello")

'''
data = np.load('../all_chromosomes.npy')
snp_list = np.load('../combined_SNP', allow_pickle=True)
target = np.array(np.load('../target', allow_pickle=True)) - 1 # VERY IMPORTANT
p_values = np.load('../p_values_full.npy')
'''