# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a1 = []
# a2 = []
# a3 = []
# for i in data:
#     a1.append(i[0])
#     a2.append(i[1])
#     a3.append(i[2])

# def avg(list_atr):
#     # return sum(list_atr)/len(list_atr)
#     total = 0
#     for i in list_atr:
#         total += i
#     return total / len(list_atr)

# print(f"The average of firsts: {avg(a1)}")
# print(f"The average of seconds: {avg(a2)}")
# print(f"The average of thirds: {avg(a3)}")

# def fun1():
#     return 1

# l1 = [[fun1(), 123], ["Temp", "Humidity"]]
# print(l1[1][1])
# for i in l1:
#     print(i)

#Slicing

# l2 = [1, 2, 3, 4, 5]
# print(l2[0:5]) #start, stop, step
# print(l2[4::-1])

# #string is immutable demonstration

# c = "Hello"                                                    
# print(c)
# print(id(c))                                   
# print(hex(id(c)))                 
# d = c.replace("e", "i")                                    
# print(d)

# a = [1, 2, 3]
# b = [4, 5, 6]

# x = a.append(b)
# print(x)

a = 5
print(type(a))
print(type(type))