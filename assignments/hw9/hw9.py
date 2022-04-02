from random import randint


def get_words(file_name):
    input_file = open(file_name, "r")
    new_list = input_file.readlines()
    return new_list


def get_random_word(words):
    new_word = len(words)
    random_num = randint(0, new_word - 1)
    updated_word = words[random_num]
    list_word = updated_word.strip()
    secret_word = ''.join(list_word)
    return secret_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    return False


def make_hidden_secret(secret_word, guesses):
    spacing = ""
    for letter in secret_word:
        if letter in guesses:
            right_answer = "{}".format(letter)
            spacing = spacing + right_answer.strip()
        else:
            wrong_answer = "_"
            spacing = spacing + wrong_answer.strip()
    return " ".join(spacing)


def won(guessed):
    if "_" not in guessed:
        return True
    return False

def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    print


if __name__ == '__main__':
    pass
    # file_name = "words.txt"
    # words = get_words("words.txt")
    # secret_word = get_random_word(words)
    # guesses = ["a"]
    # guessed = "attention"
    # print(get_words("words.txt"))
    # print(get_random_word(words))
    # print(letter_in_secret_word("a", secret_word))
    # print(make_hidden_secret(secret_word, guesses))
    # print(won(guessed))
    # play_command_line(secret_word)
    # play_graphics(secret_word)
