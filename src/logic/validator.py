def validator(start,end):
    while True:
        user_input = input(f'please enter a number between {start} and {end}: ')
        
        if user_input.lower()=='q':
            print('Have a nice Day')
            break
        
        try:
            user_input= int(user_input)
            if user_input > end or user_input < start:
                print('Invalid input number. it must be in range')
            else :
                return user_input
        except ValueError:
            print('invalid input format please enter a number')