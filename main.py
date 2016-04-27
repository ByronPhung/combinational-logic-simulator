#===============================================================================
#  File        : main.py
#  Project     : Combinational Logic Simulator
#  Description : Simulate combinational logic circuits using Python.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Libraries
#===============================================================================

#-------------------------------------------------------------------------------
#  Existing Python Modules
#-------------------------------------------------------------------------------

# Common pathname manipulations
# Reference: https://docs.python.org/2/library/os.path.html
import os.path

#-------------------------------------------------------------------------------
#  Custom Modules
#-------------------------------------------------------------------------------

# Logic gate simulation
# Reference: gate.py
from gate import Gate

# Combinational logic simulation
# Reference: circuit.py
from circuit import Circuit

#===============================================================================
#  Functions
#===============================================================================

def main():
    # Ask for path to circuit file.
    file = input("INPUT:: Enter path to circuit file (e.g. D:\Path\To\circuit1.in): ")

    # If the file exists, then check if it is a supported input file.
    if os.path.isfile(file):
        # If it is a supported input file, then parse it.
        if file.endswith(".in"):
            # Create a new Circuit object consisting of the gates from the
            # input file.
            circuit = Circuit(file)
            print("INFO::  Printing gates in circuit...")
            print()

            # Print the list of gates sorted by ID.
            circuit.print_gates()
            print()

            # Prompt the user for desired outputs.
            print("INFO::  Use spaces to select multiples (e.g., 1 4 6).")
            selected_output = input("INPUT:: Enter desired outputs by ID for truth table: ")

            # Print the truth table for the selected outputs.
            print("INFO::  Printing truth table for selected outputs...")
            print()
            circuit.print_truth_table(selected_output.split())
            
        # Otherwise, display an error.
        else:
            print("ERROR:: Invalid file (\"" + file + "\"")
            print("        File must be of extension .in (e.g. circuit1.in).")
            
    # Otherwise, display an error.
    else:
        print("ERROR:: Cannot find file at path \"" + file + "\"")

#===============================================================================
#  Main Execution
#===============================================================================

main()