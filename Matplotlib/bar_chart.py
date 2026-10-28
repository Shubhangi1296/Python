import matplotlib.pyplot as plt 

names = ["A", "B", "C", "D"]
marks = [80, 70, 90, 60]

plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show