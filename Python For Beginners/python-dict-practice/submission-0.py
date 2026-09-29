from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char_dict = {}
    for ch in word:
        value = char_dict.get(ch)
        if value is None:
            char_dict[ch] = 1
        else:
            char_dict[ch] = value + 1
    return char_dict





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
