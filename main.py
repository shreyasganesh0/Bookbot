
from collections import Counter
def count_unique_chars(text):
    text=text.lower()
    c = Counter(text)
    print(c)
    
def count_words(text):
    count = 0
    for i in text.split():
        count +=1
    print(f"count is {count}")
def main():
    with open("book/frankenstein.txt", 'r') as f:
        file_text=f.read()
        count_words(file_text)
        count_unique_chars(file_text)

if __name__ == "__main__":
    main()
