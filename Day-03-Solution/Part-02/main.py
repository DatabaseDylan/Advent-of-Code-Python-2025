def main():
    with open('batteries.txt', 'r') as file:
        batteries = file.read().splitlines()

    battery_voltages = []

    for battery in batteries:
        unique_numbers = list(dict.fromkeys(list(battery)))
        unique_numbers.sort(reverse=True)
        largest_first_digit = unique_numbers[0]
        battery = tuple(battery)

        i = 0
        keep_running = True
        largest_unique_number_index = 1
        # Find the first occurence of the largest first digit
        while keep_running == True:
            for digit in battery:
                if digit == largest_first_digit and len(battery) - (i + 1) <= 10:
                    # if our largest digit in the list only has 10 digits (not 11) after it, we need to try again with the next highest number!
                    # Keep trying until we get all the way through the list
                    largest_first_digit = unique_numbers[largest_unique_number_index]
                    largest_unique_number_index += 1
                    i = 0
                    break
                elif digit == largest_first_digit:
                    i += 1
                    keep_running = False
                    break
                else:
                    i += 1

        remaining_digits = [{"digit": -1, "index": i - 1}]
        # Find the largest second digit after the index of the largest first digit
        for current_loop in range(1, 12):
            for index in range(remaining_digits[-1]["index"] + 1,len(battery)):
                current_num = int(battery[index])

                # If we are running out of number, we can no longer be picky so we just accept every number moving forward
                if (len(battery) - index) < (12 - current_loop) and len(remaining_digits) != current_loop:
                    remaining_digits.append({"digit": current_num, "index": index})
                    break

                if current_num > remaining_digits[-1]["digit"] or len(remaining_digits) != current_loop:
                    # Safeguard to protect against instance where we find a high number at the tail end of the tuple, 
                    # but there aren't enough digits to satisfy the 12
                    if (len(battery) - index) < (12 - current_loop):
                        break
                    if len(remaining_digits) == current_loop:
                        remaining_digits.pop(-1)
                    remaining_digits.append({"digit": current_num, "index": index})
                    if current_num == 9:
                        # Optimization
                        break
        

        voltage = list(str(largest_first_digit)) + [str(remaining_digits['digit']) for remaining_digits in remaining_digits]
        if len(voltage) != 12:
            raise ValueError("Voltage is not 12 digits. Something is wrong!")
        battery_voltages.append(int(''.join(voltage)))
    
    print(sum(battery_voltages))

if __name__ == '__main__':
    main()