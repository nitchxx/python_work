items = ["milk", "bread", "eggs"]

def add_item(item):
    items.append(item)

def remove_last_item():
    items.pop()

item = lambda product :print("item : ",product)
for product in items:
    item(product)


def count_characters(character = 0):
    if character == len(items):
        return 0
    else:
        return len(items[character]) + count_characters(character+1)

print("bonus : ",count_characters())


        

