
def get_index(max_index):
    while True:
        try: 
            index = int(input("Enter an index (-1 to quit): "))
            if index == -1:
                return index
            elif 0 <= index < max_index:
                return index
            else:
                print("invalid index")
        except ValueError:
            print("invalid index")

def get_letter():
    while True:
        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print("Must be exactly one character!: ")
        elif not letter.islower():
            print("Character must be a lowercase letter!")
        else:
            return letter
            
def get_word():
    word = input("Enter a word: ")
    current_word = list(word)
    max_index = len(current_word)
    while True:
        index = get_index(max_index)
        if index == -1:
            break
        letter = get_letter()
        current_word[index] = letter
        print("".join(current_word))

get_word()