with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    letters = {}
    for word in words:
        word = word.lower()
        for l in word:
            try:
                letters[l] += 1
            except:
                letters[l] = 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    sorted_letters = sorted(letters.items(), key=lambda x: x[0])
    for let, count in sorted_letters:
        if let.isalpha():
            print(f"The '{let}' character was found {count} times")

    print("--- End report ---")