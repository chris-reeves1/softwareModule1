# if, elif, else
# different pathways for our code to follow. 


#my_bool = False

#if my_bool:
#    print("mybool is true")
#else:
#    print("my_bool must be false!")


#if some condition:
#    if come other condtion:
#        code.....
#    else:
#        code ....
#else: 
#    code ....

#is_admin = True
#is_verified = False
#on_holiday = False

#if (is_admin or is_verified) and not on_holiday:
#    print("access granted")
#else:
#    print("access denied")

# == equal to
# > greeater than
# < less than
# >= greatre than or equals to
# <= less than orequals to
# != not equals to. 

#temp = 30

#if temp >= 30:
#    print("its hot")
#if temp > 25 and temp < 30:
#    print("pretty hot")
#if temp > 10 and temp < 25:
#    print("its ok")
#if temp == 0:
#    print("very cold")
#else:
#    print("anything below 10 degrees")

#elif == else if

#if temp >= 30:
#    print("its hot")
#elif temp > 25:
#    print("pretty hot")
#elif temp > 10:
#    print("its ok")
#elif temp == 0:
#    print("very cold")
#else:
#    print("anything below 10 degrees")

# exercise:

# user to input grade/mark
# if the mark is above 85 print distiction
# between 65 and 85 print pass
# anything else if fail. 
# use if elif else. 

#x = int(input("enter a grade: "))

#if x >= 85:
#    print("distiction")
#elif x >= 65:
#    print("pass")
#else:
#    print("fail")

# multiple comparators

#deposit = 199
#password = "password1"
 
#if 0 < deposit < 100 and password == "password10":
#    print(f"thankyou for deposit of {deposit}")
#else:
#    print("deposit failed")

# not

#if not 0 < deposit < 100 and password != "password":
#    print("deposit failed")
#else:
#    print("Thanks for deposit")

# in and not in

#name = "root123"

#if name in ("root", "admin", "user"):
#    print("invalid username")
#else:
    #print("accepted")

#if name not in ("root", "admin", "user"):
#    print("accepted")
#else:
#    print("invalid username")

# exercise
# weight converter
# user to input weight
# user to input kgs or lbs
# if stement to check for unit entered
# logic to convert the wight and print out the converted value. 
# error handling for upper/lowercase
# optional - error handling for input validation. 

# 1st solution

#weight = float(input("Enter weight: ")) 
#unit = input("Enter K (kgs) or L (lbs): ")

#if unit.upper() == "K":
#    converted = weight / 0.45
#    print(f"your converted weight is {converted}")
#elif unit.upper() == "L":
#    converted = weight * 0.45
 #   print(f"your converted weight is {converted}")
#else:
#    print("invalid choice - enter L or K !!!!!")


# 2nd solution 
#import sys

#while True:
  #  try:
  #      weight = float(input("Enter weight: "))
 #       break
 #   except ValueError: 
 #       print("invalid input, please enter a numeric value!!!")

#while True:
 #   unit = input("Enter K (kgs) or L (lbs): ").upper()
 #   if unit == "K":
 #       converted = weight / 0.45
 #       print(f"your converted weight is {converted}")
 #       break
 #   elif unit == "L":
#        converted = weight * 0.45
#        print(f"your converted weight is {converted}")
#        break
#    else:
#        print("invalid choice - enter L or K !!!!!")

#  highest number

#num = 10
#num1 = 20

#if num > num1:
#    print(num)
#else:
#    print(num1)

# Rewrite without using if statements, or any inbuilt function like max()!!

#result = num * (num > num1) + num1 * (num1 > num)
#print(result)