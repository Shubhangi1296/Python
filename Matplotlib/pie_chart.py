import matplotlib.pyplot as plt

values = [40, 30, 20, 10]
labels = ["Python", "Java", "C++", "C"]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()