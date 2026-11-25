import random
import math

guest_name = input("Enter guest names separated by commas: ")

guest_list = [name.strip() for name in guest_name.split(",")]

guest_list = [name for name in guest_list if name]

unique_guest = list(dict.fromkeys(guest_list))

if not unique_guest:
    print("No guest names entered.")

else:
    selected_guest = random.choice(unique_guest)

    reversed_name = selected_guest[::-1]

    total_guests = len(unique_guest)

    square_root = round(math.sqrt(total_guests))

    print("\nUnique guest list:", unique_guest)
    print("Selected guest:", selected_guest)
    print("Reversed name:", reversed_name)
    print("Total unique guests:", total_guests)
    print("Rounded square root:", square_root)