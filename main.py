#===================================================================================================================================
#  File        : main.py
#  Project     : Combinational Logic Simulator
#  Description : Simulate combinational logic circuits using Python.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===================================================================================================================================

#===================================================================================================================================
#  Libraries
#===================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------
#  Existing Python Modules
#-----------------------------------------------------------------------------------------------------------------------------------

# Parser for command-line options, arguments, and sub-commands
# Reference: https://docs.python.org/3.3/library/argparse.html
import argparse

# Common pathname manipulations
# Reference: https://docs.python.org/2/library/os.path.html
import os.path

#-----------------------------------------------------------------------------------------------------------------------------------
#  Custom Modules
#-----------------------------------------------------------------------------------------------------------------------------------

# Combinational logic simulation
# Reference: circuit.py
from circuit import Circuit

# Logic gate simulation
# Reference: gate.py
from gate import Gate

# Handle basic system operations
# Reference: system.py
from system import *

#===================================================================================================================================
#  Global Variables
#===================================================================================================================================

VERSION = "1.2.0"

#===================================================================================================================================
#  Functions
#===================================================================================================================================

def get_args():
    parser = argparse.ArgumentParser(description='v' + VERSION + ' - Simulates combinational logic circuits and generates a truth table.')
    parser.add_argument('circuit_file',
                        nargs=1,
                        help='path to input circuit file (e.g. path/to/circuit.in)')
    parser.add_argument('-o', '--out',
                        nargs=1,
                        dest='output_file',
                        help='output truth table to specified file instead of printing to console')
    parser.add_argument('--format-csv',
                        dest='format_csv',
                        action='store_true',
                        help='output truth table in CSV format instead of whitespace-separated row/col')

    return parser.parse_args()

def validate_selected_outputs(selected_outputs, num_gates):
        """Ensure the selected outputs are in range.

        Keyword arguments:
        selected_outputs -- Original list of selected outputs
        num_gates        -- Number of gates in the circuit
        """
        for i in range(len(selected_outputs)):
            if int(selected_outputs[i]) >= num_gates or int(selected_outputs[i]) < 0:
                print("        Ignoring " + selected_outputs[i] + " out of range... ")
                selected_outputs.pop(i)
                i = i - 1

        return selected_outputs

def main():
    # Parse the command-line arguments.
    args = get_args()
    circuit_file = args.circuit_file[0]
    output_file = args.output_file
    if output_file:
        output_file = output_file[0]
    format_csv = args.format_csv

    # If the file exists, then check if it is a supported input file.
    if os.path.isfile(circuit_file):
        # If it is a supported input file, then parse it.
        if circuit_file.endswith(".in"):
            # Create a new Circuit object consisting of the gates from the input file.
            circuit = Circuit(circuit_file, output_file, format_csv)
            print("INFO::  Printing gates in circuit...")
            print()

            # Print the list of gates sorted by ID.
            circuit.print_gates()
            print()

            # Prompt the user for desired outputs.
            print("INFO::  Use spaces to select multiples (e.g., 1 4 6).")
            print("INFO::  To calculate all gates, just press 'Enter' without inputting anything.")
            selected_output = input("INPUT:: Select gates: ")

            # Validate the selected outputs to ensure they are in range.
            print("INFO::  Validating selected outputs...")
            selected_outputs = validate_selected_outputs(selected_output.split(), len(circuit.get_gates()))

            # Generate the truth table for the selected outputs.
            if output_file:
                print("INFO::  Outputting truth table to \"" + output_file + "\"...")
            else:
                print("INFO::  Printing truth table for selected outputs...")
            print("        This may take awhile for large numbers of inputs because of 2^n combinations...")
            print("        Total Combinations: " + str(pow(2, circuit.get_num_of_general_input_values())))
            if output_file is None:
                print()
            circuit.print_truth_table(selected_outputs)
            
        # Otherwise, display an error.
        else:
            print("ERROR:: Invalid file: \"" + circuit_file + "\"")
            print("        File must be of extension .in (e.g. circuit1.in).")
            
    # Otherwise, display an error.
    else:
        print("ERROR:: Cannot find file at path \"" + circuit_file + "\"")

#===================================================================================================================================
#  Main Execution
#===================================================================================================================================

main()
