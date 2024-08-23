import random
import hangman_wordlist 
import hangman_art
word = hangman_wordlist.word_list
stages_0= hangman_art.stages
logo_main = hangman_art.logo
print(logo_main)
print("welcome to hangman world !")
random_word = random.choice(word)
place_holder = ""
for position in range(len(random_word)):
    place_holder += "_"
lives = 6
list_new = []
game_over = False
while not game_over :
    print(f"you have {lives}/6 lives left !")
    user_guess = input("Guess a letter : ").lower()
    if user_guess in list_new:
        print(f"you have already choose {user_guess}")
    display = ""
    for char in random_word:
        if user_guess == char :
            display = display + char
            list_new.append(char)
        elif char in list_new:
            display +=char
            
        else :
            display = display + "_"
            
    print(display)
    if user_guess not in random_word:
        lives -= 1
        print(f"you entered {user_guess} that is not present in word")
        if lives==0:
            game_over = True
            print(f"**********  YOU LOST THE GAME... THE GUESS WORD WAS {random_word} *************")
    print(stages_0[lives])
            
            
    if "_" not in display:
        game_over = True
        print("************* CONGRATS! YOU WON THE GAME ******************")

        
