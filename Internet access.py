# Let's start to study how work with web via python

from urllib import request


def main():
    webUrl = request.urlopen("https://www.google.com")
    print("Status:", str(webUrl.getcode()))


if __name__ == "__main__":
    main()
