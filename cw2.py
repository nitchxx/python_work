book1_price = 450
book2_price = 600
book1_title = "Python Basics"
book2_title = "Data Science Intro"

total_bill = str(book1_price + book2_price)

message = ("""ABHI Supermarket
Kattakkada, Trivandrum
SALES RECEIPT
Date: 05-11-2026
Time: 12:00 PM""")

bought_items = ("\"{}\" - ₹{}\n\"{}\" - ₹{}".format(book1_title,book1_price,book2_title,book2_price))
bill_amount = ("Total bill = ₹{}".format(total_bill))

print ( message.upper() +"\n"+bought_items.upper()+"\n"+bill_amount.upper()+"\n"+"\t"+"Thank you for shopping with us!"+"\n"+"\t"+"Visit Again!".upper())

