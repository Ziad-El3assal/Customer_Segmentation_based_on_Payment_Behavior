import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_corr(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_dist(df):
    plt.figure(figsize=(10, 8))
    sns.distplot(df['Annual Income (k$)'], bins=20, color='blue')
    plt.title('Annual Income Distribution')
    plt.show()
    
def plot_count(df):
    plt.figure(figsize=(10, 8))
    sns.countplot(df)
    plt.title("Count Plot")
    
def plot_box(df):
    plt.figure(figsize=(10, 8))
    sns.boxplot(df['Spending Score (1-100)'], color='red')
    plt.title('Spending Score Distribution')
    plt.show()
    
def plot_scatter(df):
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=df)
    plt.title('Annual Income vs Spending Score')
    plt.show()
    
def plot_pair(df):
    plt.figure(figsize=(10, 8))
    sns.pairplot(df)
    plt.title('Pair Plot')
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('CC GENERAL.csv')
    plot_corr(df)
    plot_dist(df)
    