from sex import *
from gwlf import *
from AITester import *
from datetime import datetime

#Calorie and Macro Nutrient Calculator V 0.7
#Created by Anti-Void
#Last Update: May 3rd 2024 @ 9:08 PM

#Features to add: Female support,
#                 calculate average calories based upon calories burned last 7 days
#                 add the option to save multiple data blocks in one text file
#                 add other 3 fitness goals

#Creates the computer user object
com = AITester()

#boolean that determines if the program will run or not, will turn False in an event on an error
run = True

##getting user data to make calculations
while(run):

    #choice to input your own data or have the computer do it for you
    choice = input("Type \"self\" to input your own data\nType \"com\" to randomly generate user data\n")

    #Gets the biological sex from the user
    if choice.lower() == "self":
        sex = Sex()
        user_sex = sex.bioSex()

        if user_sex == "female":
            print("hot")
            run = False

        if user_sex == "male":
            run = False
        ##ask them their exercise goals

        run2 = True

        #Gets the user's fitness goal, if they type an invalid goal the program will loop back and ask the user again
        #until they type a valid goal
        while(run2):

            goal = input("Type \"gain\" if you want to gain weight\nType \"lose\" if you want to "
                         "lose weight\nType \"gwlf\""
                         " if you want to gain muscle and lose fat at the same time\nType \"muscle\""
                         " if you just want to gain muscle and don’t want to worry about fat %\n")

            if goal.lower() == "gwlf":
                run2 = False
                gwlf = GainWeightLoseFat()

                #get the user's weight
                weight, weightunits = gwlf.getweight()

                #Get the user's height and store whether or not it's in cm or in
                units = gwlf.getheight()

                #Function that calculates all the data and stores them in their respective variables
                total_calories, weight, fat_calories, carb_calories, BMR, height = gwlf.calculate()

                #Generate output and save to text file
                print("Be sure to include the name of the data file with the .txt extension")
                file_path = input("Where would you like me to save your data?\nEx: \"C:\ users\ data.txt\n""")

                #Display Data in console
                print("Personal Stats\nHeight = " + str(height) + str(units) + "\nWeight = " + str(round(float(weight), 1)) +
                      " " + str(weightunits) + "\n")

                print("Total Amount of Calories Burned Daily = " + str(round(total_calories, 1)) +
                    "\nBMR = " + str(round(BMR, 1)) + "\nCalories Needed to Loose Fat = "
                    + str(round(total_calories - 500, 1)) + " cal\nTo gain muscle, make sure you are eating\n" + str(round(float(weight) * 0.8, 1)) +
                    "g of protein\n" + str(round(fat_calories / 9, 1)) + "g of fat\n" + str(round(carb_calories / 4, 1)) +
                      " g of carbs\nIn order to maximize muscle gain while in a caloric deficit to loose fat.")

                #Pulls the current date and time from user's computer
                current_datetime = datetime.now()
                convert_to_string = current_datetime.strftime("%m-%d-%Y %H:%M:%S")

                #Save data to text file
                with open(file_path, "w") as file:

                    file.write("Date: " + convert_to_string + "\n\n")

                    file.write("Personal Stats\n\nHeight = " + str(height) + str(units) + "\nWeight = " + str(
                        round(float(weight), 1)) + " " + str(weightunits) + "\n")

                    file.write("\nTotal Amount of Calories Burned Daily = " + str(round(total_calories, 1)) +
                               "\nBMR = " + str(round(BMR, 1)) + "\nCalories Needed to Loose Fat = "
                               + str(round(total_calories - 500, 1)) + " cal\n")

                    file.write("\nTo gain muscle, make sure you are "
                               "eating\n\n" + str(round(float(weight) * 0.8, 1)) +
                               "g of protein\n" + str(round(fat_calories / 9, 1)) + "g of fat\n" +
                               str(round(carb_calories / 4, 1)) + " g of carbs\nIn order to maximize muscle"
                                                                      " gain while in a caloric deficit to loose fat.")

                print("Data Saved to " + file_path)

            else:
                print("Please input a valid fitness goal")

    #Starts the computer mode
    if choice.lower() == "com":
        sex = Sex()
        com_sex = sex.comSex()
        tester = AITester()
        if com_sex == "female":
            print("hot")
            run = False

        if com_sex == "male":
            run = False
        ##ask them their exercise goals
            com_goal = tester.getmode()

            if com_goal == "gwlf":

                com_weight, com_height, com_age, com_calories = tester.getdata()

                com_total_calories, com_weight, com_fat_calories, com_carb_calories, com_bmr, heightcheck = tester.calculations()

                if heightcheck < 3:
                    units = " cm"
                else:
                    units = " in"

                #Generate output and save it to text file

                print("Be sure to include the name of the data file with the .txt extension")
                file_path = input("Where would you like me to save your data?\nEx: \"C:\ users\ data.txt\n""")

                print("Personal Stats\nHeight = " + str(com_height) + units + "\nWeight = "+ str(round(com_weight, 1)) +
                      " lbs\n")

                print("Total Amount of Calories Burned Daily = " + str(round(com_total_calories, 1)) +
                    "\nBMR = " + str(round(com_bmr, 1)) + "\nCalories Needed to Loose Fat = "
                    + str(round(com_total_calories - 500, 1)) + " cal\nTo gain muscle, make sure you are eating\n"
                      + str(round(float(com_weight) * 0.8, 1)) + "g of protein\n" + str(round(com_fat_calories / 9, 1))
                      + "g of fat\n" + str(round(com_carb_calories / 4, 1)) + " g of carbs\nIn order to maximize muscle"
                        " gain while in a caloric deficit to loose fat.")

                current_datetime = datetime.now()
                convert_to_string = current_datetime.strftime("%m-%d-%Y %H:%M:%S")

                with open(file_path, "w") as file:

                    file.write("Date: " + convert_to_string + "\n\n")

                    file.write("Personal Stats\n\nHeight = " + str(com_height) + units + "\nWeight = " + str(
                        round(com_weight, 1)) + " lbs\n")

                    file.write("\nTotal Amount of Calories Burned Daily = " + str(round(com_total_calories, 1)) +
                               "\nBMR = " + str(round(com_bmr, 1)) + "\nCalories Needed to Loose Fat = "
                               + str(round(com_total_calories - 500, 1)) + " cal\n")

                    file.write("\nTo gain muscle, make sure you are "
                               "eating\n\n" + str(round(float(com_weight) * 0.8, 1)) +
                               "g of protein\n" + str(round(com_fat_calories / 9, 1)) + "g of fat\n" +
                               str(round(com_carb_calories / 4, 1)) + " g of carbs\nIn order to maximize muscle"
                                                                      " gain while in a caloric deficit to loose fat.")

                print("Data Saved to " + file_path)

