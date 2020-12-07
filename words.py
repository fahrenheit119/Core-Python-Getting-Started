import sys
from urllib.request import urlopen

def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words
    

def print_words(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_words(words)


if __name__ == '__main__':
    main(sys.argv[1])
