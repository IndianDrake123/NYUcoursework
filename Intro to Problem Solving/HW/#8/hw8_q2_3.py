"""
Author: Brian Thomas 
Assignment / Part: HW8 - Q2, Q3 Of Code And Poetry & Now, let's make it presentable
Date due: November 16, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""

def is_haiku(haiku):
    syllable_amts = list()
    lines = haiku.split('/')
    for line in lines:
        syllables = line.count(',') + 1 
        syllable_amts.append(syllables)

    haiku_or_not = None
    if len(lines) == 3:
        if syllable_amts[0] == 5:
            haiku_or_not = True
        else:
            print('WARNING: The first line is not 5 syllables long.')
            haiku_or_not = False
        if syllable_amts[1] == 7:
            haiku_or_not = True
        else:
            print('WARNING: The second line is not 7 syllables long.')
            haiku_or_not = False
        if syllable_amts[2] == 5:
            haiku_or_not = True
        else:
            print('WARNING: The third line is not 5 syllables long.')
            haiku_or_not = False
    else:
        haiku_or_not = False

    return haiku_or_not

def haiku_string_parser(input_string):
    if is_haiku(input_string):
        haiku_str = str()
        lines = input_string.split('/')
        for line in lines:
            for char in line:
                if char != ',':
                    haiku_str += char
            haiku_str += '\n'
        
        return haiku_str.strip()
    else:
        return ""
    
def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon "
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)

main()
#"clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding,ha,bit/ga,zing,at ,the ,moon "
#"clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding,ha,bit/ga,zing "