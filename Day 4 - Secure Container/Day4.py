def is_valid_part_1(n):
    double_digits = False
    prev_num = None

    for num in str(n):
        if prev_num is not None and num < prev_num:
            return False

        if prev_num == num:
            double_digits = True

        prev_num = num

    return double_digits


def is_valid_part_2(n):
    double_digits = False
    current_streak = 1
    prev_num = None

    for num in str(n):
        if prev_num is not None and num < prev_num:
            return False

        if prev_num == num:
            current_streak += 1
        else:
            if current_streak == 2:
                double_digits = True

            current_streak = 1

        prev_num = num

    return double_digits or current_streak == 2


if __name__ == "__main__":
    total = 0

    for n in range(353096, 843212):
        if is_valid_part_2(n):
            print(n)
            total += 1

    print(total)
