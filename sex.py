class Sex:

    def __init__(self):
        self.sex = ""

    def bioSex(self):

        ##getting user data to make calculations
        run = True

        #Checks for errors, if an error is found, it'll loop back to the input function so the user
        #can try again
        while(run):

            self.sex = input("What is your biological sex?\n")
            if self.sex.lower() == "male":
                run = False
                self.sex = self.sex
                return self.sex

            if self.sex.lower() == "female":
                run = False
                self.sex = self.sex
                return self.sex

            else:
                print("Please only type either \"male\" or \"female\"")

    #assigns the sex for the computer, only set to male due to the lack of female support
    #Will make it so the computer randomly chooses between male and female
    def comSex(self):
        self.sex = "male"
        return self.sex