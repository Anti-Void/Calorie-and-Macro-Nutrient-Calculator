import random

class AITester:

    def __int__(self):
        self.weight = 0
        self.height = 0
        self.age = 0
        self.calories = 0

    #Computer chooses weight goal, will add more once other goals are implemented
    def getmode(self):
        mode = "gwlf"
        return mode

    #Randomly fills in user data with random numbers up to a specific range
    def getdata(self):
        self.weight = random.randint(0, 600)
        self.height = random.randint(0, 200)
        self.age = random.randint(0, 100)
        self.calories = random.randint(1000, 3000)

        return self.weight, self.height, self.age, self.calories

    #Calulates BMR, total calories consumed, calories needed as well as macros. Same as the user version
    def calculations(self):

        # convert height from in to cm
        heightcheck = len(str(self.height))
        if heightcheck < 3:
            heightCM = float(self.height) * 2.54
        else:
            heightCM = float(self.height)
        # calculate the amount of calories your body uses for basic metabolic functions
        bmr = 88.362 + (13.397 * float(self.weight)) + (4.799 * float(heightCM) - (5.677 * float(self.age)))

        # total calories you burn with activity and with your basic metabolic functions
        total_calories = bmr + float(self.calories)

        # the amount of calories that should compose of fat throughout the day
        fat_calories = (float(total_calories) - 500) * 0.30

        # the amount of calories that should compose of carbohydrates throughout the day
        carb_calories = (float(total_calories) - 500) * 0.60

        # convert weight back to lbs
        self.weight = (float(self.weight) * 2.20462)

        return total_calories, self.weight, fat_calories, carb_calories, bmr, heightcheck
