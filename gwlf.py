class GainWeightLoseFat:

    def __init__(self):
        self.height1 = 0
        self.height0 = 0
        self.units = 0
        self.weight = 0
        self.age = 0
        self.calories = 0
        self.heightCM = 0
    def getweight(self):
        self.units = input("what units do you use for weight?\nType \"kg\" for kilograms or \"lbs\" for pounds\n")
        self.weight = input("Type your weight in your selected units\n")

        ##convert lbs to kg for BMR formula
        if self.units == "lbs":
            self.weight = (float(self.weight) * 0.453592)
        return self.weight

    def getheight(self):
        self.height = input("Type your height in centimeters. If you only know inches I’ll convert it for you\n")
        heightCheck = len(self.height)

        # convert height from in to cm
        if heightCheck < 3:
            self.heightCM = float(self.height) * 2.54

        return self.heightCM, heightCheck

    def calculate(self):
        self.age = input("Type your age in years\n")
        self.calories = input("Type the amount of calories you burn in a day\n")

        # calculate the amount of calories your body uses for basic metabolic functions
        bmr = 88.362 + (13.397 * float(self.weight)) + (4.799 * float(self.heightCM) - (5.677 * float(self.age)))

        # total calories you burn with activity and with your basic metabolic functions
        total_calories = bmr + float(self.calories)

        # the amount of calories that should compose of fat throughout the day
        fat_calories = (float(total_calories) - 500) * 0.30

        # the amount of calories that should compose of carbohydrates throughout the day
        carb_calories = (float(total_calories) - 500) * 0.60

        # convert weight back to lbs
        self.weight = (float(self.weight) * 2.20462)

        return total_calories, self.weight, fat_calories, carb_calories, bmr
