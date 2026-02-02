while True:
    try:
      print("enter an integer from 0 to 9")
      user_num = int(input())
      if 0 <= user_num <= 9:
          break
      else:
            print("number must be between 0 and 9.")

    except ValueError:
      print("Invalid input, please enter an ingteger")

count = 0
print("Starting While Loop - Comparing User & Count Variable")

while count <= 9:
    print(count)
    count += 1
    if user_num == count:
        print("The User variable is equal to the count variable.")
        print("Count =", count)
        print("user_num =", user_num)
        continue
