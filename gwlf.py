class GainWeightLoseFat:

    def __init__(self):
        self.height1 = 0
        self.height0 = 0
        self.units = ""
        self.weight = 0
        self.age = 0
        self.calories = 0
        self.heightcheck = 0

    def getweight(self):
        run = True
        run2 = True
        #Make sure the user only inputs kg or lbs. If not, it'll repeat until the user does so
        while(run):

            self.units = input("what units do you use for weight?\nType \"kg\" for kilograms or \"lbs\" for pounds\n")

            if self.units.lower() == "kg":
                run = False

                while(run2):
                    self.weight = input("Type your weight in your selected units\n")

                    try:
                        if self.weight.isdigit():

                            if float(self.weight) < 0.0:
                                print(self.weight + " is an invalid weight, only type a weight in a positive value")

                            else:
                                run2 = False
                                self.weight = self.weight
                                return self.weight, self.units

                        else:
                            print(self.weight + " is an invalid weight, only type a weight in a positive value")

                    except ValueError:
                        print(self.weight + " is invalid, try again")

            if self.units.lower() == "lbs":
                run = False
                run2 = True

                # Error handler in case the user inputs something invalid
                while(run2):
                    self.weight = input("Type your weight in your selected units\n")

                    if self.weight.isdigit():
                        run2 = False
                        self.weight = self.weight
                        return self.weight, self.units

                    try:
                        if float(self.weight) < 0.0:
                            print(self.weight + " is an invalid weight, only type a weight in a positive value")

                        if float(self.weight) >= 0.0:
                            run2 = False

                            ##convert lbs to kg for BMR formula
                            self.weight = (float(self.weight) * 0.453592)
                            return self.weight, self.units

                    except ValueError:
                        print(str(self.weight) + " is invalid, try again")
            else:
                print("Only type either kg for kilograms or lbs for pounds")

    def getheight(self):
        run = True

        # Error handler in case the user inputs something invalid
        while(run):
            self.height = input("Type your height in centimeters. If you only know inches I’ll convert it for you\n")
            self.height = round(float(self.height), 0)

            try:

                if float(self.height) < 0.0:
                    print(self.height + " is invalid, only type a positive number please")

                if float(self.height) >= 0.0:
                    run = False
                    self.heightcheck = len(str(self.height))

                    # Checks the user's height and assigns the correct units to the value
                    # convert height from in to cm
                    if self.heightcheck <= 4:
                        self.height = float(self.height) * 2.54
                        units = " in"
                        return units

                    #If the amount of characters in height is greather than 3 then it's cm
                    if self.heightcheck > 4:
                        units = " cm"
                        return units

            except ValueError:
                print(self.height + " is invalid, only type a positive number please")

    def calculate(self):
        run = True

        # Error handler in case the user inputs something invalid
        while(run):
            self.age = input("Type your age in years\n")

            try:
                if float(self.age) < 0.0:
                    print(self.age + " is an invalid age, only enter a positive number")

                if float(self.age) >= 0.0 and float(self.age) <= 200:
                    run = False
                    self.age = self.age
                if float(self.age) > 200.0:
                    print("I don't think you're that old bub, try again")

            except ValueError:
                print(self.age + " is an invalid age, only enter an age from 0 - 200")

        run2 = True

        #Error handler in case the user inputs something invalid
        while(run2):
            self.calories = input("Type the amount of calories you burn in a day\n")

            try:
                if float(self.calories) < 0.0:
                    print(self.calories + " is an invalid amount, only enter a positive amount")

                if float(self.calories) >= 0.0:
                    run2 = False
                    self.calories = self.calories

            except ValueError:
                print(self.calories + " is an invalid amount, only enter an amount from 0 or higher")

        # calculate the amount of calories your body uses for basic metabolic functions
        print("weight = " + str(self.weight) + "\nheight = " + str(self.height) + "\nage = " + str(self.age))
        bmr = 88.362 + (13.397 * float(self.weight)) + (4.799 * float(self.height) - (5.677 * float(self.age)))

        # total calories you burn with activity and with your basic metabolic functions
        total_calories = bmr + float(self.calories)

        # the amount of calories that should compose of fat throughout the day
        fat_calories = (float(total_calories) - 500) * 0.30

        # the amount of calories that should compose of carbohydrates throughout the day
        carb_calories = (float(total_calories) - 500) * 0.60

        #If the user originally inputed in, then convert the converted in back to in as the BMR calculater needs
        #cm so regardless, the user height is converted to cm. This function converts it back to in for users who
        #are used to the imperial system
        if self.heightcheck <= 4:
            self.height = self.height * 0.393701

        # convert weight back to lbs
        if self.units == "lbs":
            self.weight = (float(self.weight) * 2.20462)

        return total_calories, self.weight, fat_calories, carb_calories, bmr, round(self.height, 0)
