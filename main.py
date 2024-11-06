from collections import Counter
def count_unique_chars(text):
    text=[i for i in text.lower() if i.isalnum()]
    c = Counter(text)
    return c
    
def count_words(text):
    count = 0
    for i in text.split():
        count +=1
    return count
def book_report(count,words_d):
    print("---book report for frankenstein---\n")
    print(f"Number of words {count} \n")
    for i in words_d:
        print(f"The count of letter {i} is {words_d[i]}\n")
    print("---End Report--")

    
def main():
    with open("book/frankenstein.txt", 'r') as f:
        file_text=f.read()
        word_count=count_words(file_text)
        word_count_dict=count_unique_chars(file_text)
        book_report(word_count,word_count_dict)

if __name__ == "__main__":
    main()
