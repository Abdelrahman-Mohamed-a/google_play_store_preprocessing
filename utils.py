import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_hist(df,column):
    plt.figure(figsize=(8,5))
    plt.hist(df[column], bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()