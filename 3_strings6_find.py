# Finding a substring using the find method:
# Note that this only finds the FIRST instance
myString = "Hello, my name is Paul!"

result = myString.find("name")

print(result)

# If the substring is not present, find will return -1
print(myString.find("how"))