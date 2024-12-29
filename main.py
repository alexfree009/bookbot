

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_count = character_count(file_contents)
        sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
        word_count = 0
        words = file_contents.split()
        for word in words:
            word_count += 1
        print_report(word_count, sorted_char_count)

def character_count(file_contents):
    char_count = {}
    for c in file_contents:
        character = c.lower()
        if character.isalpha():
            if character in char_count:
                char_count[character] += 1
            else:
                char_count[character] = 1
    return char_count

def print_report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print(" ")
    for char, count in char_count.items():
        print(f"The {char} character was found {count} times")
    print("--- End report ---")

main()



