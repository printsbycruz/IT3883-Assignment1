# Program Name: Assignment1.py
# Course: IT3883/Section V
# Student Name: John Doe
# Assignment Number: Lab1
# Due Date: 06/12/2026
# Purpose: This program shows a simple text menu that lets the user add text
#          to a "buffer" (basically just a string variable), clear it out,
#          look at what's currently stored, or quit the program. It keeps
#          looping and asking for input until the user picks the exit option.
# Resources Used: Python docs (docs.python.org) to double check how string
#                 concatenation with += works.

# this string is going to hold whatever the user has typed in so far
# starts off empty since nothing has been entered yet
my_buffer = ""

# using this as a simple on/off switch for the while loop below
keep_going = True

# loop keeps running and re-showing the menu until the user chooses to exit
while keep_going:

    # show the menu so the user knows what their options are
    print("\n===== MAIN MENU =====")
    print("1) Append data to the input buffer")
    print("2) Clear the input buffer")
    print("3) Display the input buffer")
    print("4) Exit the program")

    # ask the user what they want to do
    user_choice = input("What would you like to do? (1-4): ")

    if user_choice == "1":
        # ask the user for some text and stick it onto the end of our buffer
        text_to_add = input("Type the text you want to add: ")
        my_buffer += text_to_add  # += just adds this onto the existing string
        print("Got it, that's been added to the buffer.")

    elif user_choice == "2":
        # just wipe the buffer back to an empty string
        my_buffer = ""
        print("Buffer is now empty.")

    elif user_choice == "3":
        # show whatever is currently saved in the buffer
        # if nothing has been typed yet this will just print nothing
        print("Here's what's currently in the buffer:")
        print(my_buffer)

    elif user_choice == "4":
        # flip the switch so the while loop stops on the next check
        print("Thanks for using the program, goodbye!")
        keep_going = False

    else:
        # catches anything that isn't 1, 2, 3, or 4
        print("Hmm, that's not a valid option. Please choose 1-4.")
