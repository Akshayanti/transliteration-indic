import argparse
from Scraper.PaliScraper import PaliScraper
from Scraper.PrakritScraper import PrakritScraper

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Program to scrape Pali and Prakrit files")
    parser.add_argument("-l", "--language", type=str, required=True, choices=["pali", "prakrit"],
                        help="Language for Scraper")
    parser.add_argument("-i", "--input", nargs="+", type=str, required=True,
                        help="Input Files")
    parser.add_argument("-o", "--output", type=str, required=False, help="Output File")
    args = parser.parse_args()

    scraper = PaliScraper(args.input) if args.language == "pali" else PrakritScraper(args.input)
    scraper.write_text_in(args.output if args.output else "sample.txt")

