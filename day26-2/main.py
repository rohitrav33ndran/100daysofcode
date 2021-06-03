import random
#Dictionary Comprehension

#new_dict = {new_key:new_value for(key,value) in dict.items() if test}

# names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
#
# student_scores = {name:random.randint(30,90) for name in names}
#
# #print(student_scores)
#
# passed_students = {student:score for student,score in student_scores.items() if score > 50}
# print(passed_students)

# Challenge1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split(" ")}
# print(result)

#Challenge 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f =  {day:temp * 1.8 + 32 for day,temp in weather_c.items()}
#
# print(weather_f)
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
# for(key,value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)