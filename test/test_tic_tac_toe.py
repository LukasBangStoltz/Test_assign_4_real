import unittest
import sys
sys.path.insert(0, '../src')
import tic_tac_toe

class TestWriteDataBRToOS(unittest.TestCase):
    def test_play_board(self):
        #Arrange
        expected = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
        #Act
        actual = tic_tac_toe.create_grid()
        #Assert
        self.assertEqual(expected, actual, "Should be the same board")

    def test_to_start_the_game(self):
        #Arrange
        expected = [[" ", " ", " "],
            [" ", "O", " "],
            [" ", " ", " "]]
        count = 1
        player_1 = 'X'
        player_2 = 'O'
        #Act
        board = tic_tac_toe.create_grid()
        #Assert
        self.assertEqual(expected, tic_tac_toe.startGamming(board, player_1, player_2, count))

    def test_who_won(self):
        #Arrange
        expected_winner = False
        winner_board = [["X", "X", "X"],
            ["O", "O", " "],
            [" ", " ", "O"]]
        count = 1
        player_1 = 'X'
        player_2 = 'O'
        #Act
        board = tic_tac_toe.create_grid()
        #Assert
        self.assertEqual(expected_winner, tic_tac_toe.isWinner(winner_board, player_1, player_2, count))

    def test_if_square_is_picked(self):
        player_1 = 'X'
        player_2 = 'O'
        row = 0
        column = 2
        expected = "The square you picked is already filled. Pick another one."
        board = [["X", "X", "X"],
             [" ", " ", " "],
             [" ", " ", " "]]

        self.assertEqual(expected, tic_tac_toe.illegal(board, player_1, player_2, row, column))

if __name__ == '__main__':
    unittest.main()