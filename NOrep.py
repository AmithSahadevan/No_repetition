Input = input("Enter a phrase: ")	#Taking in input.

lizt = list(Input)	#Convering Input into a list and storing it in a variable called lizt.

dictionary = dict.fromkeys(lizt)	#Converting the above list into a dictionary.

back_to_list = list(dictionary)	#Converting the above dictionary back to list.

for letters in back_to_list: # looping thru the letters in the list.

	print(letters, end = "")	#Printing out the letters one by one from the list, but in a single line.

print("")	#Just for adding a bit of final touch..Yeah, that's it.