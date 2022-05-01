#!/usr/bin/env python3

from bs4 import BeautifulSoup
import inltk

from Devnagri_Brahmi_Converter import Converter


def open_and_parse(input_doc):
    with open(input_doc, "r", encoding="utf-8") as htmlDoc:
        contents = htmlDoc.read()
        soup = BeautifulSoup(contents, "lxml")
        text_version = soup.get_text()
        return text_version


class Scraper:

    text_orig = ""
    text_dev = ""
    text_brah = ""
    converter = Converter()

    def __init__(self, input_files=None):
        if type(input_files) == list:
            for input_doc in input_files:
                self.text_orig += open_and_parse(input_doc)
        elif type(input_files) == str:
            self.text_orig += open_and_parse(input_files)

    def parse_only_content(self):
        text = []
        flag = True
        for line in self.text_orig.split("\n"):
            if flag and "http://gretil.sub.uni-goettingen.de/gretil.htm" in line:
                flag = False
                continue
            if not flag and "Page " not in line and "page " not in line:
                text.append(line.replace(" ", ""))
        self.text_orig = "\n".join(text)
        return self.text_orig

    def rom_to_dev(self):
        text_dev = []
        for lines in self.text_orig.split("\n"):
            inltk


    def dev_to_brah(self):
        text_brah = []
        for lines in self.text_dev.split("\n"):
            chars = ""
            for char in lines:
                if 0x905 <= ord(char) <= 0x96F:
                    self.converter.to_brahmic(char)
                    chars += self.converter.get_char_brah()
                else:
                    chars += char
            text_brah.append(chars)
        self.text_brah = "\n".join(text_brah)

    def parse_into_brah(self):
        self.rom_to_dev()
        self.dev_to_brah()

    def print_text(self):
        print(self.text_orig)

    def print_dev_text(self):
        print(self.text_dev)

    def print_brah_text(self):
        print(self.text_brah)

    def write_text_in(self, filename):
        with open(filename, "w", encoding="utf-8") as outfile:
            outfile.write(self.text_orig)

    def write_dev_text_in(self, filename):
        with open(filename, "w", encoding="utf-8") as outfile:
            outfile.write(self.text_dev)

    def write_brah_text_in(self, filename):
        with open(filename, "w", encoding="utf-8") as outfile:
            outfile.write(self.text_brah)
