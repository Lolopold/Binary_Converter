#Binary-Generator by Lolopold_ (https://github.com/Lolopold)
#I'm still learning to code and I'd love to hear your feedback or even recomendations.
#This is my programming journey
#I hope someone can use this (although I strongly doubt it)
#XOXO


#import libraries
import colorama
from colorama import Fore, Style

#define the two operations of script
def alph_to_bin():
	alph_to_bin={
		" ": 1011111,
		"A": 1000001,
		"B": 1000010,
		"C": 1000011,
		"D": 1000100,
		"E": 1000101,
		"F": 1000110,
		"G": 1000111,
		"H": 1001000,
		"I": 1001001,
		"J": 1001010,
		"K": 1001011,
		"L": 1001100,
		"M": 1001101,
		"N": 1001110,
		"O": 1001111,
		"P": 1010000,
		"Q": 1010001,
		"R": 1010010,
		"S": 1010011,
		"T": 1010100,
		"U": 1010101,
		"V": 1010110,
		"W": 1010111,
		"X": 1011000,
		"Y": 1011001,
		"Z": 1011010,
		"_": 1011111,
		"a": 1100001,
		"b": 1100010,
		"c": 1100011,
		"d": 1100100,
		"e": 1100101,
		"f": 1100110,
		"g": 1100111,
		"h": 1101000,
		"i": 1101001,
		"j": 1101010,
		"k": 1101011,
		"l": 1101100,
		"m": 1101101,
		"n": 1101110,
		"o": 1101111,
		"p": 1110000,
		"q": 1110001,
		"r": 1110010,
		"s": 1110011,
		"t": 1110100,
		"u": 1110101,
		"v": 1110110,
		"w": 1110111,
		"x": 1111000,
		"y": 1111001,
		"z": 1111010,
	}
	print("Enter The Word You Want To Convert To Binary:")
	letters=str(input())
	for letter in letters:
		if letter in alph_to_bin:
			print(Fore.RED+str(alph_to_bin[letter]))	
		else:
			print("\nNo Binary Representation Found For Letter(s):", Fore.BLUE+str(letter))
			print(Style.RESET_ALL)
def num_to_bin():
	print("Enter The Number You Want To Convert To Binary:")
	try:
		number = input()
		binary = []
		while number != 0:
			binary.append(int(number) % 2)
			number = int(number) // 2
		binary.reverse()
		binarys = "".join(str(bit)for bit in binary)
		print(Fore.RED+str(binarys))
	except ValueError:
		print("\nNo Binary Representation Found For Number(s):", (Fore.BLUE+str(number)))
		print(Style.RESET_ALL)
		pass

#actual beginning of the script
print(Fore.YELLOW+"Welcome To The Binary Converter. \n")
print(Style.RESET_ALL)
try:
	print("Do You Want To Convert Text To Binary",Fore.BLUE+"(1)",Style.RESET_ALL,"Or Convert Numbers To Binary",Fore.BLUE+"(2)",Style.RESET_ALL,":")
	choice=input("1 Or 2:	")
	choice=int(choice)
	if int(choice) == 1:
		alph_to_bin()
	elif int(choice) == 2:
		num_to_bin()
	else:
		print("Try Again. Number Must Be In Range",Fore.BLUE + "1-2")
		print(Style.RESET_ALL)
except ValueError:
	pass
	print("This In Not A Number:",Fore.BLUE + str(choice))
	print(Style.RESET_ALL)
print(Style.RESET_ALL)

#be polite and say bye!
input("Okay, bye...")

