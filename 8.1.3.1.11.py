def challenge_2(x,y):
  z=x*y
  return z

def challenge_3(x,y):
  z=x+y
  if z % 2 == 1:
    z+=1
    return z
  else:
    return z

def main():
  x=True
  while x:
    try:
      num_1 = int(input("Enter a number: "))
      num_2 = int(input('Now enter another number: '))

      first_challenge = challenge_2(num_1,num_2)
      print('The mutiplication of your two numbers is', first_challenge )
      second_challenge = challenge_3(num_1,num_2)
      print('the sum of these numbers is', second_challenge, '(if it was odd, then it was rounded up to the nearest even)')
      return False
    
    except ValueError:
      print("Invalid input, please enter an integer")
  
main()
