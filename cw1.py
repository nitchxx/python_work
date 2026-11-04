apple= 15.5  
orange = 20
grape = 10.25

total_voloume = apple+orange+grape
print(total_voloume)

sold_int = int(total_voloume)
print(sold_int)

sold_string = str(total_voloume)
print("The total quantity sold is"+" "+sold_string+" "+ "litres.")

import random
additional_bonus = random.randrange(5,10)

final_voloume = total_voloume + additional_bonus
print("final voloume :",final_voloume)
