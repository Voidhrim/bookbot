def main():
	book_path = "books/frankenstein.txt"

	book = open_file(book_path)
	wordcount = count_words(book)

	print(f"--- Begin report of {book_path} ---")
	print(f"{wordcount} words found in the document\n")

	letter_dict = count_characters(book)
	lettercount_list = convert_dict_to_listofdicts(letter_dict)
	lettercount_list.sort(reverse=True, key=sort_on)
	
	for item in lettercount_list:
		letter = item["letter"]
		count = item["count"]
		if letter.isalpha() == True:
			print(f"The '{letter}' character was found {count} times")

	print("--- End report ---")

	return

def open_file(path):
	with open(path) as f:
		return f.read()

def count_words(text):
	words = text.split()
	return len(words)
	
def count_characters(text):
	count_dict = {}
	
	for letter in text:
		letter = letter.lower()
		if letter in count_dict:
			count_dict[letter] += 1
		else:
			count_dict[letter]	= 1
	return count_dict

def convert_dict_to_listofdicts(dict):
	outputlist = []
	for key, value in dict.items():
		outputlist.append({"letter": key, "count": value})
	
	return outputlist
	
def sort_on(dict):
	# Only for the lettercount list-of-dictionaries
	return dict["count"]

main()