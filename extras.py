# 1
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# 2

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 3
# pi = 3.1415926535897931
# r= 6.0
# V= 4.0/3.0*pi* r**3
# print('The volume of the sphere is: ',V)


# 4

# def larger_string(str, n):
#   result = ""
#   for i in range(n):
#       result = result + str
#   return result

# print(larger_string('abc', 22))
# print(larger_string('.py', 3))


# 5
# from math import sqrt
# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))

# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is", c )

# 6

# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([1, 2, -8, 0]))


# 7

# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)

# 8
# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(0))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
# print('Dictionary in descending order by value : ',sorted_d)