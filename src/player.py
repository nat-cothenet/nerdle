import word_selector
import wordle_dict
from PyInquirer import prompt


class Nerdle:
    def __init__(self):
        self.word_selector = word_selector.WordSelector()
        self.wordle_dict = wordle_dict.WordleDict()
        self.score = {i: 0 for i in range(7)}

    def play_game(self):
        for i in range(999999):
            game_word = self.word_selector.select_word()
            success = False
            for i in range(1, 7):
                question = [
                    {
                        'type': 'input',
                        'name': f'guess_{i}',
                        'message': 'Guess a 5-letter word',
                        'validate': lambda x: self.wordle_dict.is_valid(x.lower())
                    }
                ]
                guess = list(prompt(question).values())[0].lower()
                result = self.guess_word(guess, game_word, i)
                print(f'\t\t\t{"".join(result)}')
                if result == (["$"] * 5):
                    print("SUCCESS!! You did it!")
                    success = True
                    self.score[i] += 1
                    break
            if not success:
                print("Womp womp")
                print(f"The word was {game_word}!")
                self.score[0] += 1

            print("Your record is:")
            for g, wl in self.score.items():
                if g == 0:
                    print(f"{wl} losses")
                else:
                    print(f"{wl} wins in {g} guesses")
            question = [{
                'type': 'confirm',
                'message': 'Play again?',
                'name': 'continue',
                'default': True,
            }]
            cont = list(prompt(question).values())[0]
            if not cont:
                break
        self.wordle_dict.save_word_scores()

    def guess_word(self, guess, game_word, guess_num):
        result = []
        for idx, ch in enumerate(guess):
            if ch == game_word[idx]:
                result.append("$")
            elif ch in game_word:
                result.append("~")
            else:
                result.append("_")
        self.wordle_dict.score_word(guess, result, guess_num)
        return result


if __name__ == "__main__":
    nerdle = Nerdle()
    nerdle.play_game()
