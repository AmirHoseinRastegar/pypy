def hint_maker(user_guess, actual_number):
    if user_guess < actual_number:
        print('number is higher')
    else:
        print('number is lower')