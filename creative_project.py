import random

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
            print(i)
        else:
            wordpool[key] = [parsed[i+2]]
            print (i)
    return wordpool

def generate_quad_dictionary(parsed):
    parselen = len(parsed)
    wordpool = {}
    for i in range(parselen-3):
        key = (parsed[i].lower(), parsed[i+1].lower(), parsed[i+2].lower())
        if key in wordpool.keys():
            wordpool[key].append(parsed[i+3])
            print (i)
        else:
            wordpool[key] = [parsed[i+3]]
            print (i)
    return wordpool

def generate_penta_dictionary(parsed):
    parselen = len(parsed)
    wordpool = {}
    for i in range(parselen-4):
        key = (parsed[i].lower(), parsed[i+1].lower(), parsed[i+2].lower(), parsed[i+3].lower())
        if key in wordpool.keys():
            wordpool[key].append(parsed[i+4])
            print (i)
        else:
            wordpool[key] = [parsed[i+4]]
            print (i)
    return wordpool

def create_art(dictionary, n, length):
    random.seed()
    start = random.randint(0, wordamt - n)
    poetry = []
    if n == 3:
        (first, second) = (parsed[start], parsed[start+1])

        for i in range(length):
            poetry.append(first)
            (first, second) = (second, random.choice(dictionary[(first.lower(), second.lower())]))
        print (' '.join(poetry))
            
    if n == 4:
        (first, second, third) = (parsed[start], parsed[start+1], parsed[start+2])
        for i in range(length):
            poetry.append(first)
            (first, second, third) = (second, third, random.choice(dictionary[(first.lower(), second.lower(), third.lower())]))
        print (' '.join(poetry))
    if n == 5:
        (first, second, third, fourth) = (parsed[start], parsed[start+1], parsed[start+2], parsed[start+3])
        for i in range(length):
            poetry.append(first)
            (first, second, third, fourth) = (second, third, fourth, random.choice(dictionary[(first.lower(), second.lower(), third.lower(), fourth.lower())]))
        print (' '.join(poetry))
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

def main():
    state = get_state()
    cont = True
    if state == 3:
        tri = generate_tri_dictionary(parsed)
        while (cont == True):
            amount = get_amount()
            cont = create_art(tri, 3, amount)
    if state == 4:
        quad = generate_quad_dictionary(parsed)
        while (cont == True):
            amount = get_amount()
            cont = create_art(quad, 4, amount)
    if state == 5:
        penta = generate_penta_dictionary(parsed)
        while (cont == True):
            amount = get_amount()
            cont = create_art(penta, 5, amount)

def prelim():
    global wordamt
    global parsed

    inputfile = "shakespear_ebooks.txt"
    parsed = file_to_words(inputfile)
    wordamt = len(parsed)

if __name__ == "__main__":
    prelim()
    main()
