 # -----------------------------------------------------------------
# Project Name: Saw Cut Yields
# Name: Rodney Clark
# -----------------------------------------------------------------
import math
import os

intCount = int(0)

#Gather inputs
dblDimension1 = float(input("Enter Dimension 1 "))
dblDimension2 = float(input("Enter Dimension 2 "))
dblJointEdge1 = float(input("How many edge finished sides (Dimension 1) "))
dblJointEdge2 = float(input("How many edge finished sides (Dimension 2) "))

# Calculate How much is needed for jointed edges
dblJoint1 = float(dblJointEdge1 * .03125)
dblJoint2 = float(dblJointEdge2 * .03125)

# Calculate The Size Of Each cut after sawblade
dblCutSize1 = (dblDimension1 + dblJoint1)
dblCutSize2 = (dblDimension2 + dblJoint2)

# Calculate The Yield if cut each direction
intYield1 = int(96 / (dblCutSize1 + .125)) * int(48 / (dblCutSize2 + .125))
intYield2 = int(96 / (dblCutSize2 + .125)) * int(48 / (dblCutSize1 + .125))

# Print results
print("Cut dimensions for this part are ", dblCutSize1, " x ", dblCutSize2)
print("The cut size of ", dblCutSize1, " along the 96 yields ", intYield1, " pieces.")
print("The cut size of ", dblCutSize2, " along the 96 yields ", intYield2, " pieces.")

#Compare Yield 1 to yield 2 and print result
if ( intYield1 > intYield2 ):
    print("The cut size of ", dblCutSize1, " along the 96 yields is the better yield" )
else:
    print("The cut size of ", dblCutSize2, " along the 96 yields is the better yield" )

os.system("pause")
