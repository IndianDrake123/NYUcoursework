"""
Author: Brian Thomas 
Assignment / Part: HW7 - Q3 Damage Report
Date due: November 9, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def create_error_log(sequence, filename) -> bool:
    erorr_log = open('error_log.txt', 'w')
    length = len(sequence)
    line = 1
    try:
        indices = open(filename, 'r')
    
    except FileNotFoundError:
        erorr_log.write('FileNotFoundError: The file specified was not found or could not be opened.')
        return False
    
    for line in indices:
        try:
            num = int(line)
            sequence[num]

        except IndexError:
            erorr_log.write(f"IndexError at LINE {line}: The value read, '{line.rstrip()}', is larger than the sequence length of {length}.\n")

        except ValueError:
            erorr_log.write(f"ValueError at LINE {line}: The value read, '{line.rstrip()}', cannot be casted into an integer to be used as an index.\n")
        
        line += 1

    indices.close()
    erorr_log.close()
    
    return True