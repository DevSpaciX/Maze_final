from Maze import main_finder
from check_dead_way import MazeWayError, GateMazeError
import pytest
from unittest import mock


class TestMazeWay:
    @pytest.mark.parametrize(
        "matrix, enter, result",
        [
            (
                    """  #........#
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ####.#####
                         ##....####
                         ##########  """,
                    [5, 6],
                    [0, 5],
            ),
            (
                    """  #........#
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ####.#####
                         ##....####
                         ######.###  """,
                    [0, 6],
                    [11, 6],
            ),
            (
                    """  #........#
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ####.#####
                         ##....####
                         ######.###  """,
                    [11, 6],
                    [0, 5],
            ),
            (
                    """  #........#
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ####.#####
                         ##########
                         ######.###  """,
                    [9, 4],
                    [0, 5],
            ),
            (
                    """  #........#
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ####.#####
                         ##.#######
                         ######.###  """,
                    [0, 4],
                    [11, 6],
            ),
            (
                    """  #........#
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ##########
                         ##.#######
                         ######.###  
                         ########## """,
                    [6, 4],
                    [0, 5],
            ),
        ],
    )
    def test_check_if_maze_ok(self,
                              matrix: str, enter: list,
                              result: list) -> None:
        assert main_finder(matrix, enter) == f"Your finish is on {result}"


class TestMazeWayError:
    @pytest.mark.parametrize(
        "matrix, enter, error",
        [
            (
                    """  ##########
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ##########
                         ##.#######
                         ######.###  
                         ########## """,
                    [6, 4],
                    MazeWayError,
            ),
            (
                    """  ##########
                         #......###
                         #####.####
                         #.......##
                         #####.####
                         #.......##
                         #......###
                         #..###...#
                         #.....####
                         ##########
                         ##.#######
                         ######.###  
                         ########## """,
                    [4, 1],
                    GateMazeError,
            ),
        ],
    )
    def test_check_if_maze_is_raise_error(
            self,
            matrix: str,
            enter: list,
            error: Exception
    ) -> None:
        with pytest.raises(error):
            main_finder(matrix, enter)
