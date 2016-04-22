#===============================================================================
#  File        : main.py
#  Project     : Combinational Logic Simulator
#  Description : Python simulation of combinational logic circuits.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Libraries
#===============================================================================

from gate import Gate

#===============================================================================
#  Functions
#===============================================================================

def main():
    gate1 = Gate(0, "not1", "not", ["a", "b"])
    gate2 = Gate(1, "or1", "or", ["a", "b"])
    gate3 = Gate(2, "and1", "and", ["a", "b"])
    gate4 = Gate(3, "xor1", "xor", ["a", "b"])
    gate5 = Gate(4, "nand1", "nand", ["a", "b"])
    gate6 = Gate(5, "nor1", "nor", ["a", "b"])
    gate7 = Gate(6, "xnor1", "xnor", ["a", "b"])
    gate1.print()
    gate2.print()
    gate3.print()
    gate4.print()
    gate5.print()
    gate6.print()
    gate7.print()

#===============================================================================
#  Main Execution
#===============================================================================

main()
