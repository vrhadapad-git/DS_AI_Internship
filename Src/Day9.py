#Task 1 Pandas Series 
import pandas as pd
products =pd.Series([700, 150, 300],index=['Laptop', 'Mouse', 'Keyboard'])
print([products])
print(products['Laptop'])
print(products[['Keyboard','Laptop']])


#Task 2 boolean masking
students=pd.Series([85, None, 92, 45, None, 78, 55])
print(students.isnull())
print(students.fillna(0))
scores=students[students>60]
print(students)
print(scores)


#Task 3
usernames =pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(usernames.str.strip())
lower_cased=(usernames.str.lower())
print(lower_cased)
print(lower_cased.str.contains('a'))
print(usernames)