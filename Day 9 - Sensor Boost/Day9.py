# 1 - Add
# 2 - Multiply
# 3 - Input
# 4 - Output
# 5 - Jump if true
# 6 - Jump if false
# 7 - Less than
# 8 - Equal
# 9 - Change relative base

DEBUG = False


class ParameterMode:
    POSITION = '0'
    IMMEDIATE = '1'
    RELATIVE = '2'


def run_op_codes(content):
    pointer = 0
    relative_base = 0

    content.extend([0 for _ in range(512)])

    while pointer <= len(content) - 1:
        instruction = content[pointer]
        op_code = int(instruction[-2:])
        pointer += 1

        if op_code == 99:
            return

        if 1 <= op_code <= 2:  # Arithmetic
            parameter_modes = instruction[:-2].rjust(3, '0')

            input_1, pointer = get_value(content, pointer, relative_base, parameter_modes[-1])
            input_2, pointer = get_value(content, pointer, relative_base, parameter_modes[-2])

            if op_code == 1:
                pointer = set_value(content, pointer, str(input_1 + input_2), relative_base, parameter_modes[-3])
            elif op_code == 2:
                pointer = set_value(content, pointer, str(input_1 * input_2), relative_base, parameter_modes[-3])

        elif op_code == 3:  # Input
            parameter_modes = instruction[:-2].rjust(1, '0')
            pointer = set_value(content, pointer, input("Enter an integer: "), relative_base, parameter_modes[-1])

        elif op_code == 4:  # Output
            parameter_modes = instruction[:-2].rjust(1, '0')
            value, pointer = get_value(content, pointer, relative_base, parameter_modes[-1])
            print(value)

        elif op_code == 5:
            parameter_modes = instruction[:-2].rjust(2, '0')

            jump_if, pointer = get_value(content, pointer, relative_base, parameter_modes[-1])

            if jump_if != 0:
                pointer, _ = get_value(content, pointer, relative_base, parameter_modes[-2])
            else:
                pointer += 1

        elif op_code == 6:
            parameter_modes = instruction[:-2].rjust(2, '0')

            jump_if, pointer = get_value(content, pointer, relative_base, parameter_modes[-1])

            if jump_if == 0:
                pointer, _ = get_value(content, pointer, relative_base, parameter_modes[-2])
            else:
                pointer += 1

        elif 7 <= op_code <= 8:  # Comparative
            parameter_modes = instruction[:-2].rjust(3, '0')

            input_1, pointer = get_value(content, pointer, relative_base, parameter_modes[-1])
            input_2, pointer = get_value(content, pointer, relative_base, parameter_modes[-2])

            if op_code == 7:
                pointer = set_value(content, pointer, 1 if input_1 < input_2 else 0, relative_base, parameter_modes[-3])
            elif op_code == 8:
                pointer = set_value(content, pointer, 1 if input_1 == input_2 else 0, relative_base, parameter_modes[-3])

        elif op_code <= 9:
            parameter_modes = instruction[:-2].rjust(1, '0')

            value, pointer = get_value(content, pointer, relative_base, parameter_modes[-1])
            relative_base += value

        if DEBUG:
            print()
            print(f"pointer {pointer} | ", f"instruction {instruction} |", f"next value {content[pointer]} |", content)
            print()


def get_value(content, pointer, relative_base, mode=ParameterMode.POSITION):
    if mode == ParameterMode.POSITION:
        address = int(content[pointer])
        value = int(content[address])

    elif mode == ParameterMode.IMMEDIATE:
        value = int(content[pointer])

    elif mode == ParameterMode.RELATIVE:
        address = int(content[pointer]) + relative_base
        value = int(content[address])

    else:
        raise ValueError(f'Unknown parameter mode {mode}')

    if DEBUG:
        print(str(value) + ", ", end='')

    return value, pointer + 1


def set_value(content, pointer, value, relative_base, mode=ParameterMode.POSITION):
    if mode == ParameterMode.POSITION:
        address = int(content[pointer])
        content[address] = value

    elif mode == ParameterMode.IMMEDIATE:
        content[pointer] = value

    if mode == ParameterMode.RELATIVE:
        address = int(content[pointer]) + relative_base
        content[address] = value

    return pointer + 1


def main():
    with open('input.txt', 'r+') as file:
        content = file.read().split(',')

        run_op_codes(content)


if __name__ == "__main__":
    main()
