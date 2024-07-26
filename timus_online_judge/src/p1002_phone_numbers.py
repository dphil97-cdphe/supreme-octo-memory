import sys
from io import StringIO

INPUT_PATH = "test_input.txt"

KEYPAD_DICT = {
      '1': ['i, j'],
      '2': ['a', 'b', 'c'],
      '3': ['d', 'e', 'f'],
      '4': ['g', 'h'],
      '5': ['k', 'l'],
      '6': ['m', 'n'],
      '7': ['p', 'r', 's'],
      '8': ['t', 'u', 'v'],
      '9': ['w', 'x', 'y'],
      '0': ['o', 'q', 'z']
  }


def digit_test(num):
"""Test if character is digit"""	
	try:
		int(num)
		return True
	except ValueError:
		return False

def create_phone_number_dict(phone_num):
"""Generate dictionary for letters per digit
in phone number"""	
	phone_num_dict = []

	for count, digit in enumerate(phone_num):

    	# need to have unique keys (duplicate numbers)
    	phone_num_digit_key = f"p{count}_" + digit

    	phone_num_dict += [phone]
    	phone_num_dict[phone_num_digit_key] = keypad_dict[digit]

  return phone_num_dict

def is_potential_word():
	pass

def check_word():
	pass

def update_phone_idx():
	pass

def parse_input(stream_in):
"""Generate chunk of data from stream
containing words and phone number"""	

	chunk_valid_words = []
	count_chunk_words = 0
	row_idx = 1

	with open(INPUT_PATH, "r") as input:
		
		line = input.readline().strip()

		# First row is phone number
		if row_idx == 0 and digit_test(line) and len(line) == 10:
			phone_num = line
			row_idx += 1 

		# Second row is count of words in message
		elif row_idx == 1 and digit_test(line):
			count_chunk_words = int(line)
			row_idx += 1

		# Chunk ends when we hit last word
		# this is the finished product to process
		elif (row_idx == words_in_d + 1):
			print(f'phone number: {phone_num}\nwords_in_d: {words_in_d}\nwords: {words}')

		    # Clear all chunk data
		    phone_num = ''
		    row_idx = 0
		    words_in_d = 0
		    words.clear()

		elif line == '-1':
			break

if __name__ == "__main__":
	parse_input(INPUT_PATH)