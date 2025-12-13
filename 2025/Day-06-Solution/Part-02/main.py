def calculate(numbers: list[int], operation_type: str) -> int:
    if len(numbers) == 1:
        return numbers[0]

    if operation_type == '+':
        total_num = 0
        for number in numbers:
            total_num += number
    elif operation_type == '*':
        total_num = 1
        for number in numbers:
            total_num *= number
    else:
        print("Uh oh.. something is not right!")

    return total_num

def main():
    with open('math_problems.txt', 'r') as file:
        math_problems = file.read().splitlines()

    grand_total = 0

    operator_char_list = list(math_problems[-1])
    step_indexes = []
    for index,char in enumerate(operator_char_list):
        if char != ' ':
            step_indexes.append(index)

    for index, current_line in enumerate(math_problems):
        math_problems[index] = [current_line for current_line in list(current_line)]

    while len(step_indexes) > 0:

        if len(step_indexes) > 1:
            stop_index = step_indexes[1]
        else:
            # end of list
            stop_index = len(math_problems[0])

        numbers_to_calc = []

        for column_index in range(step_indexes[0],stop_index):
            operation_type = operator_char_list[step_indexes[0]]
            number_builder = []

            for row_index in range(len(math_problems) - 1):
                value = math_problems[row_index][column_index]

                if value != ' ':
                    number_builder.append(math_problems[row_index][column_index])
            
            if len(number_builder) > 0:
                numbers_to_calc.append(int(''.join(number_builder)))

        total = 0
        if len(numbers_to_calc) > 0:
            total = calculate(numbers=numbers_to_calc, operation_type=operation_type)
        grand_total += total
        
        # This is our condition to know we are finished
        step_indexes.pop(0)

    print(grand_total)

if __name__ == '__main__':
    main()