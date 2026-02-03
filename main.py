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

condition = 1 > 2
target = 10

if(target > 2 and condition):
    print("right")
elif(target == 10 or condition):
    print("equal")
else:
    print("wrong")

print("right") if(condition) else (print("equal") if (target == 10) else print("wrong"))

point = 80

match(point):
    case 50:
        print("you got 50 points")
    case 70:
        print("you got 70 points")
    case 90:
        print("you got 90 points")
    case _:
        print("execeptional case")

text = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Architecto voluptas iste harum iusto recusandae laudantium aperiam mollitia! Eius, quam perspiciatis?"

# for char in text:
#     print(word)

for i in range(len(text)):
    if i == 10:
        break
    print(text[i])

# i = 0 
# while(i < len(text)):
#     print(text[i])
#     i += 1