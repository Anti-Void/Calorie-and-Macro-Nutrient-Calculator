class Sex:

    def __init__(self):
        self.sex = ""

    def bioSex(self):

        ##getting user data to make calculations
        self.sex = input("What is your biological sex?\n")
        return self.sex

    def comSex(self):
        self.sex = "male"
        return self.sex