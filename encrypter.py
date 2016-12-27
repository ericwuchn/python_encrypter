# python encrypter/ decrypter
# by Jiayue Wu

def main():
	text_list = []
	encrypt_list = []
	decrypt_list = []
	function_choice = 0
	print("\nPython Encrypter/ Decrypter\nby Jiayue Wu\n")
	while function_choice != "1" and function_choice != "2":
		print("Please choose a function:")
		print("[1] Encrypt")
		print("[2] Decrypt")
		function_choice = str(input())

	if function_choice == "1":
		text_input = input("\nPlease input the message you want to encrypt (letter & number & space only):\n")
		text_list = list(text_input)
		for index in text_list:
			encrypt_list.append(encrypt(index))
		print("\nThe encrypted message is:")
		print("".join(encrypt_list))

	if function_choice == "2":
		text_input = input("\nPlease input the message you want to decrypt (letter & number & space only):\n")
		text_list = [text_input[i:i+2] for i in range(0, len(text_input), 2)]
		for index in text_list:
			decrypt_list.append(decrypt(index))
		print("\nThe decrypted message is:")
		print("".join(decrypt_list))

def encrypt(index):
	# encrypter
	if index == "a":
		return "23"
	if index == "b":
		return "24"
	if index == "c":
		return "25"
	if index == "d":
		return "26"
	if index == "e":
		return "27"
	if index == "f":
		return "28"
	if index == "g":
		return "29"
	if index == "h":
		return "30"
	if index == "i":
		return "31"
	if index == "j":
		return "32"
	if index == "k":
		return "33"
	if index == "l":
		return "22"
	if index == "m":
		return "21"
	if index == "n":
		return "20"
	if index == "o":
		return "19"
	if index == "p":
		return "18"
	if index == "q":
		return "17"
	if index == "r":
		return "16"
	if index == "s":
		return "15"
	if index == "t":
		return "14"
	if index == "u":
		return "13"
	if index == "v":
		return "12"
	if index == "w":
		return "11"
	if index == "x":
		return "10"
	if index == "y":
		return "09"
	if index == "z":
		return "08"
	if index == " ":
		return "07"
	if index == "1":
		return "(("
	if index == "2":
		return "))"
	if index == "3":
		return "!@"
	if index == "4":
		return "@!"
	if index == "5":
		return "*@"
	if index == "6":
		return "&*"
	if index == "7":
		return "$("
	if index == "8":
		return ")("
	if index == "9":
		return "$$"
	if index == "0":
		return "!!"
	if index == "A":
		return "93"
	if index == "B":
		return "94"
	if index == "C":
		return "95"
	if index == "D":
		return "96"
	if index == "E":
		return "97"
	if index == "F":
		return "98"
	if index == "G":
		return "99"
	if index == "H":
		return "00"
	if index == "I":
		return "01"
	if index == "J":
		return "02"
	if index == "K":
		return "03"
	if index == "L":
		return "82"
	if index == "M":
		return "81"
	if index == "N":
		return "80"
	if index == "O":
		return "79"
	if index == "P":
		return "78"
	if index == "Q":
		return "77"
	if index == "R":
		return "76"
	if index == "S":
		return "75"
	if index == "T":
		return "74"
	if index == "U":
		return "73"
	if index == "V":
		return "72"
	if index == "W":
		return "71"
	if index == "X":
		return "70"
	if index == "Y":
		return "69"
	if index == "Z":
		return "68"

def decrypt(index):
	# decrypter
	if index == "23":
		return "a"
	if index == "24":
		return "b"
	if index == "25":
		return "c"
	if index == "26":
		return "d"
	if index == "27":
		return "e"
	if index == "28":
		return "f"
	if index == "29":
		return "g"
	if index == "30":
		return "h"
	if index == "31":
		return "i"
	if index == "32":
		return "j"
	if index == "33":
		return "k"
	if index == "22":
		return "l"
	if index == "21":
		return "m"
	if index == "20":
		return "n"
	if index == "19":
		return "o"
	if index == "18":
		return "p"
	if index == "17":
		return "q"
	if index == "16":
		return "r"
	if index == "15":
		return "s"
	if index == "14":
		return "t"
	if index == "13":
		return "u"
	if index == "12":
		return "v"
	if index == "11":
		return "w"
	if index == "10":
		return "x"
	if index == "09":
		return "y"
	if index == "08":
		return "z"
	if index == "07":
		return " "
	if index == "((":
		return "1"
	if index == "))":
		return "2"
	if index == "!@":
		return "3"
	if index == "@!":
		return "4"
	if index == "*@":
		return "5"
	if index == "&*":
		return "6"
	if index == "$(":
		return "7"
	if index == ")(":
		return "8"
	if index == "$$":
		return "9"
	if index == "!!":
		return "0"
	if index == "93":
		return "A"
	if index == "94":
		return "B"
	if index == "95":
		return "C"
	if index == "96":
		return "D"
	if index == "97":
		return "E"
	if index == "98":
		return "F"
	if index == "99":
		return "G"
	if index == "00":
		return "H"
	if index == "01":
		return "I"
	if index == "02":
		return "J"
	if index == "03":
		return "K"
	if index == "82":
		return "L"
	if index == "81":
		return "M"
	if index == "80":
		return "N"
	if index == "79":
		return "O"
	if index == "78":
		return "P"
	if index == "77":
		return "Q"
	if index == "76":
		return "R"
	if index == "75":
		return "S"
	if index == "74":
		return "T"
	if index == "73":
		return "U"
	if index == "72":
		return "V"
	if index == "71":
		return "W"
	if index == "70":
		return "X"
	if index == "69":
		return "Y"
	if index == "68":
		return "Z"

main()