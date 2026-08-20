with open("demo.txt", "r") as file:
    lines = file.readlines()

tail = lines[-3:]

print("Last 3 lines:")
for line in tail:
    print(line.strip())