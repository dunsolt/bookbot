def word_count(book):
    text = book.split()
    num_words = 0
    for x in text:
        num_words += 1
    return num_words

def character_count(book):
    chars = {}
    for char in book.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(item):
    return item["num"]

def character_count_sorted(char_counts):
    items_list = []
    for char, count in char_counts.items():
        items_list.append({"char":char, "num":count})
    items_list.sort(reverse=True, key=sort_on)
    return items_list