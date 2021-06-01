# file = open("new_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#With doesn't require a manual close methods.
# with open("new_file.txt") as file:
#     contents = file.read()
#     print(contents)


# Write to the file
with open("new_file.txt", mode="w") as file:
    file.write("What's happening")