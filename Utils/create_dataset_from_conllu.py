#!/usr/bin/env python3

import argparse

ALL_BLOCKS = []
ALL_TEXT = []
ALL_TRANSLIT = []


def check_if_conllu_file(input_file):
    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            if line != "\n":
                if line.startswith("#") or len(line.split("\t")) == 10:
                    continue
                else:
                    print("Incorrect conllu file: {x}".format(x=input_file))
                    exit(1)


def read_block(input_conllu_file):
    global ALL_BLOCKS
    current_block = ""
    for line in input_conllu_file:
        if line == "\n":
            ALL_BLOCKS.append(current_block)
            current_block = ""
        else:
            current_block += line + "\n"


def filter_empty_block(input_file):
    global ALL_BLOCKS
    read_block(input_conllu_file=input_file)
    for input_block in ALL_BLOCKS:
        block = input_block.split("\n")
        text = [x.split(" = ")[1] for x in block if x.startswith("# text =")][0]
        if "_ _ _" not in text:
            yield input_block


def extract_text(input_block):
    text = []
    for line in input_block.split("\n"):
        if line.startswith("#") or line == "":
            continue
        else:
            cols = line.split("\t")
            if "-" not in cols[0]:
                text.append(cols[1])
    return " ".join(text)


def extract_translit(input_block):
    text = []
    for line in input_block.split("\n"):
        if line.startswith("#") or line == "":
            continue
        else:
            cols = line.split("\t")
            if "-" not in cols[0]:
                translit_text = [x.split("=")[1] for x in cols[-1].split("|") if x.startswith("Translit")]
                text.append(translit_text[0] if len(translit_text) != 0 else "xyz")
    return " ".join(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Before running this program, download and extract latest UD package from "
                                     "universaldependencies.org/#download. \n "
                                     "Then, concatenate all the hindi/sanskrit conllu files (with .conllu extension) "
                                     "into a singular file.\n "
                                     "This concatenated file becomes the input for this program")
    parser.add_argument("-l", "--language", type=str, required=True, choices=["hi", "sa"],
                        help="Language for Creating Dataset")
    parser.add_argument("-i", "--input", nargs="+", type=str, required=True,
                        help="Input Files")
    args = parser.parse_args()

    globals()
    for given_file in args.input:
        check_if_conllu_file(given_file)
        with open(given_file, "r", encoding="utf-8") as infile:
            for block in filter_empty_block(infile):
                ALL_TEXT.append(extract_text(block))
                ALL_TRANSLIT.append(extract_translit(block))

    with open("{x}.dataset".format(x=args.language), "w", encoding="utf-8") as outfile:
        for text, translit in zip(ALL_TEXT, ALL_TRANSLIT):
            outfile.write("{x}\n{y}\n\n".format(x=text.strip(), y=translit.strip()))
