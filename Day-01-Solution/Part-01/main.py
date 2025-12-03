def spin_dial(current_number:int, turn_direction: str, direction_count: int):
    # we know 100 is one rotation so just do nothing
    if direction_count != 100:
        if turn_direction == 'L':
            current_number -= direction_count
            if current_number < 0:
                current_number += 100
        elif turn_direction == 'R':
            current_number += direction_count
            if current_number > 99:
                current_number -= 100
        else:
            print('Uh oh.. Santa is not happy...')
    return current_number

if __name__ == "__main__":
    with open('combinations.txt', 'r') as file:
        combinations = file.read().splitlines()

    count_of_zeros = 0

    current_number = 50

    for combination in combinations:
        turn_direction = combination[0]
        direction_count = int(combination[1:])

        # if the value is larger than 100, we can trim off the excess so we can avoid any type of recursion
        if direction_count > 100:
            direction_count = int(str(direction_count)[-2:])
        
        current_number = spin_dial(current_number=current_number, 
                  turn_direction=turn_direction,
                  direction_count=direction_count)

        if current_number == 0:
            count_of_zeros += 1

    print(count_of_zeros)
