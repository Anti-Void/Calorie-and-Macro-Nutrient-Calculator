import random

class AITester:

    def __int__(self):
        self.weight = 0
        self.height = 0
        self.age = 0
        self.calories = 0
        self.questionnum = 0
        self.heightcheck = 0

    #Computer chooses weight goal, will add more once other goals are implemented
    def getmode(self):
        mode = "gwlf"
        return mode

    def skipToQuestion(self):

        run = True
        while(run):

            self.questionnum = input("Type the question number you want to skip to and I'll fill in the data up to that"
                           "point.\n0 = skip to no question and just automatically fill in all the data"
                           "\n1 = weight\n2 = height\n3 = age\n4 = calories\n")

            if self.questionnum.isdigit() == True:

                if int(self.questionnum) <= 4 and int(self.questionnum) >= 0:

                    run = False
                    return self.questionnum

                else:
                    print("Error Type: Out of Range\n"
                          + str(self.questionnum) + " is an invalid choice. Please only type a number from 0 - 4")
            else:

                print("Error Type: Wrong Type, Only Positive Number Allowed\n"
                      + str(self.questionnum) + " is an invalid choice. Please only type a number from 0 - 4")



    #Randomly fills in user data with random numbers up to a specific range
    def getdata(self):

        self.weight = random.randint(100, 250)
        self.height = random.randint(153, 213)
        self.age = random.randint(18, 100)
        self.calories = random.randint(1000, 3000)

        #Convert weight to kg for BMR formula
        self.weight = (float(self.weight) * 0.453592)

        self.heightcheck = len(str(self.height))

        if self.heightcheck == 3:
            units = " cm"
        else:
            units = " in"

        return self.weight, self.height, self.age, self.calories, units

    #Calulates BMR, total calories consumed, calories needed as well as macros. Same as the user version
    def calculations(self):

        # convert height from in to cm
        if self.heightcheck < 3:
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

        return total_calories, self.weight, fat_calories, carb_calories, bmr
