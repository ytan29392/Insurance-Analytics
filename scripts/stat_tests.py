from scipy.stats import ttest_ind, f_oneway
from statsmodels.stats.proportion import proportions_ztest

def t_test_numeric(df, group_col, value_col, group1, group2):
    g1 = df[df[group_col] == group1][value_col].dropna()
    g2 = df[df[group_col] == group2][value_col].dropna()
    stat, p = ttest_ind(g1, g2, equal_var=False)
    return stat, p

def anova_numeric(df, group_col, value_col):
    groups = [df[df[group_col] == g][value_col].dropna() for g in df[group_col].unique()]
    stat, p = f_oneway(*groups)
    return stat, p

def z_test_proportions(df, group_col, group1, group2, flag_col='HasClaim'):
    count1 = df[df[group_col] == group1][flag_col].sum()
    nobs1 = len(df[df[group_col] == group1])
    count2 = df[df[group_col] == group2][flag_col].sum()
    nobs2 = len(df[df[group_col] == group2])
    stat, p = proportions_ztest([count1, count2], [nobs1, nobs2])
    return stat, p
