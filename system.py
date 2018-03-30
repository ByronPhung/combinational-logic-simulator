#===================================================================================================================================
#  File        : system.py
#  Project     : Combinational Logic Simulator
#  Description : Handle basic system operations.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===================================================================================================================================

#===================================================================================================================================
#  Functions Definition
#===================================================================================================================================

def print_or_output(output, output_file=None, is_same_line=True):
    """Print to console or output to file.

    Keywords arguments:
    output       -- Output string
    is_same_line -- Determines if print should have newline or not
    output_file  -- Path to output file
    """
    if is_same_line:
        end_line = ""
    else:
        end_line = "\n"
    if output_file:
        print(output, end=end_line, file=open(output_file, "a"))
    else:
        print(output, end=end_line)

def read_file(file):
    """Read the raw content of a file.

    Keyword arguments:
    file -- File to read
    """
    file_content = open(file)
    return file_content.read()
    