def sort_on(dict):
    return dict["num"]

def get_sorted_list_by_char(chars_dict):
    new_list = []
    sorted_list = []

    for k, v in chars_dict.items():
        if k.isalpha():
            new_list.append({"char": k, "num": int(v)})
  
    new_list.sort(key=sort_on, reverse=True)
    return new_list


def get_character_count(text):
    char_with_count = {}

    for i, char in enumerate(text.lower()):
        if char in char_with_count:
            char_with_count[char] += 1
        else:
            char_with_count[char] = 1
   
    return char_with_count
            
def get_number_of_words(text):
    return len(text.split())
