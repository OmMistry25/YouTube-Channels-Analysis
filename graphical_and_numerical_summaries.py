import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns                  
sns.set()  
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.patches as mpatches
df = pd.read_csv("Youtuber.csv")
df['Subscribers'] = df['Subscribers'].str[:-1]
df = df.iloc[1: , :]
df['Subscribers'] = df['Subscribers'].astype(float)

#Seeing how many NA values are in the Category column:
df["Category"].isna().sum()

#Turning all categories that are not available into an "Other" category.
df["Category"] = df["Category"].fillna("Other")


#Seeing how many NA values are in the Category column:
df["Category"].isna().sum()

#first few observations of the cleaned up data:
df.head()
df.dtypes

#graphical summaries
ax = sns.boxplot(x='Category', y='Subscribers', data=df)
plt.xlabel("Category")
plt.ylabel('Number of Subscribers (in millions)')
categories = df['Category'].unique()
palette = sns.color_palette("husl", len(categories))
legend_handles = [mpatches.Patch(color=palette[i], label=f'{categories[i]}') for i in range(len(categories))]
plt.legend(handles=legend_handles, title='Categories', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
ax.set_xticks([])
plt.text(0.5, -0.1, "*Categories are listed corresponding to the legend above.",
         ha='center', va='center', transform=ax.transAxes, fontsize=11, color='black')
plt.title('Relationship between YouTube Channel Category and Subscriber Count')
plt.show()
ax

#numerical summaries
num_summary = df[['Category', 'Subscribers']].groupby('Category').describe()
num_summary