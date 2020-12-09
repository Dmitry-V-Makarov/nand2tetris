import re

def get_bin(x, bits=0):
    """
    Get the binary representation of x.

    Parameters
    ----------
    x : int
    bits : int
        Minimum number of digits. If x needs less digits in binary, the rest
        is filled with zeros.

    Returns
    -------
    str
    """
    return format(x, 'b').zfill(bits)

# create a dictionariy with predefined symbols
symb = { 'R0' : 0 , 'R1' : 1 , 'R2' : 2 , 'R3' : 3 , 'R4' : 4 , 'R5' : 5 , 'R6' : 6 , 'R7' : 7 , 'R8' : 8 , 'R9' : 9 , 'R10' : 10 , 'R11' : 11 , 'R12' : 12 , 'R13' : 13 , 'R14' : 14 , 'R15' : 15 , 'SCREEN' : 16384 , 'KBD' : 24576 , 'SP' : 0 , 'LCL' : 1 , 'ARG' : 2 , 'THIS' : 3 , 'THAT' : 4 }

# create a dictionary with comp instructions
ctable = { '0' : '0101010' , '1' : '0111111' , '-1' : '0111010' , 'D' : '0001100' , 'A' : '0110000' , '!D' : '0001101' , '!A' : '0110001' , '-D' : '0001111' , '-A' : '0110011' , 'D+1' : '0011111' , 'A+1' : '0110111' , 'D-1' : '0001110' , 'A-1' : '0110010' , 'D+A' : '0000010' , 'D-A' : '0010011' , 'A-D' : '0000111' , 'A&D' : '0000000' , 'D|M' : '0010101' , 'M' : '1110000' , '!M' : '1110001' , '-M' : '1110011' , 'M+1' : '1110111' , 'M-1' : '1110010' , 'D+M' : '1000010' , 'D-M' : '1010011' , 'M-D' : '1000111' , 'D&M' : '1000000' , 'D|M' : '1010101' }

# create a dictionary with dest instructions
dtable = { 'M' : '001' , 'D' : '010' , 'MD' : '011' , 'A' : '100' , 'AM' : '101' , 'AD' : '110' , 'AMD' : '111' }

# create a dictionary with jump instructions
jtable = { 'JGT' : '001' , 'JEQ' : '010' , 'JGE' : '011' , 'JLT' : '100' , 'JNE' : '101' , 'JLE' : '110' , 'JMP' : '111' }


# open .asm file
fname = input('Enter file: ')
if len(fname) < 1 : fname = 'Max.asm'
hand = open(fname)
hand2 = open(fname)

#create and open a file with the same name and .hack extension
hackfile = re.findall('([^ ]+)\.', fname)
hackfile = hackfile[0]
outF = open(hackfile + ".hack", "w")

count = 0

# add labels to the symbols dictionary
for line in hand:
    # eliminate empty lines and new line comments
    line = line.rstrip()
    if len(line) < 1 : continue
    if re.search('^//', line) : continue

    # look for label declarations
    if re.search('^\(', line) :
        label = re.findall('\(([^ ]*)\)', line)
        label = label[0]
        if label not in symb :
            symb[label] = count #there is a counting error
            continue
    count = count + 1

    #print(line)

#print(symb)

n = 16

# look for variables, add new variables to dictionnary, replace them with digits 
for line2 in hand2:
    # eliminate empty lines, new line comments and variables
    line2 = line2.rstrip()
    if len(line2) < 1 : continue
    if re.search('^//', line2) : continue
    if re.search('^\(', line2) : continue

    # variable A-instruction
    if re.search(r'^\s*@\D', line2) :
        var = re.findall('@([^ ]*)', line2)
        var = var[0]

        #if variable is in dictionary
        if var in symb :
            z = symb[var]

            # translate n into binary
            abin = get_bin(z, bits=15)
            abin = "0" + abin
            print(abin)
            outF.write(abin)
            outF.write("\n")

        
        #if variable is not in dictionary
        else :
            symb[var] = n

            #translate n into binary
            abin = get_bin(n, bits=15)
            abin = "0" + abin
            print(abin)
            outF.write(abin)
            outF.write("\n")

            n = n + 1

    # digit A-instruction
    if re.search(r'^\s*@\d', line2) :
        var = re.findall('@([^ ]*)', line2)
        var = int(var[0])

        #translate digit into binary
        abin = get_bin(var, bits=15)
        abin = "0" + abin
        print(abin)
        outF.write(abin)
        outF.write("\n")

    # C-instruction
    if not re.search(r'^\s*@', line2) :

        #find destination bits before "=", spaces ignored
        if re.search(r'([^ ]+)=', line2) :
            dest = re.findall('([^ ]+)=', line2)
            dest = dest[0]
            if dest in dtable :
                dinstruction = dtable[dest]
        else :
            dinstruction = '000'

        #find computation bits after "="
        if re.search(r'=([^ ]+)', line2) :
            comp = re.findall('=([^ ]+)', line2)
            comp = comp[0]
            if comp in ctable :
                cinstruction = ctable[comp]

        #find computation bits before ";"
        if re.search(r'([^ ]+);', line2) :
            comp = re.findall('([^ ]+);', line2)
            comp = comp[0]
            if comp in ctable :
                cinstruction = ctable[comp]

        #find jump bits after ";"
        if re.search(r';([A-Z]+)', line2) :
            jump = re.findall(';([A-Z]+)', line2)
            jump = jump[0]
            if jump in jtable :
                jinstruction = jtable[jump]
        else :
            jinstruction = '000'

        instruction = '111' + cinstruction + dinstruction + jinstruction
        print(instruction)
        outF.write(instruction)
        outF.write("\n")

outF.close()