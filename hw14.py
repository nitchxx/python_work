import random
import math

customer_names = input("Enter customer names separated by commas: ")

customer_list = [name.strip() for name in customer_names.split(",")]

customer_list = [name for name in customer_list if name]

unique_customers = list(dict.fromkeys(customer_list))

if len(unique_customers) < 2:
    print("At least 2 unique participants are required.")

else:
    random.shuffle(unique_customers)

    winners = random.sample(unique_customers, 2)

    winner_one = winners[0][::-1]
    winner_two = winners[1][::-1]

    total_participants = len(unique_customers)

    square_root = round(math.sqrt(total_participants))

    print("\nUnique participants:", unique_customers)
    print("Winner 1:", winner_one)
    print("Winner 2:", winner_two)
    print("Total unique participants:", total_participants)
    print("Rounded square root:", square_root)