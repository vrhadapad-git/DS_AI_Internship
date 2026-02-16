#Task 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Housing.csv")
print(df.head())
sns.histplot(df['price'], kde=True)
plt.subplot(2,2,2)
sns.countplot(x='bedrooms',data=df)
df['price'].value_counts()
plt.show()


#Task 2
sns.scatterplot(x='price',y='area',data=df)
plt.subplot(2,2,2)
sns.boxplot(x='mainroad',y='parking',data=df)
plt.show()
print("/n as mainroad increases the parking increases")
print("/n as mainroad decreases the parking decreases")


#Task 3

corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
sns.boxplot(x=df['price'])
plt.show()

