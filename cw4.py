fruits = ["Grapes","Apple","Orange","Mango"]
vegetables = ["Carrot","Cucumber","Onion","Tomato"]
bevereages = ["7UP","Cococola","Redbull","Pepsi"]

print(fruits ,"\n", vegetables ,"\n", bevereages)

fruits.append("Watermelon")
print(fruits)

vegetables.insert(1,"Potato")
print(vegetables)

bevereages.pop()
print(bevereages)

inventory =[fruits,vegetables,bevereages]
print(inventory)

print(fruits[:2])

print(vegetables[-1])

fruitlen = [len(x) for x in fruits]
print(fruitlen)

if "Water" in bevereages:
    print("Yes")
else:
    print("No")

tupleForFirst = (fruits[0],vegetables[0],bevereages[0])
print(tupleForFirst)