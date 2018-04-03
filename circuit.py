#===================================================================================================================================
#  File        : circuit.py
#  Project     : Combinational Logic Simulator
#  Description : Simulate combinational logic circuits.
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

#-----------------------------------------------------------------------------------------------------------------------------------
#  Custom Modules
#-----------------------------------------------------------------------------------------------------------------------------------

# Logic gate simulation
# Reference: gate.py
from gate import Gate

# Handle basic system operations
# Reference: system.py
from system import *

#===================================================================================================================================
#  Class Definition
#===================================================================================================================================

class Circuit(object):
    """Simulate combinational logic circuits.

    Keyword arguments:
    file -- Circuit file to read
    """
    def __init__(self, file, output_file, format_csv):
        self.__parse_circuit_file(file)
        self.__output_file = output_file
        self.__format_csv = format_csv

    def __parse_circuit_file(self, file):
        """Parse the circuit file.

        Keyword arguments:
        file -- Circuit file to read
        """
        self.__get_gates_from_file(file)
        self.__sort_gates_by_id(0, len(self.__gates) - 1)

    def __get_gates_from_file(self, file):
        """Get all the gates from the circuit file and store it in the circuit.

        Keyword arguments:
        file -- Circuit file to read
        """
        # Initialize a private list to hold logic gates.
        self.__gates = []
        
        # Read the .in file and get each line.
        file_content = read_file(file)
        file_content_lines = file_content.splitlines()

        # Parse each line for gate information.
        for i in range(len(file_content_lines)):
            # Get the gate information separated by whitespaces.
            data = file_content_lines[i].split()
            data_fields = []
            gate_inputs = []

            # Temporarily store each data field.
            for j in range(len(data)):
                # If j is 0, then store an int for the gate ID.
                if j == 0:
                    data_fields.append(int(data[j]))

                # Else if j is greater than 2, then store the gate inputs.
                elif j > 2:
                    gate_inputs.append(data[j].upper())

                # Otherwise, simply store either the name or type.
                else:
                    data_fields.append(data[j].upper())

            # Merge the gate inputs into the data fields list.
            data_fields.append(gate_inputs)

            # Create a new Gate object and store it.
            self.__gates.append(Gate(data_fields[0], data_fields[1], data_fields[2], data_fields[3]))

    def __sort_gates_by_id(self, left, right):
        """Sort the stored gates by ID using quick sort algorithm.

        Keyword arguments:
        <None>
        """
        # Base Condition: If all left and right indexes have finished parsing, then do nothing.
        if left == right:
            pass

        # Base Condition: If there are only 2 elements being compared, then simply check the order.
        elif left == right - 1:
            # If the gate's ID at left index is greater than that of the right, then swap the 2 gates.
            if self.__gates[left].id > self.__gates[right].id:
                temp = self.__gates[left]
                self.__gates[left] = self.__gates[right]
                self.__gates[right] = temp

        # Recursive Condition: Continue sorting the data.
        else:
            # Sum the ID values starting from the left index to the right index.
            sum = 0
            for i in range(left, right + 1):
                sum = sum + self.__gates[i].id

            # Calculate the average of the ID sum.
            average = sum / (right - left + 1)

            # Track the left and right pointers.
            left_pointer = left
            right_pointer = right

            # Divide the list into 2 sub-lists (if applicable) while the left pointer is less than the right pointer.
            while left_pointer < right_pointer:
                # While the left pointer is less than the average, keep incrementing the left pointer.
                while self.__gates[left_pointer].id < average:
                    left_pointer = left_pointer + 1

                # While the right pointer is greater than or equal to the average, keep incrementing the right pointer.
                while self.__gates[right_pointer].id >= average:
                    right_pointer = right_pointer - 1

                # If the left pointer is less than the right pointer, then swap the gates at the left and right pointers.
                if left_pointer < right_pointer:
                    temp = self.__gates[left_pointer]
                    self.__gates[left_pointer] = self.__gates[right_pointer]
                    self.__gates[right_pointer] = temp

            # If the left index is less than the right pointer, then sort the lower half sub-list.
            if left < right_pointer:
                self.__sort_gates_by_id(left, right_pointer)

            # If the right pointer is less than the left pointer, then sort the upper half sub-list.
            if right_pointer < left_pointer:
                self.__sort_gates_by_id(left_pointer, right)

    def print_gates(self):
        """Print the gates in the current circuit sorted by ID.

        Keyword arguments:
        <None>
        """
        # Print the table headers and a border.
        print("ID      Name            Type    Inputs")
        print("-" * 80)

        # Print each gate.
        for gate in self.__gates:
            # Print the gate's ID, name, and type.
            print(str(gate.id).ljust(8) + gate.name.ljust(16)
                  + gate.type.ljust(4) + " " * 4, end="")

            # Print the gate's inputs.
            for input in gate.input:
                print(input.ljust(5) + "  ", end="")
            print()

    def get_gates(self):
        """Get the gates in the current circuit.

        Keyword arguments:
        <None>
        """
        return self.__gates

    def print_truth_table(self, selected_outputs):
        """Print the truth table with the selected outputs (if applicable).

        If no outputs are selected, then all gates will be printed.

        Keyword arguments:
        selected_outputs -- List of selected outputs
        """
        # Get the number of general input values.
        num_general_values = self.get_num_of_general_input_values()

        # Print the truth table headers.
        self.__print_truth_table_headers(num_general_values, selected_outputs)
                    
        # Calculate the values of each gate and print the outputs of the selected gates (if applicable) in the truth table for
        # 2^n combinations.
        for combination in product([0, 1], repeat=num_general_values):
            gate_values = self.__calculate_outputs_for_combinations(combination)
            self.__print_gate_outputs(combination, selected_outputs, gate_values)

    def __print_truth_table_headers(self, num_bits, selected_outputs):
        """Print the headers of the truth table.

        Keyword arguments:
        num_bits         -- Max number of combination inputs
        selected_outputs -- List of selected outputs
        """
        # Print the headers for the general combinations.
        for i in range(num_bits):
            if self.__format_csv:
                print_or_output("I" + str(i) + ",", self.__output_file)
            else:
                print_or_output(("I" + str(i)).ljust(len(str(i)) + 2), self.__output_file)

        # If outputs were selected, then only print headers for those outputs.
        if len(selected_outputs) > 0:
            for i in range(len(selected_outputs)):
                output = selected_outputs[i]
                if self.__format_csv:
                    print_or_output(self.__gates[int(output)].name, self.__output_file)
                    if i < len(selected_outputs) - 1:
                        print_or_output(",", self.__output_file)
                else:
                    print_or_output(self.__gates[int(output)].name.ljust(len(self.__gates[int(output)].name) + 1), self.__output_file)

        # Otherwise, print headers for all outputs.
        else:
            for i in range(len(self.__gates)):
                gate = self.__gates[i]
                if self.__format_csv:
                    print_or_output(gate.name, self.__output_file)
                    if i < len(self.__gates) - 1:
                        print_or_output(",", self.__output_file)
                else:
                    print_or_output(gate.name.ljust(len(gate.name) + 1), self.__output_file)
        print_or_output("", self.__output_file, False)

    def __calculate_outputs_for_combinations(self, combination):
        """Calculate the outputs for the current bit combination.

        Keyword arguments:
        combination -- Current bit combination
        """
        # Create and initialize an empty list of gate values.
        gate_values = [''] * len(self.__gates)

        # While all the gate values are not found, determine the gate values.
        while not self.__are_all_gate_values_found(gate_values):
            # Parse each gate value.
            for i in range(len(gate_values)):
                # If the gate value has already been determined, then skip the current iteration.
                if gate_values[i] != '':
                    continue

                # If all the required inputs for the current gate are available, then calculate the gate value.
                if self.__are_all_required_inputs_available(self.__gates[i], gate_values):
                    # Get the int input values for the current gate.
                    inputs = []
                    for input in self.__gates[i].input:
                        if input.startswith("I"):
                            inputs.append(combination[self.__get_int_of_general_value(input)])
                        else:
                            inputs.append(gate_values[int(input)])

                    # Assign the gate value to the current index of the list of block values.
                    gate_values[i] = self.__gates[i].output(inputs)

        # Return the calculated gate values.
        return gate_values

    def __print_gate_outputs(self, combination, selected_outputs, gate_values):
        """Print the outputs of the selected gates in the truth table.

        Keyword arguments:
        combination      -- Current combination to calculate
        selected_outputs -- List of selected outputs
        gate_values      -- List of values for each gate
        """
        # Print the current general input combination.
        for i in range(len(combination)):
            if self.__format_csv:
                print_or_output(str(combination[i]) + ",", self.__output_file)
            else:
                print_or_output(str(combination[i]).ljust(len(str(i)) + 2), self.__output_file)

        # If outputs were selected, then only print the values for those outputs.
        if len(selected_outputs) > 0:
            for i in range(len(selected_outputs)):
                output = selected_outputs[i]
                if self.__format_csv:
                    print_or_output(str(gate_values[int(output)]), self.__output_file)
                    if i < len(selected_outputs) - 1:
                        print_or_output(",", self.__output_file)
                else:
                    print_or_output(str(gate_values[int(output)]).ljust(len(self.__gates[int(output)].name) + 1), self.__output_file)

        # Otherwise, print values for all outputs.
        else:
            for i in range(len(self.__gates)):
                gate = self.__gates[i]
                if self.__format_csv:
                    print_or_output(str(gate_values[gate.id]), self.__output_file)
                    if i < len(self.__gates) - 1:
                        print_or_output(",", self.__output_file)
                else:
                    print_or_output(str(gate_values[gate.id]).ljust(len(gate.name) + 1), self.__output_file)
        print_or_output("", self.__output_file, False)

    def get_num_of_general_input_values(self):
        """Get the number of general input values.

        Keyword arguments:
        <None>
        """
        # Track the number of general input values.
        num_general_values = 0

        # Parse each gate to determine the maximum number of general input values.
        for gate in self.__gates:
            # Parse each gate input.
            for input in gate.input:
                # If the current input starts with an I, then get its general position.
                if input.startswith("I"):
                    # Get only the integer value of the general input value.
                    general_value = self.__get_int_of_general_value(input)
                    
                    # If its general position is greater than the current stored number of general values, then store that position.
                    if general_value + 1 > num_general_values:
                        num_general_values = general_value + 1

        # Return the number of general input values.
        return num_general_values

    def __get_int_of_general_value(self, general_value):
        """Get the integer component of the general value formatted I0, I1, etc.

        Keyword arguments:
        general_value -- General value formatted I0, I1, etc.
        """
        general_values = general_value.split("I")
        return int(general_values[1])

    def __are_all_gate_values_found(self, gate_values):
        """Check if all the gate values are found.

        This is using a developer-chosen definition of empty being ''.

        Keyword arguments:
        gate_values -- List of gate values
        """
        # Return False if any gate values are empty.
        for value in gate_values:
            if value == '':
                return False

        # Otherwise, return True.
        return True

    def __are_all_required_inputs_available(self, gate, gate_values):
        """Check if all the required inputs for the current gate are available.

        Keyword arguments:
        gate        -- Current logic gate
        combination -- List of general input values
        gate_values -- List of gate values
        """
        # Return False if any required gate values are empty.
        for input in gate.input:
            if not input.startswith("I"):
                if gate_values[int(input)] == '':
                    return False

        # Otherwise, return True.
        return True
        