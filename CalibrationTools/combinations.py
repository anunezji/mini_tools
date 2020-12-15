#%% IMPORT PACKAGES

import numpy as np
import itertools as it

def count_unique_combinations_to_one(var_dict):
    """
    Determines the number of unique combinations that sum up to one
    """
    # Create list of unique combinations
    combos = list(it.product(*var_dict.values()))

    # Count how many combinations sum up to one
    count_uct1 = len([1 for combo in combos if np.sum(combo) == 1])

    return count_uct1

#%%
var_dict = {
        "w_econ": [0.1, 0.2, 0.3, 0.4],
        "w_swn": [0.1, 0.2, 0.3, 0.4],
        "w_att": [0.1, 0.2, 0.3, 0.4, 0.5],
        "w_subplot": [0, 0.1, 0.2, 0.3],}