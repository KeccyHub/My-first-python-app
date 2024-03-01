# how_much_do_you_weigh = input('How much do you weigh? ')
# print(type(how_much_do_you_weigh))
# weight = 0.454 * int(how_much_do_you_weigh)
# print(type(weight))
# print(weight)
# weight_lbs = input('Your weight? ')
# weight_kg = int(weight_lbs) * 0.454
# print(weight_kg)
# weight_kg = input('weight? ')
# weight_lbs = int(weight_kg) * 2.205 + "kg"
# print(weight_lbs)

# how_much_do_you_weigh = int(input('Weight: '))
# lbs_or_kg=str(input("Lbs or Kg:")).lower()
# if lbs_or_kg=="lbs":
#     print(f"{how_much_do_you_weigh / 0.454}lbs")
# elif lbs_or_kg=="kg":
#     print(f"{how_much_do_you_weigh*0.454}kg")
# else:
#     print("Invalid Command")

import sys
# import random as r
# list=[0,1,2,3,4,5,6,7,8,9]
# r.shuffle(list)
# print(list)

# for x in list:
#     for y in list:
#         result=x-y
#         print(result)
max_booking=20
initial_booking=0
num_booking=int(input("Enter the number of booking\n>> "))
if num_booking>max_booking:
    print("Number of booking exceeds the maximum limit.\n>>")
    num_booking=max_booking
    sys.exit()

while initial_booking<=num_booking:
    predicts=str(input("Enter Home and Away teams Score\n>> "))
    if predicts==result:
        print(result)
        print(predicts)
        print("You Win!")
        break
else:
    print("You loose")