"""
src/hypothesis_tests.py
Reusable statistical testing functions for ACIS Marketing Analytics risk drivers.
"""

import numpy as np
import pandas as pd
from scipy import stats

def run_chi_square_test(df, group_col, target_col, group_a_val, group_b_val):
    """
    Runs a Chi-Squared test of independence for categorical variables (e.g., Claim Frequency).
    KPI is expected to be binary (1 for claim, 0 for no claim).
    """
    # Filter for the two specific groups being tested
    filtered_df = df[df[group_col].isin([group_a_val, group_b_val])].copy()
    
    # Create contingency table: Rows = Groups, Columns = Out-comes (0 or 1)
    contingency_table = pd.crosstab(filtered_df[group_col], filtered_df[target_col])
    
    # Run test
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    
    # Calculate frequencies for business interpretation
    freq_a = filtered_df[filtered_df[group_col] == group_a_val][target_col].mean()
    freq_b = filtered_df[filtered_df[group_col] == group_b_val][target_col].mean()
    
    return {
        "test_type": "Chi-Squared",
        "p_value": p_value,
        "stat": chi2,
        "group_a_mean": freq_a,
        "group_b_mean": freq_b
    }

def run_two_sample_t_test(df, group_col, target_col, group_a_val, group_b_val, conditional_filter=None):
    """
    Runs an independent two-sample t-test for numerical variables (e.g., Severity or Margin).
    """
    # Apply optional filters (like choosing only rows where a claim occurred for Severity)
    working_df = df.copy()
    if conditional_filter is not None:
        for col, val in conditional_filter.items():
            working_df = working_df[working_df[col] == val]
            
    # Extract arrays
    group_a_data = working_df[working_df[group_col] == group_a_val][target_col].dropna()
    group_b_data = working_df[working_df[group_col] == group_b_val][target_col].dropna()
    
    # Run Levene's test to check if variances are equal
    _, p_var = stats.levene(group_a_data, group_b_data)
    equal_var = p_var > 0.05  # If p < 0.05, variances are statistically unequal
    
    # Run T-Test (Welch's T-Test if variances are unequal)
    t_stat, p_value = stats.ttest_ind(group_a_data, group_b_data, equal_var=equal_var)
    
    return {
        "test_type": "Two-Sample T-Test",
        "p_value": p_value,
        "stat": t_stat,
        "group_a_mean": np.mean(group_a_data),
        "group_b_mean": np.mean(group_b_data)
    }