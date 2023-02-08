
from datetime import datetime as dt
from datetime import date
import re


f = open("spendings.txt", "a")

while True:
    item = input("Enter the reason of spending(or to stop press 'q'): ")
    if item.lower() == "q":
        f.write("\n")
        f.close()
        break
    
    cost = int(input("Enter the cost of the item: ₹ "))
    expence = f"\n{str(dt.now())} ) {item}  ->  {cost}" 
    
    f.write(expence)

f1 = open("spendings.txt", "r")
for line in f1:
    print("enter FOR")
    if str(dt.now()) in line:
        print("enter IF")
        x = re.findall('[0-9]+', line)
        print(x)
f1.close()

# print(date.today())
