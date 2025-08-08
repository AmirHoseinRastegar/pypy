from utils.numb_generator import make_rand
from logic.hint_maker import hint_maker
from logic.validator import validator
from logic.score_calculator import Score_calculator

def main():
    number_to_guess= make_rand(1,100)
    score= Score_calculator()
    
    
    while True:
        geuss= validator(1,100)
        if geuss == number_to_guess:
            
           print('yes you nailed it')
           score_amount=score.show_score()
           print(f"your score is {score_amount}")
           break
        else:
            hint=hint_maker(geuss,number_to_guess)
            print(hint)
            score.decrement_score()
            
if __name__== '__main__':
    main()
        
         