#===============================================================================
#  File        : system.py
#  Project     : Combinational Logic Simulator
#  Description : Handle basic system operations.
#  Company     : Cal Poly Pomona
#  Engineer    : Byron Phung
#===============================================================================

#===============================================================================
#  Functions Definition
#===============================================================================

def read_file(file):
    """Read the raw content of a file.

    Keyword arguments:
    file -- File to read
    """
    file_content = open(file)
    return file_content.read()