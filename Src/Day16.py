#Task 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("distribution_dataset.csv")
df = pd.DataFrame(data)
print(df)
print(df.head())
plt.subplot(1,3,1)
sns.histplot(data["Height_cm"], kde=True)
plt.subplot(1,3,2)

sns.histplot(data["Household_Income"], kde=True)
plt.subplot(1,3,3)
sns.histplot(data["Exam_Score"], kde=True)
plt.show()
print(data["Exam_Score"].mean())
print(data["Exam_Score"].median())
print("Mean = Median it's symmetric")




#Task 2
mean = (data["Exam_Score"].mean())
std =(data["Exam_Score"].std())
data["z_score"] = (data["Exam_Score"] - mean) / std
print(data["z_score"])
print(data)
if (data["z_score"] > 3).any():
    print("All z_scores are more than 3")
else:
    print("z_scores are not more than 3")




#Task 3
means = []

for _ in range(1000):
    sample = np.random.choice(data["Exam_Score"], size=30)
    means.append(sample.mean())

sns.histplot(means, bins=30, kde=True)
plt.title("Distribution of Sample Means")
plt.show()