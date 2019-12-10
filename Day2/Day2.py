# Op code 1 - add number
# Op code 2 - multiply numbers
# Op code 99 - halt


def run_op_codes(content):
    for i in range(0, len(content) - 1, 4):
        op_code = content[i]

        if op_code == '99':
            return

        input_1_pos = int(content[i + 1])
        input_2_pos = int(content[i + 2])
        output_pos = int(content[i + 3])

        input_1 = int(content[input_1_pos])
        input_2 = int(content[input_2_pos])

        if op_code == '1':
            content[output_pos] = str(input_1 + input_2)

        elif op_code == '2':
            content[output_pos] = str(input_1 * input_2)

        print(op_code)


def main():

    with open('input.txt', 'r+') as file:
        content = file.read().split(',')
        print(content)

        run_op_codes(content)

        print(content)




if __name__ == "__main__":
    main()
