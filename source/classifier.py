import unicodedata

def classify_character(char):

    category = unicodedata.category(char)

    if category.startswith("L"):
        return "Letter"

    elif category.startswith("M"):
        return "Mark"

    elif category.startswith("N"):
        return "Number"

    elif category.startswith("P"):
        return "Punctuation"

    elif category.startswith("Z") or char.isspace():
        return "Whitespace"

    elif category.startswith("S"):
        return "Symbol"

    else:
        return "Other"
