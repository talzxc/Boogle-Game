from boggle_board_randomizer import *
from typing import *

DICT_FILE = "boggle_dict.txt"


def load_dictionary(filename: str = DICT_FILE):
    """
    function: make a list from the dictionary file
    """
    word_list = []
    with open(filename) as words:
        for word in words:
            word_list.append(word.strip('\n'))
    return word_list


class Game:
    def __init__(self, dict_file: str):
        self.__dictionary = load_dictionary(dict_file)
        self.board: List = randomize_board()
        self.__score = 0

    def update_score(self, score_add: int):
        """
        function: given an int the score updates accordingly
        """
        self.__score += score_add**2

    def get_score(self):
        return self.__score

    def word_check(self, word: str):
        """
        function: return whether the give word exists
        """
        return word in self.__dictionary


if __name__ == '__main__':
    import screen
