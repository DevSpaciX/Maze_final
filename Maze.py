from maze_finder import find_closest_gate
from check_dead_way import MazeWayError, DeleteDeadWay
from data_visual import visual_maze

main_matrix = """   #.########
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
                    ####.#####  """


def main_finder(start_matrix, start_point: list, gate: str = ".") -> str:
    start_matrix = [level.split() for level in start_matrix.split()]
    clean_matrix = DeleteDeadWay(start_point, start_matrix).calculating()
    x_line = [start_point[1]]
    result = []
    for number, item in enumerate(clean_matrix, start=start_point[0]):
        if gate in item[0]:
            x_line.append(find_closest_gate(item, x_line[-1]))
            result.append([number, x_line[-1]])
        else:
            raise MazeWayError
    if clean_matrix[-1] == start_matrix[0]:
        number = 0
        for elem in result:
            elem[0] = elem[0] - number
            number += 2

    visual_maze(result, len(start_matrix) - 1, len(start_matrix[0][0]))
    return f"Your finish is on {result[-1]}"

print(main_finder(main_matrix,[5, 3]))
