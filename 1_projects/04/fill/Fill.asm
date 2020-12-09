// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(RESTART)

	@8192
	D=A // sets the value 8192 to D
	@n
	M=D // n=8192

	@SCREEN
	D=A, sets the value (not the content which can be -1, for example) 16384 to D
	@address
	M=D // address = 16384 (base address of the Hack screen)

	@i
	M=0 // i=0

(LOOP)
	@n
	D=M
	@i
	D=D-M
	@RESTART
	D; JEQ // if @n - @i = 0 goto RESTART

	@KBD
	D=M // check keyboard

	@WHITE
	D;JEQ // if @KBD is 0 goto WHITE

	@BLACK
	D;JNE // if @KBD is not 0 got BLACK

(WHITE)

	@address
	A=M
	M=0 // RAM (address) = 0 (16 pixels)
	
	@END
	0;JMP // goto END


(BLACK)

	@address
	A=M
	M=-1 // RAM (address) =-1 (16 pixels)
	
	@END
	0;JMP // goto END

(END)

	@address
	M=M+1 // address = address + 1
	
	@i
	M=M+1 // i=i+1
	
	@LOOP
	0;JMP // goto LOOP