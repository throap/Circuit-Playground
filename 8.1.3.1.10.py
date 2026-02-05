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
  print('Enter a number!')
  number_1 = int(input())
  print('Now eneter another number!')
  number_2 = int(input())
  first_challenge = challenge_2(number_1,number_2)
  print('The mutiplication of your two numbers is', first_challenge )
  second_challenge = challenge_3(number_1,number_2)
  print('the sum of these numbers is', second_challenge, '(if it was odd, then it was rounded up to the nearest even)')

main()
