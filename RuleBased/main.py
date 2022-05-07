HINDI_WORDS = []
GLYPH = ['्']
NO_HALANT = []


# todo: create fnc that filtered words without matra(no matra)
# todo: create fnc that filter words without halant(no halflings)
# todo: generate list of words without matras and without halant
# todo: generate list of words without halant


def read_input_file(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        for line in infile:
            hin, _ = line.strip().split("\t")
            HINDI_WORDS.append(hin)


def no_matra():
    for word in HINDI_WORDS:
        if not any([x in word for x in GLYPH]):
            yield (word)


def no_halant():
    for word in HINDI_WORDS:
        if not any([x in word for x in GLYPH]):
            yield (word)

if __name__ == "__main__":
    read_input_file("../Utils/dev_to_translit.tsv")
    for x in no_halant():
        print(x)
        NO_HALANT.append(x)
