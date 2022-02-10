#1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())
#prediction: Console will print 5

#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#predicted an error due to a function being called that has not been defined

#3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())
#Console wil print: 5 10... Console only printed 5, vscode says line 16 is "unreachable"

#4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())
#Console will print: 5 10... Console only printed 5, vscode says line 23 is "unreachable", likely due to return usually being used to end a block of code. 
#print would have to be outside the function likely as line 25 to print that integer, or a conditional would have to be added to include in code block. 


#5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)
#Prediction: Console will print 5 and none.... Correct

#6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
#Prediction: Console will print 5... Python instead produces an TypeError: Unsopprted operand type(s) nonetype and nonetype, perhaps values need to be set to
#to integers to work properly. 

#7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))
#Prediction: Console will print 25... Correct

#8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())
#Prediction: Console will print 100 then 10 then 7... Likely did not print 7 due to code block ending at return when function was called. 

#9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Prediction: Console will print 7 then 14 then 14... for line 70, values that the print function will add are 7 and 14, will condsider boolean first for time function
#was called on line 70.

#10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))
#Prediction: Console will print 8... Correct

#11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)
#Prediction: console will print 500 then 500 then 300 then 300.... Console printed
# 500 then 500 then 300 then 500. Likely the defined function has to be called to 
#get console to set b to 300 and print 300, otherwise it will print the preset value
#of 500.

#12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)
#Prediction: Console will print 500 then 500 then 300 then 300... Console still printed
#the same as #11. 500 then 500 then 300 then 500


#13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)
#Prediction: Console will print 500 then 500 then 300 then 300.... Correct (finanlly ^.^'') 

#14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
#Prediction: Console will print 1 then 3 then ... Correct! 


#15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)
#Prediction: console will print 1 then 3 then 2