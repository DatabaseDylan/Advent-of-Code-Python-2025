def spin_dial(current_number:int, turn_direction: str, direction_count: int, completed_rotations: int):
    original_number = current_number
    if turn_direction == 'L':
        current_number -= direction_count
        if current_number < 0:
            current_number += 100
            # avoid double counting
            if current_number != 0 and original_number !=0:
                completed_rotations += 1
    elif turn_direction == 'R':
        current_number += direction_count
        if current_number > 99:
            current_number -= 100
            # avoid double counting
            if current_number != 0 and original_number !=0:
                completed_rotations +=1
    else:
        print('Uh oh.. Santa is not happy...')
    return current_number, completed_rotations

if __name__ == "__main__":
    with open('combinations.txt', 'r') as file:
        combinations = file.read().splitlines()

    count_of_zeros = 0

    current_number = 50

    for combination in combinations:
        turn_direction = combination[0]
        direction_count = int(combination[1:])
        completed_rotations = 0
        # if the value is larger than 100, we can trim off the excess so we can avoid any type of recursion
        if direction_count > 100:
            # Part 2 of the puzzle asks that we track how many times zero is passed so we need to track that as well
            completed_rotations = int(direction_count / 100)
            direction_count = int(str(direction_count)[-2:])

        current_number, completed_rotations = spin_dial(current_number=current_number, 
                  turn_direction=turn_direction,
                  direction_count=direction_count,
                  completed_rotations=completed_rotations)

        if current_number == 0:
            count_of_zeros += 1

        count_of_zeros += completed_rotations

    print(count_of_zeros)
