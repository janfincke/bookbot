def generate_report(letter_count_dict: dict, word_count: int, file_path: str):
    with open("report.txt", "w") as f:
        f.write(f"--- Begin report of {file_path} ---\n")
        f.write(f"{word_count} words found in the document\n")
        sorted_dict = dict(sorted(letter_count_dict.items(), key=lambda item: item[1], reverse=True))
        for letter, count in sorted_dict.items():
            f.write(f"The '{letter}' character was found {count} times\n")
        f.write(f"--- End report---\n")


def number_of_words(text: str):
    result = text.split()
    return len(result)

def count_characters(text: str):
    text = text.lower()
    result = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        result[letter] = 0
        for char in text:
            if char == letter:
                result[letter] += 1
    return result

def main():
    path = "books/frankenstein.txt"
    with open(path, encoding="utf-8") as f:
        contents = f.read()
        word_count = number_of_words(contents)
        letter_count_dict = count_characters(contents)
        generate_report(letter_count_dict, word_count, path)
main()