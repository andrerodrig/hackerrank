import re


def main():
    result = re.split(r"[,.]+", input())
    for i in result:
        print(i)


main()
