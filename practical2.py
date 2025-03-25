
from collections import Counter


def read_file(sample):
    with open(sample, 'r') as file:
        return file.read()


content = read_file('sample.txt')
print(content[:100])  

# Count the number of lines
def count_lines(content):
    return len(content.split('\n'))


# Count Words

def count_words(content):
    return len(content.split())


# Most Common Word

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]


# Average Word Length

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

#  Number of Unique Words
def count_unique_words(content):
    words = set(content.lower().split())
    return len(words)

# Longest Words
def longest_word(content):
    words = content.split()
    return max(words, key=len)

# Count of Occurence of specific words

def count_specific_word(content, specific_word):
    words = content.lower().split()
    specific_word = specific_word.lower()
    return words.count(specific_word)


# Percentage of words longer than the average

def percentage_longer_than_average(content):
    words = content.split()
    average_length = average_word_length(content)

    longer_words = [word for word in words if len(word) > average_length]
    percentage = (len(longer_words) / len(words))* 100
    return percentage

def analyze_text(filename, specific_word=None):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    num_unique_words = count_unique_words(content)
    longest = longest_word(content)
    percentage = percentage_longer_than_average(content)

    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Longest word: {longest}")
    print(f"Percentage of words longer than  the average word length: {percentage:.2f}")


    if specific_word: 
        specific_word_count = count_specific_word(content, specific_word)
        print(f"Occurrences of '{specific_word}': {count}")

if __name__ == "__main__":
    specific_word_input = input("Enter a word to count its occurrences (or press Enter to skip): ")
    analyze_text('sample.txt', specific_word_input if specific_word_input else None)