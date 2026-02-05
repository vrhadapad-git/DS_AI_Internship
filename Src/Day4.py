contact = {"X": 1234, "A": 3456, "B": 6789}
contact["ZZZ"] = 5468
for name, number in contact.items():
    print(name, number)
print(contact.get("X"))


raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print(type(unique_users))
print(unique_users)
print("ID05" in unique_users)
print("sfd" in unique_users)
print(len(unique_users))


friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(friend_a | friend_b)
print(friend_a & friend_b)
print(friend_a-friend_b)

