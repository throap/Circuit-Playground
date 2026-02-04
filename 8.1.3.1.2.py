print('Hello!')
Input = input("Who is the best in this class?")
type (Input)
name = max('Andy', 'Minh', 'Ethan', 'Dang')
if Input == 'Minh':
        print("yes,", name, "is the best in this class!")
        print(name, "is" ,len(name),'characters long!')
elif Input != 'Minh':
    for i in range (5):
        if Input != 'Minh':
            print('wrong, guess again!')
            Input = input()
        elif Input == 'Minh':
            print("yes, ", name, "is the best in this class!")
            print(name, "is" ,len(name),'characters long!')
            break 
    print ("actually, ", name, "is the best in this class!")
    print(name, "is" ,len(name),'characters long!')
number = abs(-100)
print (number)
