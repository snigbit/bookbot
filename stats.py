
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def get_chars_dic(text):
    char_dic = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dic:
            char_dic[lower_char] += 1
        else:
            char_dic[lower_char] = 1
    
    return char_dic

def sort_on(items):
    return items["num"]

def get_sorted_chars_list(chars_dic):
    chars_list = []
    for key in chars_dic:
        char_dic = {"char" : key, "num" : chars_dic[key]}
        chars_list.append(char_dic)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


