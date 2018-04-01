# Combinational Logic Simulator

This simple Python script takes an input file containing the gates and input logic of a combinational logic circuit and generates a truth table of all the possible combinations for either a selected or all gates.

## Requirements

To run this script, you will need the following:
* [Python 3](https://www.python.org/downloads/)

## Execution

### Preparing a Circuit File

Circuit files consist of 4 space-separated columns referencing the following: gate ID, gate name, gate type, and space-separated gate inputs.

#### Gate ID

Gate IDs can be any integer of your choice. The convention is to start from 0 and number upwards.

General rule of thumb is to select numbers that are easy for you to reference because if a gate has an input from another gate, then you will need to specify that gate's ID in the gate input column.

Examples: 0, 1, 2, 3, 4, etc.

#### Gate Name

Gate names can be any single-word (no spaces) names of your choice. The convention is to just have the gate type + a number label. This input is case-insensitive.

Examples: carry, XOR1, and2

#### Gate Type

Gate types can be any of the following supported types:
* NOT
* OR
* AND
* XOR
* NAND
* NOR
* XNOR

This column is case-insensitive.

#### Gate Inputs

This is a space-separated list referencing gate inputs.

You have 2 types of inputs available to use:
1. Raw input
2. Gate input

Raw inputs are actual bit inputs that determine the combinations for your truth table. This input begins with the letter "I" (eye) followed by an input number starting from 0.

This input is case-insensitive.

Examples: I0, i1, I2, i3, etc.

Gate inputs are strictly the gate IDs you define in the first column of every row.

For example, if you want to use a gate that you labelled with ID 2 for an input into another gate, then you simply input "2".

#### Full Example

Here's an example circuit file that represents a full adder.

```
5    carry    OR     2     3    4
0    xor1     Xor    i0    i1
2    and2     AnD    I0    I2
3    AND1     AND    i0    I1
4    AND3     AND    i1    I2
1    sum      xor    0     I2
```

### Command Line

This is a command-line only tool. Once executed, the tool should walk you through instructions as you use it.

```
python main.py [OPTIONS...] path\to\circuit_file.in
```

If you are still unsure and need help, please don't hesitate to reach out here on GitHub.

#### Supported Command-Line Options

| Option     | Argument            | Description                                                                |
| ---------- | ------------------- | -------------------------------------------------------------------------- |
| -h, --help | None                | Shows the help menu.                                                       |
| -o, --out  | path/to/output_file | Outputs truth table to the specified file instead of printing to console. |

#### Example Execution

Using circuits/fulladder-sample1.in:

```
5    carry    OR     2     3    4
0    xor1     Xor    i0    i1
2    and2     AnD    I0    I2
3    AND1     AND    i0    I1
4    AND3     AND    i1    I2
1    sum      xor    0     I2
```

Output:

```
> python main.py D:\combinational-logic-simulator\circuits\fulladder-sample1.in
INFO::  Printing gates in circuit...

ID      Name            Type    Inputs
--------------------------------------------------------------------------------
0       XOR1            XOR     I0     I1
1       SUM             XOR     0      I2
2       AND2            AND     I0     I2
3       AND1            AND     I0     I1
4       AND3            AND     I1     I2
5       CARRY           OR      2      3      4

INFO::  Use spaces to select multiples (e.g., 1 4 6).
INFO::  To calculate all gates, just press 'Enter' without inputting anything.
INPUT:: Select gates: 0 1 4
INFO::  Validating selected outputs...
INFO::  Printing truth table for selected outputs...
        This may take awhile for large numbers of inputs because of 2^n combinations...
        Total Combinations: 8

I0 I1 I2 XOR1 SUM AND3
0  0  0  0    0   0
0  0  1  0    1   0
0  1  0  1    1   0
0  1  1  1    0   1
1  0  0  1    1   0
1  0  1  1    0   0
1  1  0  0    0   0
1  1  1  0    1   1
```

## Changelog

* v1.1.1
  - Updated instructions in main.py.
  - Cleaned up some text formatting throughout the tool.
  - Updated README to reflect text & formatting changes.
* v1.1.0
  - Fixed memory limit issue for circuits with large amounts of input.
    * Note: This was tested with a 36-input, 159 gate circuit. You may still run into a memory limit issue for extremely large circuits, but I still applied a fix to significantly increase this limit.
  - Changed circuit input to be required command-line position argument.
  - Implemented support for outputting truth table to file instead of printing to console.
  - Cleaned up column whitespaces to match width of column names.
  - Added this README to finally document everything!
* v1.0.0
  - First release.

## License

MIT © [Byron Phung](https://www.byronphung.com)