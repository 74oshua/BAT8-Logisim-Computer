# load A and B reg with 1
lda #01
ldb #01

>next_num
# store old A val at $80
sta $80

# add A and B
add b

# show output
sta $C0

# load old A into B
ldb $80
jmp >next_num