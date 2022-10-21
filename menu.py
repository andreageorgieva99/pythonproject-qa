import sys
from datetime import datetime
inf_loop = True
inp_choise = 0
while (inf_loop):
    if inp_choise ==0:
        print( 'Menu:\n')
        print( "1)Today's date and time\n")
        print( '2)This month \n')
        print( "3)Today's day of the week:\n")
        print( '4)Quit\n')
        inp_choise =int(input('\nEnter a menu choice: '))
    if inp_choise == 1:
        current_dateTime = datetime.now()
        print("\nToday's date and time",current_dateTime)
        """
        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number: '))
        result= number1+number2
        print('Result : ',result)
        """
        inp_choise = int(input('\nEnter a menu choice: '))
    
    if inp_choise == 2:
        current_dateTime = datetime.now()

        print("\nThis month", current_dateTime.strftime("%B"))
        """
        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number: '))
        result= number1-number2
        print('Result : ',result)
        """
        inp_choise = int(input('\nEnter a menu choice: '))
    if inp_choise == 3:
        current_dateTime = datetime.now()
        print("\nToday's day of the week: ", current_dateTime.strftime("%A"))
        """
        number1 = int(input('Enter first number: '))
        number2 = int(input('Enter second number: '))
        result= number1*number2
        print('Result : ',result)
        """
        inp_choise = int(input('\nEnter a menu choice: ')) 
    if inp_choise == 4:
        print('\nThank you for using the date and time menu! :)\n')
        exit()