// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Pseudo code

// times = R1 - if negative change to positive
// number = R0 - if R1 negative change the sign
// product = 0
// R2 = 0
// i = 0

// LOOP
// if 
// times - i = 0 goto STOP:
// else
// product = product + number
// i = i + 1
// goto LOOP

// STOP
// R2 = product




// set basic variables

	@product
	M=0 // product = 0

	@i
	M=0 // i=0

	@R2
	M=0 // R2 = 0

// set R0 to @number and R1 to @times

	@R0
	D=M // D=RAM[0]

	@number
	M=D // set RAM[0] to @number

	@R1
	D=M // D=RAM[1]
	
	@times
	M=D // set RAM[1] to @times

// check if @times is negative

	@times
	D=M // D=RAM[1]

	@NEGATIVE
	D;JLT // if @times is negative goto NEGATIVE

	@LOOP
	D;JGE // if @times is positive or 0 goto LOOP

// change signs if R1 is negative

(NEGATIVE)

	@number
	D=M
	M=-D // set @number to -@number
	
	@times
	D=M
	M=-D // set @times to -@times

(LOOP)
	@i
	D=M
	@times
	D=M-D
	@STOP
	D,JEQ // if times = 0 goto STOP

	@number
	D=M
	@product
	M=M+D // product = product + number
	@i
	M=M+1 // i = i + 1
	@LOOP
	0; JMP

(STOP)
	@product
	D=M
	@R2
	M=D // RAM[2] = product

(END)
	@END
	0; JMP