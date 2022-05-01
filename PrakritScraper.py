#!/usr/bin/env python3

from Scraper import Scraper


class PrakritScraper(Scraper):
    parsed_data = ""

    def __init__(self, input_file=None):
        super().__init__(input_file)
        self.parsed_data = super().parse_only_content()


if __name__ == "__main__":
    pass
