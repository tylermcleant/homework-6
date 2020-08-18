#Calling the 'random property to enable to system to randomly choose a number between one and ten. 
import random
number = random.randint(1, 10)
#Asking the user to input a name so the system can identify user. Also the counter is set to 'zero' to characterize the guesses allowed.  
player_name = input("Hello, What's your name?")
number_of_guesses = 0
#System will output/display the users name and querying the user to enter a number between one and ten. 
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

#Loop is being wrapped in 'if' statements for the system to check the counter does not exceed five attempts/guesses. 
while number_of_guesses < 5:
    #This is setting up the variable 'guess' as an integer that will be input by the user/guesser
    guess = int(input())
    #Sets up the variable to represent the number of guesses it took for the user to correctly solve the secret number
    number_of_guesses += 1
    #System will notify user if the guess is too high or low from the number randomly selected by system. There is also a 'break' failsafe to resume the next lines of code to print message.
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))