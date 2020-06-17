import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
import pandas as pd
import itertools
from typing import List

def get_ref_light(ref_df: pd.DataFrame, psi_min: float = 10, psi_max: float = 80,
                  n_rows: int = 100) -> pd.DataFrame:
    """ Generate a lightweight reference, useful especially for plotting.

        Parameters
        ----------
        ref_df
            Reference dataframe including all the pre-generated data
        psi_min
            Minimum shooting angle psi to consider in reference dataframe
        psi_max
            Maximum shooting angle psi to consider in reference dataframe
        n_rows
            The number of evenspread rows to extract from the reference dataframe

        Returns
        -------
        ref_light_df
            A lightweight reference dataframe of n_rows
    """
    ref_minmax = ref_df.loc[(ref_df['true_angle']>=psi_min) & (ref_df['true_angle']<=psi_max)]
    ref_light_df = ref_minmax.iloc[::int(len(ref_minmax)/n_rows)] # take n_rows rows evenspread
    return ref_light_df

def get_datasets(ref_df: pd.DataFrame, n_datasets: int, sample_size: int = 10,
                 replace_across_datasets: bool = False, psi_min: float = 10, 
                 psi_max: float = 80) -> List[pd.DataFrame]:
    """ Generate datasets according to a dataframe of pre-generated data.

        Parameters
        ----------
        ref_df
            Reference dataframe including all the pre-generated data
        n_datasets
            Number of datasets to generate
        sample_size
            Number of observations in each dataset
        replace_across_datasets
            Perform sampling with replacement across datasets
            (within dataset sampling is done without replacement)
        psi_min
            Minimum shooting angle psi to consider in reference dataframe
        psi_max
            Maximum shooting angle psi to consider in reference dataframe

        Returns
        -------
        datasets
            A list of datasets. Each dataset is a dataframe.
    """
    # TO DO: add random state parameter
    ref_minmax = ref_df.loc[(ref_df['true_angle']>=psi_min) & (ref_df['true_angle']<=psi_max)]
    if replace_across_datasets:
        datasets = []
        for i_set in range(n_datasets):
            datasets.append(ref_minmax.sample(n=sample_size, replace=False))
    else:
        all_samples = ref_minmax.sample(n=n_datasets*sample_size, replace=False)
        datasets = np.split(all_samples, n_datasets)
    return datasets
