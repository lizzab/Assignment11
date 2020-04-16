# Ben Lizza
# April 16, 2020
# Main program to test sort algorithms

import random
import Search_Methods
import time

# redundant code, so make a method!
def fill_list():
    qty = int(input("How many values would you like in the list to be sorted?"))
    for i in range(1, qty + 1):
        my_list.append(random.randint(1,100001))
    print("The list has been filled with random values and now contains:")
    print(my_list)
    return qty

choice = 0

while choice != 6:
    # clears the list
    my_list = []

    print("Please make a selection from the menu below:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Quit Program")

    choice = int(input(">"))

    if choice == 1:
        print("You have selected a Bubble Sort!")
        qty = fill_list()

        # some new code to keep track of how long the method took
        start_time = time.time()

        my_list = Search_Methods.bubble_sort(my_list)
        # prints the time taken to run the sort
        print(f"** It takes {(time.time() - start_time)} seconds to complete a Bubble Sort with {qty} values **")
        print("\nAfter sorting the list with Bubble Sort, the list looks like the following:")
        print(my_list)

    elif choice == 2:
        print("You have selected a Selection Sort!")
        qty = fill_list()
        my_list = Search_Methods.selection_sort(my_list)
        print("\nAfter sorting the list with Selection Sort, the list looks like the following:")
        print(my_list)

    elif choice == 3:
        print("You have selected a Insertion Sort!")
        qty = fill_list()
        my_list = Search_Methods.insertion_sort(my_list)
        print("\nAfter sorting the list with Insertion Sort, the list looks like the following:")
        print(my_list)

    elif choice == 4:
        print("You have selected a Merge Sort!")
        qty = fill_list()
        my_list = Search_Methods.merge_sort(my_list)
        print("\nAfter sorting the list with Merge Sort, the list looks like the following:")
        print(my_list)

    elif choice == 5:
        print("You have selected a Quick Sort!")
        qty = fill_list()
        my_list = Search_Methods.quick_sort(my_list)
        print("\nAfter sorting the list with Quick Sort, the list looks like the following:")
        print(my_list)

    elif choice == 6:
        print("Thank you using the program!")

    else:
        print("You have entered an invalid menu option!\n")


