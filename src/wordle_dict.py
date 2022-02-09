import json
import os.path

dict_fp_txt = "C:\\Users\\natal\\PycharmProjects\\pythonProject\\nerdle\\dictionary.txt"
dict_fp_json = "C:\\Users\\natal\\PycharmProjects\\pythonProject\\nerdle\\dictionary_with_scores.json"
green_letter_score = 10
yellow_letter_score = 5
any_letter_score = 5

class WordleDict:
    def __init__(self, refresh=False):
        if not refresh and os.path.exists(dict_fp_json):
            with open(dict_fp_json, "r") as dict_file:
                self.wordle_dict = json.load(dict_file)
        else:
            with open(dict_fp_txt, "r") as dict_file:
                self.wordle_dict = dict_file.read().splitlines()
            self.wordle_dict = {word: 0 for word in self.wordle_dict}

    def is_valid(self, word):
        return isinstance(word, str) and len(word) == 5 and word in list(self.wordle_dict.keys())

    def score_first_word(self, word, vals):
        for val in vals:
            if val == "$":
                self.wordle_dict[word] += green_letter_score
            if val == "~":
                self.wordle_dict[word] += yellow_letter_score

    def score_word(self, word, vals, guess_num):
        if guess_num == 1:
            self.score_first_word(word, vals)
        else:
            for val in vals:
                if val != "_":
                    self.wordle_dict[word] += any_letter_score/guess_num

    def save_word_scores(self):
        with open(dict_fp_json, 'w', encoding='utf-8') as f:
            json.dump(self.wordle_dict, f, ensure_ascii=False, indent=4)
