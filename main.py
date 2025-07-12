import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')

df = pd.read_csv(r"C:\Users\ibrah\Documents\UK_Accident.csv")
print(df.head())

# info about each row, and column, not needed now
# df.info()

# to get the key features, and key stats
df.describe()
df.columns.tolist()
df.isnull().sum()
df.nunique()

# all avaialble columns
#print(df.columns.tolist())

# change the x and y axis here
year_counts = df['Year'].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(year_counts.index, year_counts, color='deeppink')
plt.title('Vehicles Against Casualties')
plt.xlabel('Number_Of_Casualties')
plt.ylabel('Number_Of_Vehicles')
plt.show()

# Swarm plot
"""
plt.figure(figsize=(10, 8))

sns.swarmplot(x="Year", y="Number_of_Casualties", data=df, palette='viridis')

plt.title('Swarm Plot for Casualties against Year')
plt.xlabel('Year')
plt.ylabel('Number_of_Casualties')
plt.show()


# bivariate analysis table or graph
sns.set_palette("Pastel1")

plt.figure(figsize=(10, 6))

sns.pairplot(df)

plt.suptitle('Pair Plot for DataFrame')
plt.show()
"""
# violin plots
plt.figure(figsize=(10, 8))
sns.violinplot(
    x="Year",
    y="Number_of_Casualties",
    data=df,
    alpha=0.7
)
plt.title('Violin Plot for Number of Casualties vs Year')
plt.xlabel('Year')
plt.ylabel('Number_of_Casualties')
plt.show()

# box plot
# Bin 'Accident_Severity' into broader categories (e.g., Low/Medium/High)
sns.boxplot(x='Day_of_Week', y='Number_of_Casualties', data=df)
plt.show()

# multivariate analysis with a correlation matrix plot
import seaborn as sns
import matplotlib.pyplot as plt

numeric_df = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(12, 8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="Pastel2",
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()