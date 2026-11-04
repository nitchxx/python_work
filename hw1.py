rice_price,sugar_price,oil_price = 45,40,130
rice_quantity,sugar_quantity,oil_quantity = 3,2.5,1.8

rice_bill = rice_price * float(rice_quantity)
sugar_bill = sugar_price * sugar_quantity
oil_bill = oil_price * oil_quantity
total_bill = rice_bill + sugar_bill + oil_bill

print("Rice :",rice_bill ,
      "\nSugar :",sugar_bill,
      "\noil :",oil_bill,
      "\ntotal_bill :", total_bill)

print(int(total_bill))
print(str(total_bill))


import random
delivery_charge = random.randrange(5,10)
final_bill = total_bill + delivery_charge
print("Total bill with delivery charge is ",final_bill)