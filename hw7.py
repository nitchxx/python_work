inventory = []

def add_item(item):
    inventory.append(item)

def main():
      add_item("dog food")
      add_item("cat toy")
      add_item("bird cage")
      add_item("fish tank")

      total = count_items(inventory)

      print("Inventory Items:", inventory)
      print("Total Items:", total)

      for string in inventory :
        show_item(string)

def count_items(items):
    if not items: 

        return 0
    return 1 + count_items(items[1:])

show_item = lambda  string: print(f"Item in Stock: {string}")

main()





