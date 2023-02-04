from random import shuffle

def shuffle_list(mylist):    #function which defines the shuffle list
    shuffle(mylist)
    return mylist

def user_input():           #function of taking the input from the user
    
    guess = ''
    while guess not in ['1','2','3']:
        guess = input("\nGuess the position of 'O' press 1 or 2 or 3 for the position you choose: ")
        if guess not in ['1','2','3']:
            print("wrong choice!!!!!!")
            print("Enter selective position either 1,2 or three.....")
        else:
            print("Thank you!!!")
            return int(guess)

def check(mylist):        #function of checking whether you won the game or not

    user_in = user_input()
    if mylist[user_in-1] == 'O':
        print("\nYou won the game!!!!!")
    else:
        print("\nBetter luck next time.....")
        print("\n The list is as follows\n")
        print(mylist)

mylist = [' ',' ','O']     #start the game
ans = True
print("\t\t\t !!!!!!Welcome to the guessing game!!!!!")
while ans:
    x = input("\nDo you want to play the game (yes/no)? ")
    if x in ['yes','YES','Y','y']:
        ans = True
    else:
        ans = False
    
    if ans:
        shuffle_list(mylist)
        check(mylist)