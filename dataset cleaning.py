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

#reading the dataset
df = pd.read_csv("Youtuber.csv")

#Removing the "M" from the Subscribers column, removing the first row, and turning the subscribers column from a object type to a float type.
df['Subscribers'] = df['Subscribers'].str[:-1]
df = df.iloc[1: , :]
df['Subscribers'] = df['Subscribers'].astype(float)
df

#Seeing how many NA values are in the Category column:
df["Category"].isna().sum()

#Turning all categories that are not available into an "Other" category.
df["Category"] = df["Category"].fillna("Other")
df

#Seeing how many NA values are in the Category column:
df["Category"].isna().sum()

#first few observations of the cleaned up data:
df.head()
df.dtypes