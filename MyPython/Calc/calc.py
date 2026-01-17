#Go to GITHub
#Ver 1.0.0
#Ver 1.1.0
#2026.01.17

choice = input ("* - Multiplication, / - Division , + - Addition, - - Subtraction, ** - Exponentiation, % - Modulo:   ")

a = int(input ("First number: "))
b = int(input ("Second number: "))

if (choice == '*'):
    print (a * b)
    
elif (choice == '/'):
    
        if (b == 0):
            print ("Error , 0 not support")
            
        else:
            print (a / b)

        
elif (choice == '+'):
    print (a + b)

elif (choice == '-'):
    print (a - b)


elif (choice == '**'):
    print (a ** b)

elif (choice == '%'):
    print (a % b)

else:
    print ("Bad choice !")
