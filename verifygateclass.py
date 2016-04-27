#===============================================================================
#  File        : verifygateclass.py
#  Project     : Combinational Logic Simulator
#  Description : Verify the custom gate.py module.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Libraries
#===============================================================================

#-------------------------------------------------------------------------------
#  Custom Modules
#-------------------------------------------------------------------------------

# Logic gate simulation
# Reference: gate.py
from gate import Gate

#===============================================================================
#  Functions
#===============================================================================

def main():
    # Create a list of all the possible gates.
    # The inputs are arbitrary and do not matter in this current test setup.
    gates = [Gate(0, "not1", "not", ["a", "b"]),
             Gate(1, "or1", "or", ["a", "b"]),
             Gate(2, "and1", "and", ["a", "b"]),
             Gate(3, "xor1", "xor", ["a", "b"]),
             Gate(4, "nand1", "nand", ["a", "b"]),
             Gate(5, "nor1", "nor", ["a", "b"]),
             Gate(6, "xnor1", "xnor", ["a", "b"])]

    # Print each gate information and its truth table.
    for gate in gates:
        gate.print_info()
        print()
        gate.truth_table(3)
        print()

#===============================================================================
#  Main Execution
#===============================================================================

main()