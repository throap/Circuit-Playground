while True:
    try:
      print("enter an integer that is 20 or > 20")
      user_input = int(input())
      if user_input >= 20:
        print("Your number 20 is a valid Integer 20 or greater")
        break
      
      else:
        print("number is not an integer that is 20 or > 20")

    except ValueError:
      print("Invalid input, please enter an ingteger")

print("Starting While Loop - Print Count Variable")
times_looped = 0

while user_input > 1:
    user_input = user_input / 2
    print("The current value of the user input after some math is,", user_input)
    times_looped += 1
    print("The while loop has looped", times_looped, "time/s")

print("The While Loop, looped a total of", times_looped, "times")
