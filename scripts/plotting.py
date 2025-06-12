import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column, bins=50):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=bins, kde=True)
    plt.title(f'Distribution of {column}')
    plt.tight_layout()
    plt.savefig(f'reports/{column}_hist.png')
    plt.close()

def plot_boxplot(df, column):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot of {column}')
    plt.tight_layout()
    plt.savefig(f'reports/{column}_boxplot.png')
    plt.close()
