import pandas


def add_claim_flags(df):
    df = df.copy()
    df['HasClaim'] = df['TotalClaims'] > 0
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df

def compute_group_metrics(df, group_col):
    grouped = df.groupby(group_col).agg({
        'HasClaim': 'mean',          # Claim Frequency
        'TotalClaims': lambda x: x[x > 0].mean(),  # Claim Severity
        'Margin': 'mean'
    }).rename(columns={'HasClaim': 'ClaimFrequency', 'TotalClaims': 'ClaimSeverity'})
    return grouped.sort_values(by='ClaimFrequency', ascending=False)
