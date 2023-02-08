
from datetime import date
import re


class Spending:
    def writeFile(self, f):
        while True:
            item = input("Enter the reason of spending(or to stop press 'q'): ")
            if item.lower() == "q":
                f.close()
                break
            
            cost = float(input("Enter the cost of the item: ₹ "))
            expence = f"{item}  ->  {cost}\n" 
            
            f.write(expence)


class Display:
    def disp(self, name):
        f1 = open(name, "r")
        lst = []
        for line in f1:
            line = line.strip()
            if "Today's Expence is:" in line:
                continue
            x = re.findall(r"[-+]?(?:\d*\.*\d+)", line)
            for i in x:
                lst.append(float(i))
        f1.close()
        return lst
    
    
    def costLst(self, lst, name):
        total = 0
        f = open(name, "a")
        for data in lst:
            total += data
        final = f"\nToday's Expence is:  {total}\n\n"
        f.write(final)
        print(f"today's Expence is: ₹ {total}")
        f.close()

if __name__ == "__main__":
    name = f"{date.today()}.txt"
    f= open(name, 'a')
    s = Spending()
    s.writeFile(f)
    d = Display()
    total = d.disp(name)
    d.costLst(total,name)
