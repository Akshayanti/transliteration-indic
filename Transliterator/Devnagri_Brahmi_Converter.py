#!/usr/bin/env python3


class Converter:

    char_dev = ""
    char_brah = ""
    code_dev = 0
    code_brah = 0

    def to_brahmic(self, dev_char: str):
        self.char_dev = dev_char
        self.code_dev = ord(dev_char)
        self.code_brah = self.code_dev - 0x905 + 0x11005
        self.char_brah = chr(self.code_brah)

    def to_dev(self, brahmic_char: str):
        self.char_brah = brahmic_char
        self.code_brah = ord(brahmic_char)
        self.code_dev = self.code_brah - 0x11005 + 0x905
        self.char_dev = chr(self.code_dev)

    def get_char_dev(self):
        return self.char_dev

    def get_char_brah(self):
        return self.char_brah

    def get_code_dev(self):
        return hex(self.code_dev)

    def get_code_brah(self):
        return hex(self.code_brah)
