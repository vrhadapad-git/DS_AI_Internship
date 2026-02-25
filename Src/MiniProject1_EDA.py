import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("customer_analytics.csv")
print(df.head())
print(df.info())
print(df.describe())
print("The given dataset is about the customer data about there income and purchasing behavior \n")

#Phase 2
print(df.isnull().sum())
df = df.fillna(0)
print(df.isnull().sum())
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())
print("\nThe dataset doesnot contains any dupllicate dataset:")
print(df.head())

#Phase 3
plt.subplot(2,2,1)
plt.boxplot(df["Age"])
plt.title("Age Boxplot")
print("The box plot here represents range of age of customer, and in which age category they fall in, and we can see that most of the customer are of age 30 - 40 \n ")

plt.subplot(2,2,2)
x = df["AnnualIncome"]
plt.scatter(df["AnnualIncome"], df["LastPurchaseAmount"])
plt.title("Income vs Last Purchase")


plt.subplot(2,2,3)
plt.bar(df["Gender"],df["LastPurchaseAmount"])
plt.title("Gender vs Last Purchase")
print("Both the male and female customer has almost the same amount of there last purchase \n ")


plt.subplot(2,2,4)
plt.hist(df["AnnualIncome"])
plt.title("Annual Income Distribution")
print("Most of the customer annual income range to 1,00,000 \n")

plt.tight_layout()
plt.show()

#Phase 4
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

"""Executive Summary : The dataset is about the customer data about there income and purchasing behavior
the dataset is also designed to help with customer segregation based on there Age and annual income and the 
purchase"""
