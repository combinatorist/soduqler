import unittest
import sudoqler as sud
import numpy as np
import pdb

example_one_line = '...847.5...5...2.7.4..6..3.....7.3..3.......2..7.1.....5..9..1.8.4...5...1.685...\n'

example_sudoku2d = np.asarray([['.', '.', '.', '8', '4', '7', '.', '5', '.'],
                               ['.', '.', '5', '.', '.', '.', '2', '.', '7'],
                               ['.', '4', '.', '.', '6', '.', '.', '3', '.'],
                               ['.', '.', '.', '.', '7', '.', '3', '.', '.'],
                               ['3', '.', '.', '.', '.', '.', '.', '.', '2'],
                               ['.', '.', '7', '.', '1', '.', '.', '.', '.'],
                               ['.', '5', '.', '.', '9', '.', '.', '1', '.'],
                               ['8', '.', '4', '.', '.', '.', '5', '.', '.'],
                               ['.', '1', '.', '6', '8', '5', '.', '.', '.']])

example_sudoku2d_int = np.asarray([[0, 0, 0, 8, 4, 7, 0, 5, 0],
                                   [0, 0, 5, 0, 0, 0, 2, 0, 7],
                                   [0, 4, 0, 0, 6, 0, 0, 3, 0],
                                   [0, 0, 0, 0, 7, 0, 3, 0, 0],
                                   [3, 0, 0, 0, 0, 0, 0, 0, 2],
                                   [0, 0, 7, 0, 1, 0, 0, 0, 0],
                                   [0, 5, 0, 0, 9, 0, 0, 1, 0],
                                   [8, 0, 4, 0, 0, 0, 5, 0, 0],
                                   [0, 1, 0, 6, 8, 5, 0, 0, 0]])

example_sudoku3d_bool = np.asarray([
    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, True, None],
     [None, None, None, None, None, None, None, None, None],
     [None, True, None, None, None, None, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, True, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, True],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, True, None],
     [None, None, None, None, None, None, True, None, None],
     [True, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, True, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, True, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, None, None, None, None, True, None],
     [None, None, True, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, True, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, True, None, None],
     [None, None, None, None, None, True, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, True, None, None, None, None, None]],

    [[None, None, None, None, None, True, None, None, None],
     [None, None, None, None, None, None, None, None, True],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, True, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]],

    [[None, None, None, True, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [True, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None]],

    [[None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, True, None, None, None, None],
     [None, None, None, None, None, None, None, None, None],
     [None, None, None, None, None, None, None, None, None]]])

example_box_sudoku = ([[0, 0, 0, 0, 0, 5, 0, 4, 0],
                       [8, 4, 7, 0, 0, 0, 0, 6, 0],
                       [0, 5, 0, 2, 0, 7, 0, 3, 0],
                       [0, 0, 0, 3, 0, 0, 0, 0, 7],
                       [0, 7, 0, 0, 0, 0, 0, 1, 0],
                       [3, 0, 0, 0, 0, 2, 0, 0, 0],
                       [0, 5, 0, 8, 0, 4, 0, 1, 0],
                       [0, 9, 0, 0, 0, 0, 6, 8, 5],
                       [0, 1, 0, 5, 0, 0, 0, 0, 0]])

example_partial_elimination = np.asarray(
    [[ None, False,  None, False, False, False,  None, False,  None],
     [ None, False, False,  None, False,  None, False, False, False],
     [ None, False,  None,  None, False,  None,  None, False,  None],
     [ None, False,  None,  None, False,  None, False, False,  None],
     [False, False,  None,  None, False,  None,  None, False, False],
     [False, False, False, False,  True, False, False, False, False],
     [False, False, False, False, False, False, False,  True, False],
     [False, False, False,  None, False,  None, False, False,  None],
     [False,  True, False, False, False, False, False, False, False]]
)

example_solution = np.asarray(
    [[1, 3, 2, 8, 4, 7, 9, 5, 6],
     [6, 8, 5, 1, 3, 9, 2, 4, 7],
     [7, 4, 9, 5, 6, 2, 1, 3, 8],
     [5, 2, 8, 4, 7, 6, 3, 9, 1],
     [3, 6, 1, 9, 5, 8, 4, 7, 2],
     [4, 9, 7, 2, 1, 3, 6, 8, 5],
     [2, 5, 6, 7, 9, 4, 8, 1, 3],
     [8, 7, 4, 3, 2, 1, 5, 6, 9],
     [9, 1, 3, 6, 8, 5, 7, 2, 4]]
)

# http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
hardest_sudoku = np.asarray(
    [[8, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 6, 0, 0, 0, 0, 0],
     [0, 7, 0, 0, 9, 0, 2, 0, 0],
     [0, 5, 0, 0, 0, 7, 0, 0, 0],
     [0, 0, 0, 0, 4, 5, 7, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 3, 0],
     [0, 0, 1, 0, 0, 0, 0, 6, 8],
     [0, 0, 8, 5, 0, 0, 0, 1, 0],
     [0, 9, 0, 0, 0, 0, 4, 0, 0]]
)

class bq_tests(unittest.TestCase):
    def test001_load(self):
        content = sud.load('test001_load.txt')
        self.assertEqual(
            content,
            example_one_line
        )

    def test002_from_one_line(self):
        sudoku2d = sud.from_one_line(example_one_line)
        self.assertEqual(
            sudoku2d.shape,
            (9,)*2
        )
        np.testing.assert_equal(
            sudoku2d,
            example_sudoku2d
        )

    def test003_array_to_int(self):
        int_array = sud.array_to_int(example_sudoku2d)
        np.testing.assert_equal(
            int_array,
            example_sudoku2d_int
        )

    def test004_abstract_array(self):
        abstract_array = sud.abstract_array(example_sudoku2d_int)
        np.testing.assert_equal(
          abstract_array,
          example_sudoku3d_bool
        )

        np.testing.assert_equal(
          sud.to_int_array(abstract_array),
          example_sudoku2d_int
        )

    def test005_box_sudoku(self):
        np.testing.assert_equal(
          sud.box_sudoku(example_sudoku2d_int),
          example_box_sudoku
        )

    def test005_rotate(self):
        positional_3d_array = np.asarray(range(1, 9 ** 3 + 1)).reshape((9,) * 3)
        result = sud.rotate(sud.rotate(sud.rotate(positional_3d_array)))
        np.testing.assert_equal(
            result,
            positional_3d_array
        )

    def test006_group_ungroup(self):
        # demonstrates logic used inside eliminate function
        test_array = np.arange(27).reshape((3, 3, 3))
        grouped = test_array.reshape((9, 3))
        ungrouped = grouped.reshape((3, 3, 3))

        np.testing.assert_equal(
            ungrouped,
            test_array
        )

    def test007_eliminate(self):
        result = sud.eliminate(example_sudoku3d_bool)
        # checks that it eliminated some (None -> False)
        self.assertTrue(np.any(
            np.dstack([result[0], example_sudoku3d_bool[0]]) == [False, None]))
        # actually checks that it eliminated some I missed in my manual attempt
        self.assertTrue(np.any(
            np.dstack([result[0], example_partial_elimination]) == [False, None]))

    def test008_deduce(self):
        result = sud.deduce(sud.eliminate(example_sudoku3d_bool))
        # previously unknown
        self.assertFalse(example_sudoku3d_bool[2 - 1][8 - 1][5 - 1] == True)
        # now known there's a 2 in the 8th row and 5th column
        self.assertTrue(result[2 - 1][8 - 1][5 - 1])

    def test009_solve(self):
        np.testing.assert_equal(
            sud.to_int_array(sud.solve(example_sudoku3d_bool)),
            example_solution
        )

    def test999_end_to_end(self):
        np.testing.assert_equal(
            sud.abstract_array(sud.array_to_int(
                    sud.from_one_line(sud.load('test001_load.txt'))
                )),
            example_sudoku3d_bool
        )


if __name__ == '__main__':
        puzzles = {'example': example_sudoku2d_int, 'hardest': hardest_sudoku}
        for name, puzzle in sorted(puzzles.items()):
            sud.demo(puzzle, name)
        unittest.main()
