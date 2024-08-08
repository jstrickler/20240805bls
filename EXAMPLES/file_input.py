import fileinput
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description="Faux grep program")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("-n", dest="show_file_name", action="store_true", help="Show file names")
parser.add_argument("search_term", help="Search term")
parser.add_argument("files", nargs="+", help="Files to search")

args = parser.parse_args()  # parsers sys.argv[1:]

if args.ignore_case:
    search_term = args.search_term.lower()
else:
    search_term = args.search_term

for original_line in fileinput.input(args.files):
    if args.ignore_case:
        line_to_search = original_line.lower()
    else:
        line_to_search = original_line

    if search_term in line_to_search:
        if args.show_file_name:
            print(f"{fileinput.filename()}", end=" ")
        print(original_line, end='')
