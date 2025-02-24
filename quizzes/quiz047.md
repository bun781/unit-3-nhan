# Paper Code
![image](https://github.com/user-attachments/assets/64ce2a4d-8bff-4c34-8493-6f24cbb987fd)

# Code
```.py
class CalorieCount:
    def __init__(self, daily_limit: int):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0
    def addMeal(self, cal, pro, car, fat):
        self.protein += pro
        self. daily_intake += cal
        self.carbs += car
        self.fat += fat
    def onTrack(self)->bool:
        if self.daily_intake > self.daily_limit:
            out = False
        else:
            out = True
        return out
    def getProteinPercentage(self):
        return 4*self.protein/self.daily_intake
sunday = CalorieCount(1500)

sunday.addMeal(716, 38, 38, 45)
sunday.addMeal(230, 16, 8, 16)
sunday.addMeal(568, 38, 50, 24)

print(sunday.onTrack()) #returns False
print(sunday.getProteinPercentage())
#returns 0.24
```

# Proof of Work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/f0d26576-947b-47bc-ac96-04c7e88d7aa0" />
