import random

class Wordle:
    def __init__(self):
        self.id = 1
        self.answer_dict = {}
        self.id_dict = {}
        self.user_id = 1
        self.user_dict = {}

    def get_users(self):
        self.user_id = 1
        file_object = open("users.txt", "r")
        for user in file_object:
            self.user_dict[user.strip()] = self.user_id
            self.user_id += 1
        file_object.close()
        return self.user_dict

    def add_user(self, user):
        try:
            self.user_dict[user] 
            print("User already exists!")
            return 0
        except KeyError:
            file_object = open("users.txt", "a")
            file_object.write(user.lower() + "\n")
            file_object.close()
            return 1
           
    def get_answers(self, text):
        self.answer_dict = {}
        self.id_dict = {}
        self.id = 1
        file_object = open(text, "r")
        for word in file_object:
            self.answer_dict[self.id] = word.strip()
            self.id_dict[word.strip()] = self.id
            self.id += 1
        file_object.close()
        
    def add_answer(self):
        text, word_len = self.prompt_word_len()
        word = input(f"\nEnter a {word_len} letter word to add to the word bank: ")
        try:
            self.get_answers(text)
            self.id_dict[word]
            print("Word is already in the word bank")
        except KeyError:
            if len(word) == word_len:
                file_object = open(text, "a")
                file_object.write(word.lower() + "\n")
                file_object.close()
                print(f"{word} has been added to the bank!")
            else:
                print(f"Word has to be {word_len} characters")

    def remove_answer(self):
        found = False
        text, word_len = self.prompt_word_len()
        word = input(f"\nEnter a {word_len} letter word to remove from the word bank: ")
        self.get_answers(text)
        open(text, "w")
        for answer in self.answer_dict.values():
            if answer == word:
                found = True
            else:
                file_object = open(text, "a")
                file_object.write(answer.lower() + "\n")
                file_object.close()
        if found:
            print(f"{word} was removed from the {word_len} letter word bank!")
        else:
            print(f"{word} was not in {word_len} letter word bank!")
    
    def random_word(self):
        '''Generates a random word from the word bank'''
        word_id = random.randint(1, self.id - 1)
        word = self.answer_dict[word_id]
        if word == "":
            self.random_word()
        return word

    def guess_word(self, word, guess):
        '''Compares answer to the user guess and returns feedback'''
        feedback_str = ""
        i = 0
        word = list(word)
        guess = list(guess)
        for letter in guess:
            letter = letter.lower()
            if letter == word[i]:
                feedback_str += "C"
            elif letter in word:
                feedback_str += "c"
            else:
                feedback_str += "-"
            i += 1
        return feedback_str
    
    def check_win(self, feedback_str, word_len):
        '''Checks win by comparing user feedback to win string, returns True if there is a win'''
        win_str = "C" * word_len
        if feedback_str == win_str:
            return True
    
    def valid(self, guess, word_len):
        '''Checks if word is long enough and only contains letters'''
        if len(guess) != word_len:
            return False
        elif guess.isalpha() == False:
            return False
        return guess.lower()
    
    def print_guesses(self, user_guess_lis):
        '''Prints the user´s round along with their feedback for that guess'''
        print("How your round went:")
        for guess in user_guess_lis:
            print(f"{guess[0]}  {guess[1]}")

    def prompt_word_len(self):
        '''Prompts user for their desired length and returns the word bank and a an integer'''
        text = ""
        word_len = ""
        len_user_input = input("\n1. 5 letter\n2. 6 letter\n3. 7 letter\nChoose word bank: ")
        while len_user_input:
            if len_user_input == "1":
                word_len = 5
                text = "5-letters-wordle.txt"
                len_user_input = False
            elif len_user_input == "2":
                text = "6-letters-wordle.txt"
                word_len = 6
                len_user_input = False
            elif len_user_input == "3":
                text = "7-letters-wordle.txt"
                word_len = 7
                len_user_input = False
            else:
                print("\nInvalid option, choose one (1,2,3)!")
                len_user_input = input("\n1. 5 letter game\n2. 6 letter game\n3. 7 letter game\nChoose game: ")
        return text, word_len

    def prompt_guesses(self):
        '''Prompts user for their desired amount of guesses and checks if it is valid'''
        guesses = 0
        guesses_user_input = input("\nHow many guesses would you like? ")
        while guesses_user_input:
            try:
                if int(guesses_user_input) < 1:
                    print("Number must be bigger than 0!")
                    guesses_user_input = input("\nHow many guesses would you like? ")
                else:
                    guesses = guesses_user_input
                    guesses_user_input = False
            except ValueError:
                print("Must enter a number!")
                guesses_user_input = input("\nHow many guesses would you like? ")
        return int(guesses)


        
def score(guesses, current_score):
    '''Adds to users current score depending on how many guesses they had left'''
    if guesses >= 5:
        current_score += 10
    elif guesses == 4:
        current_score += 8
    elif guesses == 3:
        current_score += 6
    elif guesses == 2:
        current_score += 4
    elif guesses == 1:
        current_score += 2
    return current_score


def play_game(game, current_score, user, text, guesses_counter, word_len):
    '''Plays one round of wordle and returns the user´s score from the round'''
    game.get_answers(text)
    user_guess_lis =[]
    word = game.random_word()
    while guesses_counter != 0:
        user_guess = input(f"Guess a {word_len} letter word, {guesses_counter} guesses left: ")
        if game.valid(user_guess, word_len):
            feedback = game.guess_word(word, user_guess)
            user_guess_lis.append([user_guess, feedback])
            if game.check_win(feedback, word_len):
                print(f"\nYOU WON, THE WORD WAS {word}")
                game.print_guesses(user_guess_lis)
                current_score = score(guesses_counter, current_score)
                return current_score
            else:
                print(f"\n{user_guess}\n{feedback}\n")
                guesses_counter -= 1
        else:
            print(f"\nGuess must only contain {word_len} letters!\n")
    highscore = get_highscore()
    if current_score >= highscore:
        save_highscore(current_score, user)
    print_score(current_score, highscore)
    print(f"\nYou have lost the game!\nThe word was {word}\n")
    return 0 

def print_score(current_score, highscore):
    '''Prints score and lets user know if he got higher than the high score'''
    if current_score > highscore:
        print(f"\nCongratulations new highscore {current_score}!")
    elif current_score == highscore:
        print(f"\nCongratulations you equaled the highscore {highscore}!")
    else:
        print(f"\nYour score is {current_score} and the highscore is {highscore}!")

def options():
    '''Displays options for user and returns their selection'''
    print("\n1. Play Game\n2. Add Word\n3. Remove word\n4. Print Scores\n5. Quit")
    user_input = input("Select option: ")
    return user_input

def save_highscore(highscore, user):
    file_object = open("highscore.txt", "a")
    file_object.write(f"{highscore},{user},")
    file_object.close()

def get_highscore():
    highscore = 0
    file_object = open("highscore.txt", "r")
    highscore_lis = file_object.read().split(",")
    for item in highscore_lis:
        try:
            item = int(item)
            if item > highscore:
                highscore = item
        except ValueError:
            pass
    return highscore

def log_in_option():
    '''Displays log in options for user and returns their selection'''
    print("\n1. Log in\n2. Sign up\n3. Quit")
    user_input = input("Select option: ")
    return user_input

def play(user):
    '''Session for user'''
    current_score = 0
    victories = 0
    losses = 0
    game = Wordle()
    play = True
    while play:
        print(f"\n----Current session----\nWins: {victories}\nLosses:{losses}\nCurrent score: {current_score} ")
        user_input = options()
        if user_input == "1":
            text, word_len = game.prompt_word_len()
            guesses = game.prompt_guesses()
            current_score = play_game(game, current_score, user, text, guesses, word_len)
            if current_score != 0:
                current_score += 10
                victories += 1
            else:
                losses += 1
        elif user_input == "2":
            game.add_answer()
        elif user_input == "3":
            game.remove_answer()
        elif user_input == "4":
            print_user_score(user)
        elif user_input == "5":
            play = False
        else:
            print("\nInvalid option, try again!\n")
    if current_score != 0:
        highscore = get_highscore()
        if current_score >= highscore:
            save_highscore(current_score, user)
        print_score(current_score, highscore)
    print(f"\nGame over!\nYou ended with {victories} victories and {losses} losses.")

def print_user_score(user):
    file_object = open("highscore.txt", "r")
    highscore_lis = file_object.read().split(",")
    print(f"\n{user} scores:")
    index = 0
    for item in highscore_lis:
        if item.lower().strip() == user:
            print(highscore_lis[index-1])
        index += 1
    
def log_in(user_dict):
    try:
        user = input("\nEnter your username: ")
        user_id = user_dict[user.lower()]
        return user
    except KeyError:
        print("User not found")

def sign_up(user_info):
    user = input("\nEnter your username: ")
    success = user_info.add_user(user)
    return user, success

def main():
    runnable = True
    user_info = Wordle()
    while runnable:
        user_dict = user_info.get_users()
        option = log_in_option()
        if option == "1":
            user = log_in(user_dict)
            if user != None:
                print(f"You have successfully logged-in {user}")
                play(user)
            pass
        elif option == "2":
            user, success = sign_up(user_info)
            if success == 1:
                print(f"You have successfully signed up {user}")
                play(user)
            pass
        elif option == "3":
            runnable = False
        else:
            print("\nInvalid option, try again!\n")
        


if __name__ == "__main__":
    main()