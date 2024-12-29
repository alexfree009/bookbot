

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_count = character_count(file_contents)
        word_count = 0
        words = file_contents.split()
        for word in words:
            word_count += 1
        print(f"Word Count: {word_count}")
        print(f"Character Count: {char_count}")

def character_count(file_contents):
    char_count = {}
    for c in file_contents:
        character = c.lower()
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count
    
main()



