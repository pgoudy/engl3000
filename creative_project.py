import random
import argparse
import os

def file_to_words(inputfile):
	textfile = open(inputfile)
	unparsed_text = textfile.read()
	parsed_text = str.split(unparsed_text)
	return parsed_text
	
def generate_tri_dictionary(parsed):
	parselen = len(parsed)
	wordpool = {}
	for i in range(parselen-2):
		key = (parsed[i].lower(), parsed[i+1].lower())
		if key in wordpool.keys():
			wordpool[key].append(parsed[i+2])
		else:
			wordpool[key] = [parsed[i+2]]
	return wordpool

def generate_quad_dictionary(parsed):
	parselen = len(parsed)
	wordpool = {}
	j = 0
	for i in range(parselen-3):
		key = (parsed[i].lower(), parsed[i+1].lower(), parsed[i+2].lower())
		if key in wordpool.keys():
			wordpool[key].append(parsed[i+3])
		else:
			wordpool[key] = [parsed[i+3]]
	return wordpool

def generate_penta_dictionary(parsed):
	parselen = len(parsed)
	wordpool = {}
	for i in range(parselen-4):
		key = (parsed[i].lower(), parsed[i+1].lower(), parsed[i+2].lower(), parsed[i+3].lower())
		if key in wordpool.keys():
			wordpool[key].append(parsed[i+4])
		else:
			wordpool[key] = [parsed[i+4]]
	return wordpool

def create_art(dictionary, n, length):
	start = random.randint(0, wordamt - n)
	poetry = []
	if n == 3:
		(first, second) = (parsed[start], parsed[start+1])
		for i in range(length):
			if first[-1] in ["!", "?", ";", ".", ":"]: #attempt to parse it better
				firstapp = first+"\n"
			else:
				firstapp = first+" "
			poetry.append(firstapp)
			(first, second) = (second, 
			random.choice(dictionary[(first.lower(), second.lower())]))
		print (''.join(poetry))
			
	if n == 4:
		(first, second, third) = (parsed[start], parsed[start+1], parsed[start+2])
		for i in range(length):
			if first[-1] in ["!", "?", ";", ".", ":"]:
				firstapp = first+"\n"
			else:
				firstapp = first+" "
			poetry.append(firstapp)
			(first, second, third) = (second, third, 
			random.choice(dictionary[
			(first.lower(), second.lower(), third.lower())]))
		print (''.join(poetry))
	if n == 5:
		(first, second, third, fourth) = (parsed[start], parsed[start+1], parsed[start+2], parsed[start+3])
		for i in range(length):
			if first[-1] in ["!", "?", ";", ".", ":"]:
				firstapp = first+"\n"
			else:
				firstapp = first+" "
			poetry.append(firstapp)
			(first, second, third, fourth) = (second, third, fourth, 
			random.choice(dictionary[
			(first.lower(), second.lower(), third.lower(), fourth.lower())]
			))
		print (''.join(poetry))
		
def continue_work():
	cont = str(input("Again? "))
	if cont.lower() in ["y", "yes", "t", "true"]:
		return True
	else:
		return False

def get_state():
	state = 0
	valid_states = ["3", "4", "5"]
	while True:
		try:
			state = int(input("Enter Search Depth: "))
		except ValueError:
			print("Try again. Options: " + str(valid_states))
			continue
		else:
			if (str(state) in valid_states):
				break
			print("Try again. Options: " + str(valid_states))
			continue
	return state
	
def get_amount():
	amount = 0
	while True:
		try:
			amount = int(input("Enter Length of String: "))
		except ValueError:
			print ("Try again. Invalid input.")
			continue
		else:
			if (amount <= 0):
				print("Try again. A number above 0 is required.")
				continue
			break
	return amount

def unique(dictionary, n):
	e=0
	k=0
	for i in dictionary.keys():
		if len(dictionary[i]) > 1:
			e=e+len(dictionary[i])
		if len(dictionary[i]) == 1:
			k = k+len(dictionary[i])
	print("Unique combinations of "+str(n)+" words: "+str(k)+" out of "+ str(e+k)
	+" ("+str(round((k/(e+k))*100, 3))+"%)")
	

def main():
	state = get_state()
	cont = True
	if state == 3:
		tri = generate_tri_dictionary(parsed)
		while (cont == True):
			amount = get_amount()
			create_art(tri, 3, amount)
			cont = continue_work()
	if state == 4:
		quad = generate_quad_dictionary(parsed)
		while (cont == True):
			amount = get_amount()
			create_art(quad, 4, amount)
			cont = continue_work()
	if state == 5:
		penta = generate_penta_dictionary(parsed)
		while (cont == True):
			amount = get_amount()
			create_art(penta, 5, amount)
			cont = continue_work()

def presentation():
	os.system('clear')
	tri = generate_tri_dictionary(parsed)
	quad = generate_quad_dictionary(parsed)
	penta = generate_penta_dictionary(parsed)
	input()
	create_art(tri, 3, 75)
	input()
	create_art(quad, 4, 75)
	input()
	create_art(penta, 5, 75)
	input()
	unique(tri, 3)
	unique(quad, 4)
	unique(penta,5)


def prelim():
	global wordamt
	global parsed

	inputfile = "shakespearetext.txt"
	parsed = file_to_words(inputfile)
	wordamt = len(parsed)
	random.seed()
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--presentation", help = "Enable Presentation Mode", action = "store_true")
	args = parser.parse_args()
	if args.presentation:
		presentation()
	else:
		main()
	

if __name__ == "__main__":
	prelim()
	
