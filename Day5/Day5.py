from enum import Enum

# Op code 1 - add number
# Op code 2 - multiply numbers
# Op code 99 - halt


class ParameterMode(Enum):
    POSITION = '0'
    IMMEDIATE = '1'


def run_op_codes(content):
    pointer = 0

    while pointer <= len(content) - 1:
        instruction = content[pointer]
        op_code = int(instruction[-2:])
        pointer += 1

        if op_code == 99:
            return

        if 1 <= op_code <= 2:  # Arithmetic
            parameter_modes = instruction[:-2].rjust(3, '0')

            input_1, pointer = get_value(content, pointer, parameter_modes[-1])
            input_2, pointer = get_value(content, pointer, parameter_modes[-2])

            if op_code == 1:
                pointer = set_value(content, pointer, str(input_1 + input_2))
            elif op_code == 2:
                pointer = set_value(content, pointer, str(input_1 * input_2))

        elif op_code == 3:
            pointer = set_value(content, pointer, input("Enter an integer: "))

        elif op_code == 4:
            parameter_modes = instruction[:-2].rjust(3, '0')
            value, pointer = get_value(content, pointer, parameter_modes[-1])
            print(value)

        elif op_code == 5:
            parameter_modes = instruction[:-2].rjust(2, '0')

            jump_if, pointer = get_value(content, pointer, parameter_modes[-1])

            if jump_if != 0:
                pointer, _ = get_value(content, pointer, parameter_modes[-2])
            else:
                pointer += 1

        elif op_code == 6:
            parameter_modes = instruction[:-2].rjust(2, '0')

            jump_if, pointer = get_value(content, pointer, parameter_modes[-1])

            if jump_if == 0:
                pointer, _ = get_value(content, pointer, parameter_modes[-2])
            else:
                pointer += 1

        elif 7 <= op_code <= 8:  # Comparative
            parameter_modes = instruction[:-2].rjust(3, '0')

            input_1, pointer = get_value(content, pointer, parameter_modes[-1])
            input_2, pointer = get_value(content, pointer, parameter_modes[-2])

            if op_code == 7:
                pointer = set_value(content, pointer, 1 if input_1 < input_2 else 0)
            elif op_code == 8:
                pointer = set_value(content, pointer, 1 if input_1 == input_2 else 0)

        # print(f"pointer {pointer}", content[pointer], content)


def get_value(content, pointer, mode=ParameterMode.POSITION.value):
    if mode == ParameterMode.POSITION.value:
        address = int(content[pointer])
        value = int(content[address])
    elif mode == ParameterMode.IMMEDIATE.value:
        value = int(content[pointer])
    else:
        raise ValueError(f'Unknown parameter mode {mode}')

    return value, pointer + 1


def set_value(content, pointer, value):
    address = int(content[pointer])
    content[address] = value

    return pointer + 1


def main():
    with open('input.txt', 'r+') as file:
        content = file.read().split(',')

        run_op_codes(content)


if __name__ == "__main__":
    main()
