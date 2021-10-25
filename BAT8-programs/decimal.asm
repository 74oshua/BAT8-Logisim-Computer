lda #00
ldb #00

sta $80
stb $81

>inc
lda $80
add #01
sta $80

cmp #0A
jcc >show

>of_a
lda #00
sta $80

lda $81
add #01
sta $81

cmp #0A
jcc >show

lda #00
sta $81

>show
lda $81
ldb $81

add b
sta $82
ldb $82
add b
sta $82
ldb $82
add b
sta $82
ldb $82
add b

ldb $80
add b
sta $C0

jmp >inc