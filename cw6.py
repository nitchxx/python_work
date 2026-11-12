attendance = [18, 20, 19, 15, 21]
i = 0
day = 0
sum = 0

for attend in attendance :
    if attend >= 20 :
        print(attend,"Full")
    else:
        print(attend,"NOT FULL")

while i < len(attendance) :
     if attendance[i] >= 20 :
        day += 1 

     i += 1

print("Total Full day :",day)

for count in attendance :
    sum += count

print("Total attendance :",sum)

