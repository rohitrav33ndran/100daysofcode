
#List comprehension
# numbers = [1, 2, 3]
# doubled_num = [num * 2 for num in numbers]
#
# #conditional list compression
#
# names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
#
# short_name_list = [name for name in names if len(name) <= 4 ]

# print(new_list)
#
# long_name_list = [name.upper() for name in names if len(name) > 5 ]
# print(long_name_list)

#Challenge 1 - Squared numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# # squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

#Challenge 2 - even numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num%2 == 0]
# print(result)

#Challenge 3 - compare 2 files file1.txt and file2.txt and save the common numbers in list

with open("file1.txt",mode="r") as file1:
    file1_list = file1.readlines()
with open("file2.txt", mode="r") as file2:
    file2_list = file2.readlines()

result = [int(n) for n in file1_list if n in file2_list]

print(result)


print()



