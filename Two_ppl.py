# TASK: Display True or False if the age entered by two users is the same.

user1 = int(input("Introduce la edad del primer usuario: \n"))
user2 = int(input("Introduce la edad del segundo usuario: \n"))

if user1 is user2:
    print("Tienen la misma edad.")
else:
    print("No tienen la misma edad.")
