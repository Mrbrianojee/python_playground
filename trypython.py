# 2
# print('Hello World')
# print('Welcome To Python')


name  = raw_input("What is your name?")

print("Hello {0}").format(name)

print(name.lower())

print(name[0].upper() + name[1: len(name)].lower() )

print(name[1:4])

# my_list = [1,2,3,4,5,6]
# print(sum(my_list))

# count =  0
# for i in my_list:
#     count += i
# print(count)

# my_list = []
# for item in range(100):
#     my_list.append(item)

# print(my_list)


# my_list = []
# for item in range(0,100,2):
#     my_list.append(item)

# print(my_list)

# or

# my_list = []
# for item in range(100):
#     if item % 2 == 0:
#         my_list.append(item)

# print(my_list)


# my_mad_list = [[0], [0, 1], [0, 1, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]

# # print(my_mad_list)

# print(my_mad_list[4][2])

# evens = []
# for i in range(1,11):
#     if i%2==0:
#         evens.append(i)

# print(evens)




# student1 = {'name':'Wouter', 'age': 6, 'nationality':'Dutch' }
# student1 = {'name':'Wouter', 'age': 6, 'nationality':'Dutch' }
# student2 = {'name':'Tom', 'age': 23, 'nationality':'Irish' }
# student3 = {'name':'Terry', 'age': 34, 'nationality':'English' }
# student4 = {'name':'Tony', 'age': 78, 'nationality':'Italian' }

# my_students = []

# my_students.append(student1)
# my_students.append(student2)
# my_students.append(student3)
# my_students.append(student4)

# # print(my_students)

# my_student_dict = {}
# for student in my_students:
#   my_student_dict[student['name']] = student 

# # print(my_student_dict["Tony"])

# print(my_student_dict)



musician1 = {'name':'Tom', 'nationality': 'Irish', 'gender':'f'}

musician1_instrument1 = {'lute': 22}
musician1_instrument2 = {'flute': 87}
musician1_instrument3 = {'boot': 99}

musician1_instruments = []

musician1_instruments.append(musician1_instrument1)
musician1_instruments.append(musician1_instrument2)
musician1_instruments.append(musician1_instrument3)

musician1_bands =[]
musician1_bands.append("Radiohead")
musician1_bands.append("Wyvern Lyngo")
musician1_bands.append("First Aid Kit")

musician1['instruments'] = musician1_instruments
musician1['bands'] =  musician1_bands

musician_list =[]

musician_list.append(musician1)


my_muso_dict = {}
for muso in musician_list:
    my_muso_dict[muso['name']] = muso


print(my_muso_dict['Tom']['instruments'][0]['lute'])
        







# s = "Hello"
# str = ""
# for i in s:
#     str = i + str
# print(str)





    