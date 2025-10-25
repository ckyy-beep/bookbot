def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    text = text.lower()

    for i in text:
        if i in char_dict:
            char_dict[i] += 1
        else :
            char_dict[i] = 1

    return char_dict

def sort_on(item):
    return item["num"]

def sort_characters(char_counts):
    char_list = []

    # Convert dictionary into a list of smaller dictionaries
    for char in char_counts:
        char_list.append({"char": char, "num": char_counts[char]})

    char_list.sort(reverse=False, key=sort_on)

    return char_list
