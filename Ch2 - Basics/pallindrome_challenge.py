import string


#
# word = input("Please enter a string to test for Pallindrome or 'exit' to quit: ")
#
# while word != "exit":
# 	word = word.replace(" ", "")
# 	for char in string.punctuation:
# 		word = word.replace(char, "")
# 	word = word.lower()
# 	reversed_word = ""
# 	for char in word:
# 		reversed_word = char + reversed_word
#
# 	if (word == reversed_word):
# 		print(word, "is a pallindrome")
# 	else:
# 		print(word, "is not a pallindrome")
# 	word = input("Please enter a string to test for Pallindrome or 'exit' to quit: ")

#######################################


def get_string():
	word = input("Please enter a string to test for Pallindrome or 'exit' to quit: ")
	if word != "exit":
		convertString(word)


def checkPallindrome(reversed_word, word):
	if word == word[::-1]:
		print(word, "is a pallindrome")
	else:
		print(word, "is not a pallindrome")
	get_string()


def reverse_word(word):
	reversed_word = ""
	for char in word:
		reversed_word = char + reversed_word
	checkPallindrome(reversed_word, word)


def convertString(word):
	word = word.replace(" ", "")
	for char in string.punctuation:
		word = word.replace(char, "")
	word = word.lower()
	reverse_word(word)


get_string()


