HINDI_WORDS = []
GLYPH = ['र']


def read_input_file(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        for line in infile:
            hin, _ = line.strip().split("\t")
            HINDI_WORDS.append(hin)


def no_matra():
    for word in HINDI_WORDS:
        if not any([x in word for x in GLYPH]):
            yield word


if __name__ == "__main__":
    read_input_file("../Utils/dev_to_translit.tsv")
    for x in no_matra():
        if x == 'राजः':
            print("exists")
