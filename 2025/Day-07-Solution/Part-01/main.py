def split_beam(current_beam_index: int, current_beam_indexes: set[int], max_beam_index: int, current_horizontal_line: list[str]) -> None:
    
    # remove current beam
    current_beam_indexes.discard(current_beam_index)

    left_beam_index = current_beam_index - 1
    right_beam_index  = current_beam_index + 1

    # modify the set in place if not out of bounds and not "^"
    if left_beam_index >= 0 and current_horizontal_line[left_beam_index] != "^":
        current_beam_indexes.add(left_beam_index)
    if right_beam_index <= max_beam_index and current_horizontal_line[right_beam_index] != "^":
        current_beam_indexes.add(right_beam_index)

    return None

def main():
    with open("puzzle.txt","r") as file:
        puzzle = file.read().splitlines()
    
    for index, item in enumerate(list(puzzle[0])):
        if item == "S":
            starting_beam_index = index

    # used to make sure we don't fall out of bounds on the right-most side
    max_beam_index = len(list(puzzle[0])) - 1

    # keep track of unique beam location
    current_beam_indexes = set()
    current_beam_indexes.add(starting_beam_index)

    # keep track of number of splits
    total_split_count = 0

    # convert data structure to a list of lists so we can keep track of beams with indexes
    for line_index, horizontal_line in enumerate(puzzle):

        # skip first line
        if line_index == 0:
            continue

        # convert to list so we can keep track of indexes
        puzzle[line_index] = list(horizontal_line)

        for value_index, value in enumerate(puzzle[line_index]):
            if value == "^" and value_index in current_beam_indexes:
                split_beam(current_beam_index=value_index, current_beam_indexes=current_beam_indexes, max_beam_index=max_beam_index, current_horizontal_line=puzzle[line_index])
                total_split_count = total_split_count + 1
            
    print(total_split_count)

if __name__ == "__main__":
    main()
