import sys
from stats import parse_book_text, count_characters, parse_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

path = sys.argv[1]
book_text = get_book_text(path)
num_words = parse_book_text(book_text)
dict_characters = count_characters(book_text)
list_dicts = parse_dict(dict_characters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for dict in list_dicts:
    if dict["character"].isalpha():
        print(f"{dict['character']}: {dict['amount']}")
print("============= END ===============")