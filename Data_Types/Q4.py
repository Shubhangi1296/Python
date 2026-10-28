project1 = {"Amit", "Rahul", "Sneha", "Priya"}
project2 = {"Sneha", "Priya", "Rohan", "Neha"}

print("Employees in both projects:", project1 & project2)

print("Employees only in Project 1:", project1 - project2)

print("Employees only in Project 2:", project2 - project1)

print("All unique employees:", project1 | project2)