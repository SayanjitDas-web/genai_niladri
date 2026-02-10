# class-1 (29/1/26)

# var = "hello"
# normalStr = "this is "  + var + " normal \\ \n string"
# rawStr = r"this is raw \\ \n string"
# formatStr = f"this is {2+2} format string."
# multilineStr = """ 
#   kdshgvb/dkgcycdh
#   dknvn/dvdvn               cb.adCVadhcjdc
#  """

# # print(normalStr)
# # print(rawStr)
# # print(formatStr)
# # print(multilineStr)

# def add(num1: int, num2: int):
#     """this is for addition"""
#     return int(num1)+int(num2)

# print(add(1,2))


# class-2 (3/2/26)

# condition = 1 > 2
# target = 10

# if(target > 2 and condition):
#     print("right")
# elif(target == 10 or condition):
#     print("equal")
# else:
#     print("wrong")

# print("right") if(condition) else (print("equal") if (target == 10) else print("wrong"))

# point = 80

# match(point):
#     case 50:
#         print("you got 50 points")
#     case 70:
#         print("you got 70 points")
#     case 90:
#         print("you got 90 points")
#     case _:
#         print("execeptional case")

# text = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Architecto voluptas iste harum iusto recusandae laudantium aperiam mollitia! Eius, quam perspiciatis?"

# # for char in text:
# #     print(word)

# for i in range(len(text)):
#     if i == 10:
#         break
#     print(text[i])

# i = 0 
# while(i < len(text)):
#     print(text[i])
#     i += 1

# class-3 (5/2/26)

# list , dictionary , tuple , set

# myList = ["one", 2 , 3, True, False]

# for data in myList:
#     print(data)

# for i in range(1,3):
#     print(myList[i])

# print(myList[::-1])

# for data in myList[:2]:
#     print(data)

# myDict = {"username":"Niladri","roll":1}

# print(myDict["username"])

# myDict["username"] = "Sayanjit"

# myDict.update({"age":20})

# del myDict["roll"]

# for [k,v] in myDict.items():
#     print(k,v)

# class-4 10/02/26

# myTuple = (1,2,"three",True)
# myTuple = myTuple + (False,"hello")
# print(myTuple)

# mySet1 = {1,2,3}
# mySet2 = {3,4,5}

# mySet1.update(("hello1","hello2","hello3"))
# mySet1.remove("hello1")
# mySet1.discard("hello2")
# mySet1.clear()
# print(mySet1)
# print(mySet1.intersection(mySet2))

# class MyClass:
#     def __init__(self):
#         print("constructor called ")

#     def __str__(self):
#         return "this is str constructor"
    
#     def sayHello(self, name):
#         print("hello , ", name)

# obj1 = MyClass()
# obj1.sayHello("Sayanjit")

# print(obj1)

# class A:
#     def __init__(self):
#         self.a = "this is a"

#     def show(self):
#         print(self.a)


# class B(A):
#     pass

# b = B()
# b.show()