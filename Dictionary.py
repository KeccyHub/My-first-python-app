# you can name your dictionary anything, this dictionary is stored as an object
# my_dict = {
#     "Ikotun": 200,
#     "Iyana Ipaja": 300, 
#     "Ishheri": 100
#     }
# {"key":"value"}
# # to add key to the dictionary,
# my_dict["Egbeda"]=500
# print(my_dict)
# print(my_dict["Ikotun"])
# for x in my_dict:
#     print([x])

# to delete a key, use
# del my_dict["Ikotun"]
# my_dict.pop("Ikotun") 
# print(my_dict)
# print("Iyana Ipaja", my_dict["Iyana Ipaja"], "Isheri", my_dict["Ishheri"])
# for key in my_dict:
#     print(f"We have {key}, {my_dict[key]}")
#     for lock in my_dict:
#         print(f"We have {lock} in my {my_dict}")

# for key, value in my_dict.items():
#     print(key, value)
# squares={number:number*number for number in range (-1,7)}
# for x in squares:
#     print(x, squares)
# print(squares)

a=1
b=2
c=3
squares={number:number*number for number in range (a,b,c)}
print(squares)