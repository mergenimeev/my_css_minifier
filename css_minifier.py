import re

def main():
    filename = "../style.css"
    filename2 = "../style-mini.css"
    file1 = open(filename)
    file2 = open(filename2, "wt")
    text = file1.read()

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