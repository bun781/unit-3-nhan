# Paper Solution
![image](https://github.com/user-attachments/assets/96f5464c-8ee0-4669-a2ef-26acd718bddc)

# Code
```.py
class rainDrops:
    def __init__(self):
        pass
    def pour(self, n:int)->str:
        out = ''
        if n%3 == 0:
            out += 'Pling'
        if n%5 == 0:
            out += 'Plang'
        if n%7 == 0:
            out += 'Plong'
        elif n%3 != 0 and n%5 != 0:
            out = n

        return out

a = rainDrops()
print(a.pour(28))
print(a.pour(30))
print(a.pour(34))

```

# Proof of Work
![image](https://github.com/user-attachments/assets/cdf7aad2-b481-4374-a28c-107559e1b13e)
