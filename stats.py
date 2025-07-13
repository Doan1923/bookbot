def get_word_count(text):
        words = text.split()
        return len(words)
def get_char_count(text):
        text = text.lower()

        char_counts = {}

        for char in text:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return char_counts

def sort_char(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
      
def sort_on(item):
    return item["num"]
                
                
