string=input("Enter String: ")

vowels = 0
consonant = 0
specialChar = 0
digit = 0
for i in range(0, len(string)):
	ch = str[i]
	if ch.isalpha():
		if (ch == 'a' or ch == 'e' or ch == 'i'or ch == 'o' or ch == 'u'):
			vowels += 1
		else:
			consonant += 1
	
	elif ch.isdigit():
		digit += 1
	else:
		specialChar += 1
	
print("Vowels:", vowels)
print("Consonant:", consonant)
print("Digit:", digit)
print("Special Character:", specialChar)