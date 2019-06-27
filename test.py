import math
import os

class Parts(object):
    def __init__(self,**kwargs):
        self.dblPartDimension1 = 0
        self.dblPartDimension2 = 0
        self.intJointedSides1 = 0
        self.intJointedSides2 = 0

        self.questions = dict(
            Dimension1="Enter the first dimension for this part : ",
            Dimension2="Enter the second dimension for this part : ",
            Jointed1="Enter the amount of jointed sides for dimension 1 : ",
            Jointed2="Enter the amount of jointed sides for dimension 2 : "
        )

    def get_inputs(self):
        self.dblPartDimension1 = self.get_valid_input(self.questions.get("Dimension1"))
        self.dblPartDimension2 = self.get_valid_input(self.questions.get("Dimension2"))
        self.intJointedSides1 = self.get_valid_input(self.questions.get("Jointed1"))
        self.intJointedSides2 = self.get_valid_input(self.questions.get("Jointed2"))

    def get_cutsize(self):
        self.dblCutsize1 = self.dblPartDimension1 + self.intJointedSides1
        self.dblCutsize2 = self.dblPartDimension2 + self.intJointedSides2

os.system("pause")