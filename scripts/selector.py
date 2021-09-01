#!/usr/local/bin/python3
"""usage: selector <CSS selector (.btn etc.)>

accepts html through stdin"""
import getopt
import sys

from bs4 import BeautifulSoup


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        inf = sys.stdin
    except getopt.GetoptError:
        print(__doc__)
        sys.exit(1)

    # settings for app runtime options
    config = {
        "attr_to_print": [],
        "print_in_html": False,
    }
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(__doc__)
            sys.exit()
        elif opt in ("--html"):
            config["print_in_html"] = True
            print("prettt")
        elif opt in ("-a", "--attr"):
            config["attr_to_print"].append(arg)
    try:
        soup = BeautifulSoup(inf, "html.parser")
        for selector in args:
            for e in soup.select(selector):
                if "--html" in sys.argv:
                    print(e.prettify())
                # e.g. cat source.html | selector img --attr src
                elif config["attr_to_print"]:
                    for arg in config["attr_to_print"]:
                        print(e[arg])
                else:
                    print(e.get_text())
    except IndexError:
        print(__doc__)
        sys.exit(1)
