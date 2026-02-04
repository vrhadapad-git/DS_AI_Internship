name = input("Enter your name:")
age = int(input("Enter your current age:"))
age_in_2030 = age + 4
print(f"\n hey{name},you will be {age_in_2030},years old in 2030")


# Bill splitter
Total_bill = float(input("\n enter your bill:"))
number_of_people = int(input("no of people:"))
Share_per_Person = (Total_bill/number_of_people)
print("\n",Share_per_Person)

# Understanding Data Types and String Formatting.
item_name = ("\n Laptop")
quantity = 2
price = 499.99
n_stock = True
print(f" item {item_name},  Qty {quantity},  Price {print},  Available {n_stock}")
