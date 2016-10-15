print "Please enter your number between 0 and 100"
high = 100
low = 0
guessed = False
while not guessed:
    guess = (high + low)/2
    print "Is your guessed number is " + str(guess) + "?"
    user_inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if user_inp == 'c':
        guessed = True
        
    elif user_inp == 'h':
        high = guess
    elif user_inp == 'l':
        low = guess
    else:
        print "Sorry, I did not understand your input"
print "Game over. Your secret number was :" + str(guess)
