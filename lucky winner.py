print("\33[43m", "LUCKY CHANCE WINNER")
print("\33[44m", "PICK ONE OF OUR LUCKY NUMBER AND WIN A PRICE TODAY!!", "\33[0m")

import random
attempt = 3
myNumber1 = random.randint(1,1000)
for i in range(3):
  while True:
    myNumber1 = int(input("Pick a number between 1 to 1,000: "))
    if myNumber1 == 102:
      print("\33[32m", "todays lucky number is", myNumber1, "you won a piece of diamond")
    elif myNumber1 == 213:
      print("\33[33m", "todays lucky number is", myNumber1, "you won a 50kg bag of groceries")
    elif myNumber1 == 324:
      print("\33[34m", "todays lucky number is", myNumber1, "you won the ownership right to ‘Rhein II’ (photograph)")
    elif myNumber1 == 435:
      print("\33[35m", "todays lucky number is", myNumber1, "you won $2million")
    elif myNumber1 == 546:
      print("\33[36m", "todays lucky number is", myNumber1, "you won a golden cup of coffee")
    elif myNumber1 == 657:
      print("\33[37m","todays lucky number is", myNumber1, "you won 5 days trip to any country of your choice")
    elif myNumber1 == 768:
      print("\33[38m","todays lucky number is", myNumber1, "you won a 2024 Ferrari Daytona SP3")
    elif myNumber1 == 879:
      print("\33[39m","todays lucky number is", myNumber1, "you won a Bugatti Chiron")
    elif myNumber1 == 980:
      print("\33[40m","todays lucky number is", myNumber1, "you won the ownership rights to an apartment in Burj Khalifa")
    elif myNumber1 == 91:
      print("\33[30m","todays lucky number is", myNumber1, "you won a coupon to play 10times")
    elif myNumber1 > 1000:
      print("\33[31m","OUT OF RANGE. KINDLY PICK WITHIN THE RANGE", "\33[0m")
      attempt += 1
    else:
      print("\33[41m", "Try again you did not win", "\33[0m")
      print("\33[42m", "you are allowed to try only 3 times", "\33[0m")
      attempt += 3
      break