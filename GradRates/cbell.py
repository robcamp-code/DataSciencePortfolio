import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def merge_into_mini(dframe, list_of_cols, final_col_name):
    df_list = []
    for i in list_of_cols:
        df_1 = pd.DataFrame(dframe.copy(deep=True)[i])
        df_1.reset_index(inplace=True)
        df_1.dropna(inplace=True)
        df_1.columns = ["UnitID", final_col_name]
        df_list.append(df_1)
    df_final = pd.concat(df_list)
    return df_final

def bs_sample(arr):
    return np.random.choice(arr, size=len(arr))

def bs_replicate(arr, func, n):
    replicates_list = []

    for i in range(n):
        sample = bs_sample(arr)
        replicate = func(sample)
        replicates_list.append(replicate)

    return replicates_list

def permutation_sample(arr1, arr2):
    size = len(arr1)

    data = np.concatenate((arr1, arr2))

    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:size]
    perm_sample_2 = permuted_data[size:]

    return perm_sample_1, perm_sample_2

#plot n ecdfs of the data if they were being drawn from the same distribution,
#then plot the actual ecdfs of the raw data
def plot_permutations(arr1, arr2, n, label1="arr 1", label2="arr 2", ax=plt.gca()):

    for i in range(n):
        perm_1, perm_2 = permutation_sample(arr1, arr2)
        _ = sns.ecdfplot(x=perm_1, color="gray", alpha=0.7, ax=ax)
        _ = sns.ecdfplot(x=perm_2, color="gray", alpha=0.7, ax=ax)

    _ = sns.ecdfplot(x=arr1, label=label1, ax=ax)
    _ = sns.ecdfplot(x=arr2, label = label2, ax=ax)

def diff_of_means(data_1, data_2):
    return data_1.mean() - data_2.mean()

def diff_of_std(data1, data_2):
    return data_1.std() - data_2.std()

def sample_replicate(arr1, arr2, func, n):
    replicate_samples = np.empty(n)

    for i in range(n):
        perm1, perm2 = permutation_sample(arr1, arr2)

        replicate = func(perm1, perm2)
        replicate_samples[i] = replicate
    return replicate_samples

def get_p(replicate_array, empiricle_value, tailed2):
    if tailed2:
        return 2 * np.sum(replicate_array >= empiricle_value) / len(replicate_array)
    return np.sum(replicate_array >= empiricle_value) / len(replicate_array)

def ecdf(arr):
    n = len(arr)
    x = np.sort(arr)
    y = (np.arange(1, n + 1)) / n
    return x, y