def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

# Counts the number of each character in a string and stores the count in a dict. 

def get_num_char(text):
    char = {}

    for character in text:
        character_lower = character.lower()

        if character_lower in char:
            char[character_lower] += 1

        else: 
            char[character_lower] = 1

    return char

# Return a sorted list of dictionaries

def sort_dict(char_count_dict):

    char_list = []
    
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "num": count}) 
    
    char_list.sort(key=get_num_key, reverse=True)
    return char_list

# Return the "num" key for comparison 

def get_num_key(char_list):

    return char_list["num"]