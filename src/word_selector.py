import random
dict_fp = "C:\\Users\\natal\\PycharmProjects\\pythonProject\\nerdle\\dictionary.txt"

class WordSelector:
    def __init__(self):
        with open(dict_fp, "r") as dict_file:
            self.wordle_dict = dict_file.read().splitlines()
        self.used_words = []

    def select_word(self):
        word = random.choice(self.wordle_dict)
        self.wordle_dict.remove(word)
        self.used_words.append(word)
        if len(self.wordle_dict) == 0:
            self.reshuffle_words()

        return word

    def reshuffle_words(self):
        self.wordle_dict = self.used_words
        self.used_words = []
