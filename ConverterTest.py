#!/usr/bin/env python3

import unittest

from Devnagri_Brahmi_Converter import Converter


class ConverterTest(unittest.TestCase):

    def test_dev_to_brahmi(self):
        input_char = "आ"
        output_char = "𑀆"
        converter = Converter()
        converter.to_brahmic(input_char)
        self.assertEquals("0x11006", converter.get_code_brah())
        self.assertEquals(output_char, converter.get_char_brah())

    def test_brahmi_to_dev(self):
        input_char = "𑀆"
        output_char = "आ"
        converter = Converter()
        converter.to_dev(input_char)
        self.assertEquals("0x906", converter.get_code_dev())
        self.assertEquals(output_char, converter.get_char_dev())


if __name__ == "__main__":
    pass
