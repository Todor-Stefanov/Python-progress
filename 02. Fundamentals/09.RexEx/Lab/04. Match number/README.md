Write a program that finds all integer and floating-point numbers in a string.
Compose the Regular Expression
A number has the following characteristics:
•	Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind). The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".
•	The number might or might not be negative, so it might have a hyphen on its left side ("-").
•	It consists of one or more digits.
•	Might or might not have digits after the decimal point
•	The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
•	Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead). The syntax for the end of the RegEx might look someth

You can follow the table below to help with composing your RegEx:
Match ALL of these	Match NONE of these
1 -1 123 -123 123.456 -123.456	1s s2 s-s -1- _55_ s-2 s-3.5 s-1.1 00.5
Find all the numbers from the string and print them on the console, separated by spaces.
