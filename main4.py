import random
def play_game():
    optios=['gheychi','khaghaz','sang']

    user_choice=input("(gheychi,khaghaz,sang)entekhab kon:").lower()
    computer_choice=random.choice(optios).lower()
    print(f'raiane entekhab kard:{computer_choice}')
    if user_choice==computer_choice:
        result='mosavi'
    elif(user_choice=="sang"and computer_choice=="gheychi")or\
        (user_choice=="khaghaz"and computer_choice=="sang")or\
        (user_choice=="gheychi"and computer_choice=="khaghaz"):
        result='shoma bordid'
    else:
        result='rayane bord'
    print(result)
play_game()    