import sys
import argparse

# instruction dict
def get_code(x):
    return {
        "lda #": 0x01,
        "lda $": 0x02,
        "ldb #": 0x03,
        "ldb $": 0x04,
        "sta $": 0x05,
        "stb $": 0x06,
        "add #": 0x07,
        "add b": 0x08,
        "jmp $": 0x09,
        "jmp >": 0x09,
        "jcs $": 0x0A,
        "jcs >": 0x0A,
        "jcc $": 0x0B,
        "jcc >": 0x0B,
        "jeq $": 0x0C,
        "jeq >": 0x0C,
        "jne $": 0x0D,
        "jne >": 0x0D,
        "cmp #": 0x0E,
        "cmp b": 0x0F
    }.get(x, 0x00)

def find_label(ins, pos, jtable):
    npos = pos
    if len(ins) == 0 or ins[0] == "#":
        return npos

    if ins[0] == ">":
        jtable.append((ins[1:], npos))
        return npos
    
    npos += 1
    if len(ins) <= 5:
        return npos
    
    npos += 1
    return npos

def compile_ins(file, ins, pos, jtable):
    npos = pos
    if len(ins) == 0 or ins[0] == "#":
        return npos

    if ins[0] == ">":
        return npos
    
    file.write(bytes([get_code(ins[0:5])])[0:1])
    npos += 1
    if len(ins) <= 5:
        return npos

    if ins[4] == ">":
        for (n, p) in jtable:
            if (n) == ins[5:]:
                file.write(bytes([p])[0:1])
                npos += 1
                break
        return npos
    
    op = int(ins[5:], 16)
    if op < 0:
        op += 0x100
    file.write(bytes([op])[0:1])
    npos += 1
    return npos

# parse arguments
parser = argparse.ArgumentParser(
    description="assembler for 74oshua's BAT8 CPU")
parser.add_argument("output", type=str, help="output file path")
parser.add_argument("source", type=str, help="assembly source code file path")

parsed_args = parser.parse_args()

out = open(parsed_args.output, "wb")
source = open(parsed_args.source, "r")

ins = source.read().split("\n", 128)

pc = 0
labels = []

# fill jump table
for i in ins:
    pc = find_label(i, pc, labels)

pc = 0
for i in ins:
    pc = compile_ins(out, i, pc, labels)

out.close()