#===============================================================================
#  File        : gate.py
#  Project     : Combinational Logic Simulator
#  Description : Gate class for combinational logic simulator.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Libraries
#===============================================================================

# Functions creating iterators for efficient looping
# Reference: https://docs.python.org/2/library/itertools.html
from itertools import *

#===============================================================================
#  Class Definition
#===============================================================================

class Gate(object):
    """A class that defines the properties of a logic gate to simulate a
    combinational logic circuit.

    Keyword arguments:
    __id    -- Block ID
    __name  -- Block name
    __type  -- Logic gate type
    __input -- List of input names
    """
    def __init__(self, id, name, type, input):
        self.__id = id
        self.__name = name.upper()
        self.__type = type.upper()
        self.__input = input

    def output(self, input):
        """Evaluate the output of the current gate based on its type given an
        input value.
        
        Keyword arguments:
        input -- Input value; could be a list or a single int (NOT gate)
        """
        if self.__type == "NOT":
            return logic_not(input)

        elif self.__type == "OR":
            return logic_or(input)

        elif self.__type == "AND":
            return logic_and(input)

        elif self.__type == "XOR":
            return logic_xor(input)

        elif self.__type == "NAND":
            return logic_not(logic_and(input))

        elif self.__type == "NOR":
            return logic_not(logic_or(input))

        elif self.__type == "XNOR":
            return logic_not(logic_xor(input))

        else:
            return 0

    def truth_table(self, bit_size):
        """Print out the truth table of the logic gate.

        This is designed primarily for verifygateclass.py and debugging purposes
        to verify the accuracy of each logic implementation.

        Keyword arguments:
        bit_size -- Maximum number of bits to test
        """

        # If the gate is a NOT gate, then simply do a basic inverter test.
        if self.__type == "NOT":
            print("I0 OUT")
            for i in range(2):
                print(str(i).rjust(2) + " ", end="")
                print(str(self.output(i)).rjust(2))

        # Otherwise, generate a truth table with the specified bit size.
        else:
            # Create the table headers (I for input and OUT for output).
            for i in range(bit_size):
                print("I" + str(i) + " ", end="")
            print("OUT")

            # Generate the 2^n bit combinations.
            combinations = list(product([0, 1], repeat=bit_size))

            # Generate the output for each bit combination.
            for combination in combinations:
                for bit in combination:
                    print(str(bit).rjust(2) + " ", end="")
                print(str(self.output(combination)).rjust(2))

    def print(self):
        """Print the stored gate information.

        This is designed primarily for verifygateclass.py and debugging purposes
        to verify the accuracy of each logic implementation.

        Keyword arguments:
        <None>
        """
        print("Gate " + str(self.__id))
        print("    * Name   : " + self.__name)
        print("    * Type   : " + self.__type)
        print("    * Inputs : " + str(self.__input))

def logic_not(input):
    """Perform a logic NOT on the input value.

    Keyword arguments:
    input -- Input value
    """
    # If input is logic 1, then return a logic 0.
    if input is 1:
        return 0

    # Otherwise, return a logic 1.
    else:
        return 1

def logic_and(input):
    """Perform a logic AND on all the input values.

    Keyword arguments:
    input -- List of input values
    """
    # If there is a logic 0 at any moment, then simply return a logic 0.
    for value in input:
        if value is 0:
            return 0

    # Otherwise, return 1 if no logic 0 is found.
    return 1

def logic_or(input):
    """Perform a logic OR on all the input values.

    Keyword arguments:
    input -- List of input values
    """
    # If there is a logic 1 at any moment, then simply return a logic 1.
    for value in input:
        if value is 1:
            return 1

    # Otherwise, return 0 if no logic 1 is found.
    return 0

def logic_xor(input):
    """Perform a logic XOR on all the input values.

    Keyword arguments:
    input -- List of input values
    """
    output = input[0]
    for i in range(1, len(input))
        # If the stored output is the same as the current input, then set the
        # output to logic 0.
        if output is input[i]:
            output = 0

        # Otherwise, set the output to logic 1.
        else:
            output = 1

    # Return the calculated logic output.
    return output
