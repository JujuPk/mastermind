import random
user_list=[]
def create_comp_list():
    while len(user_list)<4:
        random_num=random.randint(1,7)
        if random_num not in user_list:
            user_list.append(random_num)
    return user_list
def get_guess():
    while True:
        try:
            guesses_left=10
            user_input=input("pick 4 numbers withing range 1-7:")
            user_list=[]
            for item in user_input:
                user_list.append(int(item))
            illegal_numb=False
            illegal_numb2=False
            illegal_length=False
            for number in user_list:

                if number > 7 or number < 1:
                    illegal_numb=True
                if user_list.count(number) > 1:
                    illegal_numb2=True
            if len(user_list) != 4:
                illegal_length=True
            if illegal_numb:
                print "it should be within 1-7"
            if illegal_numb2:
                print "it should have unique numbers"
            if illegal_length:
                print "should be length of 4"
            if not illegal_numb and not illegal_numb2 and not illegal_length:
                return user_list

        except ValueError:
            print "Only Enter Numbers"
print get_guess()
def check_values(num_array,guesses):
    response=[]
    for numb in num_array:
        if numb in guesses:
            if num_array.index(numb)==guesses.index(numb):
                response.append("red")
            else:
                response.append("white")
        else:
            response.append("black")
    random.shuffle(response)
    print response
    return (check_win(response))
def check_win(response_list):
    win=0
#checks for each item, if its red and = 4 you win.
#by using a for loop to check each item in the list.
#if the item is red and win is 4 you win.
    for item in response_list:
        if item == "red":
            win=win+1
    if win==4:
        print "you win"
    else:
        print "you lose"
def play_game():
    game_list=create_comp_list()
    total_guesses= 0
    while total_guesses < 10:
        print "guesses left" +str(10-total_guesses)
        user_input=get_guess()
        if check_vaules(game_list,user_input)==4:
            break
        total_guesses=total_guesses + 1
        if total_guesses==-10:
            print"thats all the guesses used"
            print"that is correct"
            print game_list
        print "thanks for playing"
play_game()
# Print directions telling the user how to play the game. Then call the
# play_game function to begin the game, using all of your prewritten functions.
