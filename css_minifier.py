# -*- coding: utf-8 -*-

import re

def main():
    filename = "../temp/style.css"
    filename2 = "../temp/style-mini.css"
    file1 = open(filename, encoding="utf8")
    file2 = open(filename2, "wt", encoding="utf8")
    text = file1.read()
    print(text)

    for text_one in text.split("/*"):
        if text_one:
            comment = text_one.find("*/")
            print("/*", text_one[:comment],"*/", sep="", end="", file=file2)
            for word in text_one[comment + 2:].split():
                print(word, end="", file=file2)
            print("", file=file2)
    file1.close()
    file2.close()

if __name__ == "__main__":
    main()