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


class IntCodeComputer:
    POSITION = '0'
    IMMEDIATE = '1'
    RELATIVE = '2'

    def __init__(self, content):
        self.content = content
        self.content.extend([0 for _ in range(1000)])

        self.pointer = 0
        self.relative_base = 0

    def run(self, input_func=input, output_func=print):
        while self.pointer <= len(self.content) - 1:
            instruction = self.content[self.pointer]
            op_code = int(instruction[-2:])
            self.pointer += 1

            if op_code == 99:
                return

            if 1 <= op_code <= 2:  # Arithmetic
                parameter_modes = instruction[:-2].rjust(3, '0')

                input_1, self.pointer = self.get_value(parameter_modes[-1])
                input_2, self.pointer = self.get_value(parameter_modes[-2])

                if op_code == 1:
                    self.pointer = self.set_value(str(input_1 + input_2), parameter_modes[-3])
                elif op_code == 2:
                    self.pointer = self.set_value(str(input_1 * input_2), parameter_modes[-3])

            elif op_code == 3:  # Input
                parameter_modes = instruction[:-2].rjust(1, '0')
                self.pointer = self.set_value(input_func(), parameter_modes[-1])

            elif op_code == 4:  # Output
                parameter_modes = instruction[:-2].rjust(1, '0')
                value, self.pointer = self.get_value(parameter_modes[-1])
                output_func(value)

            elif op_code == 5:
                parameter_modes = instruction[:-2].rjust(2, '0')

                jump_if, self.pointer = self.get_value(parameter_modes[-1])

                if jump_if != 0:
                    self.pointer, _ = self.get_value(parameter_modes[-2])
                else:
                    self.pointer += 1

            elif op_code == 6:
                parameter_modes = instruction[:-2].rjust(2, '0')

                jump_if, self.pointer = self.get_value(parameter_modes[-1])

                if jump_if == 0:
                    self.pointer, _ = self.get_value(parameter_modes[-2])
                else:
                    self.pointer += 1

            elif 7 <= op_code <= 8:  # Comparative
                parameter_modes = instruction[:-2].rjust(3, '0')

                input_1, self.pointer = self.get_value(parameter_modes[-1])
                input_2, self.pointer = self.get_value(parameter_modes[-2])

                if op_code == 7:
                    self.pointer = self.set_value(1 if input_1 < input_2 else 0, parameter_modes[-3])
                elif op_code == 8:
                    self.pointer = self.set_value(1 if input_1 == input_2 else 0, parameter_modes[-3])

            elif op_code <= 9:
                parameter_modes = instruction[:-2].rjust(1, '0')

                value, self.pointer = self.get_value(parameter_modes[-1])
                self.relative_base += value

            if DEBUG:
                print()
                print(f"pointer {self.pointer} | ", f"instruction {instruction} |",
                      f"next value {self.content[self.pointer]} |", self.content)
                print()

    def run_until_output(self, input_func=input):
        while self.pointer <= len(self.content) - 1:
            instruction = self.content[self.pointer]
            op_code = int(instruction[-2:])
            self.pointer += 1

            if op_code == 99:
                return

            if 1 <= op_code <= 2:  # Arithmetic
                parameter_modes = instruction[:-2].rjust(3, '0')

                input_1, self.pointer = self.get_value(parameter_modes[-1])
                input_2, self.pointer = self.get_value(parameter_modes[-2])

                if op_code == 1:
                    self.pointer = self.set_value(str(input_1 + input_2), parameter_modes[-3])
                elif op_code == 2:
                    self.pointer = self.set_value(str(input_1 * input_2), parameter_modes[-3])

            elif op_code == 3:  # Input
                parameter_modes = instruction[:-2].rjust(1, '0')
                self.pointer = self.set_value(input_func(), parameter_modes[-1])

            elif op_code == 4:  # Output
                parameter_modes = instruction[:-2].rjust(1, '0')
                value, self.pointer = self.get_value(parameter_modes[-1])
                return value

            elif op_code == 5:
                parameter_modes = instruction[:-2].rjust(2, '0')

                jump_if, self.pointer = self.get_value(parameter_modes[-1])

                if jump_if != 0:
                    self.pointer, _ = self.get_value(parameter_modes[-2])
                else:
                    self.pointer += 1

            elif op_code == 6:
                parameter_modes = instruction[:-2].rjust(2, '0')

                jump_if, self.pointer = self.get_value(parameter_modes[-1])

                if jump_if == 0:
                    self.pointer, _ = self.get_value(parameter_modes[-2])
                else:
                    self.pointer += 1

            elif 7 <= op_code <= 8:  # Comparative
                parameter_modes = instruction[:-2].rjust(3, '0')

                input_1, self.pointer = self.get_value(parameter_modes[-1])
                input_2, self.pointer = self.get_value(parameter_modes[-2])

                if op_code == 7:
                    self.pointer = self.set_value(1 if input_1 < input_2 else 0, parameter_modes[-3])
                elif op_code == 8:
                    self.pointer = self.set_value(1 if input_1 == input_2 else 0, parameter_modes[-3])

            elif op_code <= 9:
                parameter_modes = instruction[:-2].rjust(1, '0')

                value, self.pointer = self.get_value(parameter_modes[-1])
                self.relative_base += value

            if DEBUG:
                print()
                print(f"pointer {self.pointer} | ", f"instruction {instruction} |",
                      f"next value {self.content[self.pointer]} |", self.content)
                print()

    def get_value(self, mode=POSITION):
        if mode == self.POSITION:
            address = int(self.content[self.pointer])
            value = int(self.content[address])

        elif mode == self.IMMEDIATE:
            value = int(self.content[self.pointer])

        elif mode == self.RELATIVE:
            address = int(self.content[self.pointer]) + self.relative_base
            value = int(self.content[address])

        else:
            raise ValueError(f'Unknown parameter mode {mode}')

        if DEBUG:
            print(str(value) + ", ", end='')

        return value, self.pointer + 1

    def set_value(self, value, mode=POSITION):
        if mode == self.POSITION:
            address = int(self.content[self.pointer])
            self.content[address] = value

        elif mode == self.IMMEDIATE:
            self.content[self.pointer] = value

        if mode == self.RELATIVE:
            address = int(self.content[self.pointer]) + self.relative_base
            self.content[address] = value

        return self.pointer + 1


class Robot:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self, brain: IntCodeComputer):
        self.computer = brain
        self.panels = [[0 for _ in range(100)] for _ in range(50)]
        self.x = 0
        self.y = 50

        self.panels[self.x][self.y] = 1

        self.painted_tiles = set()
        self.direction = self.UP

    def get_panel(self):
        return str(self.panels[self.x][self.y])

    def turn(self, direction):
        if direction == 1:
            if self.direction == self.LEFT:
                self.direction = self.UP
            else:
                self.direction += 1
        else:
            if self.direction == self.UP:
                self.direction = self.LEFT
            else:
                self.direction -= 1

    def move_forward(self):
        if self.direction == self.UP:
            self.y += 1
        elif self.direction == self.RIGHT:
            self.x += 1
        elif self.direction == self.DOWN:
            self.y -= 1
        elif self.direction == self.LEFT:
            self.x -= 1

    def run(self):
        while True:
            paint_color = self.computer.run_until_output(self.get_panel)
            direction = self.computer.run_until_output(self.get_panel)

            if paint_color is None or direction is None:
                break

            self.panels[self.x][self.y] = paint_color

            self.painted_tiles.add((self.x, self.y))

            self.turn(direction)

            self.move_forward()

        print("Num tiles: ", len(self.painted_tiles))

    def print(self):
        for x in range(len(self.panels)):
            for y in range(len(self.panels[0])):
                if str(self.panels[x][y]) == '0':
                    print('⬛', end='')
                else:
                    print('⬜', end='')
            print()


def main():
    with open('input.txt', 'r+') as file:
        content = file.read().split(',')

        robot = Robot(IntCodeComputer(content))

        robot.run()

        robot.print()


if __name__ == "__main__":
    main()
