from typing import Literal

def traverse(current_line: int, current_beam_index:int, direction: Literal["left", "right"], puzzle: list[str], total_timelines: int, traversal_tracking: list[dict[str, any]]) -> int:
    num_timelines = 0
    for line_index, _ in enumerate(puzzle, current_line):

        # skip first two lines
        if line_index in (0, 1):
            continue
        
        if line_index == len(puzzle) - 1:
            num_timelines = 1
            return num_timelines

        if puzzle[line_index][current_beam_index] == "^":
            if direction == "left":
                traversal_tracking.append({
                    "line_index": line_index,
                    "value_index": current_beam_index, 
                    "is_left_checked": True, 
                    "is_right_checked": False
                    })
                current_beam_index = current_beam_index - 1
            elif direction == "right":
                traversal_tracking.append({
                    "line_index": line_index,
                    "value_index": current_beam_index, 
                    "is_left_checked": False, 
                    "is_right_checked": True
                    })
                current_beam_index = current_beam_index + 1

    return num_timelines

def main():
    with open("puzzle.txt","r") as file:
        puzzle = file.read().splitlines()
    
    for index, item in enumerate(list(puzzle[0])):
        if item == "S":
            current_beam_index = index

    total_timelines = 0
    traversal_tracking = []

    # convert data structure to a list of lists so we can keep track of beams with indexes
    for line_index, horizontal_line in enumerate(puzzle):
        puzzle[line_index] = list(horizontal_line)

    num_timelines = traverse(current_line=0, current_beam_index=current_beam_index, direction="left", puzzle=puzzle, total_timelines=total_timelines, traversal_tracking=traversal_tracking)
    total_timelines = total_timelines + num_timelines

    while len(traversal_tracking) > 0:
        print(total_timelines)
        # if both routes have been checked, we no longer need it in the list and we can continue traversing upward
        if traversal_tracking[-1]["is_left_checked"] == True and traversal_tracking[-1]["is_right_checked"] == True:
            traversal_tracking.pop()

        elif traversal_tracking[-1]["is_left_checked"] == False:
            traversal_tracking[-1]["is_left_checked"] = True
            num_timelines = traverse(current_line=traversal_tracking[-1]['line_index'], current_beam_index=traversal_tracking[-1]['value_index'] - 1, direction="left", puzzle=puzzle, total_timelines=total_timelines, traversal_tracking=traversal_tracking)
            total_timelines = total_timelines + num_timelines

        elif traversal_tracking[-1]["is_right_checked"] == False:
            traversal_tracking[-1]["is_right_checked"] = True
            num_timelines = traverse(current_line=traversal_tracking[-1]['line_index'], current_beam_index=traversal_tracking[-1]['value_index'] + 1, direction="right", puzzle=puzzle, total_timelines=total_timelines, traversal_tracking=traversal_tracking)
            total_timelines = total_timelines + num_timelines
    print(total_timelines)

if __name__ == "__main__":
    main()
