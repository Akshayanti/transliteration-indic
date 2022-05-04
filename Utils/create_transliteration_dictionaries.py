#!/usr/bin/env python3

DEV_TO_TRANSLIT = dict()
TRANSLIT_TO_DEV = dict()


def write_output(filename, global_dict):
    global DEV_TO_TRANSLIT, TRANSLIT_TO_DEV
    with open(filename, "w", encoding="utf-8") as outfile:
        for key in global_dict.keys():
            outfile.write("{x}\t{y}\n".format(x=key, y=global_dict[key]))


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        count = 0
        dev = ""
        translit = ""
        for line in infile:
            count += 1
            if count % 2 != 0:
                for x, y in zip(dev.split(), translit.split()):
                    if y != "xyz" and x not in DEV_TO_TRANSLIT and y not in TRANSLIT_TO_DEV and x != y:
                        DEV_TO_TRANSLIT[x] = y
                        TRANSLIT_TO_DEV[y] = x
                dev = line.strip()
            else:
                translit = line.strip()


if __name__ == "__main__":
    read_file("hi.dataset")
    read_file("sa.dataset")

    write_output("dev_to_translit.tsv", DEV_TO_TRANSLIT)
    write_output("translit_to_dev.tsv", TRANSLIT_TO_DEV)
