#===================================================================================================================================
#  File        : gate.py
#  Project     : Combinational Logic Simulator
#  Description : Simulate logic gates.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===================================================================================================================================

#===================================================================================================================================
#  Libraries
#===================================================================================================================================

#-----------------------------------------------------------------------------------------------------------------------------------
#  Existing Python Modules
#-----------------------------------------------------------------------------------------------------------------------------------

# Functions creating iterators for efficient looping
# Reference: https://docs.python.org/2/library/itertools.html
from itertools import *

#===================================================================================================================================
#  Class Definition
#===================================================================================================================================

class Gate(object):
    """Simulate logic gates.

    Keyword arguments:
    id    -- Block ID
    name  -- Block name
    type  -- Logic gate type
    input -- List of input names
    """
    def __init__(self, id, name, type, input):
        self.id = id
        self.name = name.upper()
        self.type = type.upper()
        self.input = input

    def output(self, input):
        """Evaluate the output of the current gate based on its type.
        
        Keyword arguments:
        input -- Input value; could be a list (all) or a single int (NOT gate)
        """
        if self.type == "NOT":
            return self.__not(input)
        elif self.type == "OR":
            return self.__or(input)
        elif self.type == "AND":
            return self.__and(input)
        elif self.type == "XOR":
            return self.__xor(input)
        elif self.type == "NAND":
            return self.__not(self.__and(input))
        elif self.type == "NOR":
            return self.__not(self.__or(input))
        elif self.type == "XNOR":
            return self.__not(self.__xor(input))
        else:
            print("ERROR:: Invalid gate type (type = \"" + self.type + "\")")
            print("        Use a valid gate type (NOT, OR, AND, XOR, NAND, NOR, or XNOR).")
            return 0

    def truth_table(self, bit_size):
        """Print out the truth table of the logic gate.

        This is designed primarily for verifygateclass.py and debugging
        purposes to verify each logic implementation.

        Keyword arguments:
        bit_size -- Maximum number of bits to test
        """

        # If the gate is a NOT gate, then simply do a basic inverter test for
        # 2 inputs.
        if self.type == "NOT":
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

            # Generate 2^n bit combinations.
            combinations = list(product([0, 1], repeat=bit_size))

            # Generate the output for each bit combination.
            for combination in combinations:
                for bit in combination:
                    print(str(bit).rjust(2) + " ", end="")
                print(str(self.output(combination)).rjust(2))

    def print_info(self):
        """Print the stored gate information.

        This is designed primarily for verifygateclass.py and debugging
        purposes to verify the accuracy of each logic implementation.

        Keyword arguments:
        <None>
        """
        print("Gate " + str(self.id))
        print("    * Name   : " + self.name)
        print("    * Type   : " + self.type)
        print("    * Inputs : " + str(self.input))

    def __not(self, input):
        """Perform a logic NOT on the input value.

        Keyword arguments:
        input -- Input value
        """
        final_input = None

        # If the input is a list, then take the first element.
        if type(input) is list:
            final_input = input[0]

        # Otherwise, take the input as is.
        else:
            final_input = input

        # If the input was still not assigned, then display an error.
        if final_input is None:
            print("ERROR:: Invalid input to NOT gate (input = \"" + input + "\"")

        # Otherwise, evaluate the NOT logic.
        else:
            # If input is logic 1, then return a logic 0.
            if final_input is 1:
                return 0

            # Otherwise, return a logic 1.
            else:
                return 1

    def __and(self, input):
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

    def __or(self, input):
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

    def __xor(self, input):
        """Perform a logic XOR on all the input values.

        Keyword arguments:
        input -- List of input values
        """
        output = input[0]
        for i in range(1, len(input)):
            # If the stored output is the same as the current input, then set the
            # output to logic 0.
            if output is input[i]:
                output = 0

            # Otherwise, set the output to logic 1.
            else:
                output = 1

        # Return the calculated logic output.
        return output
        