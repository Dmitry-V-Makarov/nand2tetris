// Adds up two numbers
// RAM[2] = RAM[0] + RAM[1]
// Usage: put the values that you wish to add
// in RAM[0] and RAM [1]

	@0 // Put RAM[0] in D
	D=M

	@1 // Add up RAM[0] and RAM[1] and store the result in D
	D=D+M

	@2 // Store the result in RAM[2]
	M=D