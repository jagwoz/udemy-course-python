text = "[ 1 2 , 33 2² , 四 ], the German letter ß is equivalent to ss"

if __name__ == "__main__":
    # original text
    print(f"text => { text } \n")

    # text.capitalize() - first character uppercase, other lowercase
    text_transform = text.capitalize()
    print(f"text.capitalize() => { text_transform }")

    # text.capitalize() - first character in each word to uppercase, other lowercase
    text_transform = text.title()
    print(f"text.title() => { text_transform }")

    # text.lower() - each characters to lowercase
    # text.casefold() - each characters to lowercase, only standard ASCII (simple 26 letters)
    text_transform = text.casefold()
    print(f"text.casefold() => { text_transform }")
    text_transform = text.lower()
    print(f"text.lower() => { text_transform }")

    # text.upper() - each characters to lowercase
    text_transform = text.upper()
    print(f"text.upper() => { text_transform }")

    # text.center(width, fillchar) - string filled with the given fillchar with the given text in the middle
    text_transform = (text.center(len(text) + 2, " ")).center(100, "=")
    print(f"text.center() => { text_transform }")

    # text.ljsut() and text.rjsut() - text justification to left and right
    text_transform = text.ljust(100, " ")
    print(f"text.ljust() => { text_transform }")
    text_transform = text.rjust(100, " ")
    print(f"text.rjust() => { text_transform }")

    # text.swapcase() - swap lowercase and uppercase
    text_transform = text.swapcase()
    print(f"text.swapcase() => { text_transform }")

    # text.count(subtext_to_count, index_start, index_end) - count subtexts in text
    le_counter = text.count("le")
    # le_counter = text.count("le", 10, 20)
    print(f"text.count(\"le\") => { le_counter }")

    # text.endswith(text_end) - check if text end with text_end
    is_end_with_ss = text.endswith("ss")
    print(f"text.endswith(\"ss\") => { is_end_with_ss }")

    # text.index(subtext) - return index of subtext in text
    index_of_le = text.index("le")
    print(f"text.index(\"le\") => { index_of_le }\n")

    isalpha = ', '.join([t for t in text.split() if t.isalpha()])
    # isalpha = [t for t in text.split() if t.isalpha()]
    print(f"text.isalpha() => { isalpha }")
    isascii = [t for t in text.split() if t.isascii()]
    print(f"text.isascii() => { isascii }")
    isnumeric = [t for t in text.split() if t.isnumeric()]
    print(f"text.isnumeric() => { isnumeric }")
    isalnum = [t for t in text.split() if t.isalnum()]
    print(f"text.isalnum() => { isalnum }")
    isdigit = [t for t in text.split() if t.isdigit()]
    print(f"text.isdigit() => { isdigit }")
    isidentifier = [t for t in text.split() if t.isidentifier()]
    print(f"text.isidentifier() => { isidentifier }")
    islower = [t for t in text.split() if t.islower()]
    print(f"text.islower() => { islower }")
    isupper = [t for t in text.split() if t.isupper()]
    print(f"text.isupper() => { isupper }")
    istitle = [t for t in text.split() if t.istitle()]
    print(f"text.istitle() => { istitle }")
    isprintable = [t for t in text.split() if t.isprintable()]
    print(f"text.isupper() => { isprintable }")
    isspace = [t for t in text.split() if t.isspace()]
    print(f"text.isspace() => { isspace }")

    # text.split(separator, max_splits)
    text_split = text.split(',', 2)
    print(f"text.split(',', 2) => { text_split }")

    # alphabets
    _from = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    _to = "b c d e f g h i j k l m n o p q r s t u v w x y z a"

    dictionary = text.maketrans(_from, _to)
    print(f"text.maketrans(_from, _to) => { dictionary }")
    print(f"text.translate(dictionary) => { text.translate(dictionary) }")
