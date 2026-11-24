new_item = input("Enter a new item: ")

with open("items.txt", "a+") as f:
    f.write(new_item + "\n")
    f.seek(0)
    print("\nFull list of items:")
    print(f.read())