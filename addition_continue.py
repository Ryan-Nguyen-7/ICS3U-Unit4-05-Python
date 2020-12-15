# Created by Ryan Nguyen
# Created on December 2020
# This program gets addends and the number of addends
#   they would like to add, then finds the sum of them


def main():
    # This function does addition

    total = 0
    addend_as_number = 0
    # loops input
    loop_counter_as_string = input \
        ("How many numbers would you like to add?: ")
    try:
        loop_counter_as_number = int(loop_counter_as_string)
        if loop_counter_as_number > 0:
            for loop_counter in range(loop_counter_as_number):
                # addend input
                addend_as_string = input("Enter addend: ")

                addend_as_number = int(addend_as_string)
                if addend_as_number > 0:
                    total = total + addend_as_number
                else:
                    continue
        else:
            print("Integer must be positive")
    except Exception:
        print("Invalid integer")
    print("The sum is {}".format(total))


if __name__ == "__main__":
    main()
