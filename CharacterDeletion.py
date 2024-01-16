string = input("Read an input string: ")
for i in range(2):
    string = string.replace(string[-2], "")
print(string[::-1])