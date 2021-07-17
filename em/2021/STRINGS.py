def reverse_sentence(str):
    # word_list = str.split()
    # reverse_list = word_list[::-1]
    # reverse_senetence = " ".join(reverse_list)
    print(" ".join(reversed(str.split())))
    return " ".join(str.split()[::-1])


# Palindrome Check
def is_palindrome(arr):
    left_idx, right_idx = 0, len(arr) - 1
    while left_idx < right_idx:
        if arr[left_idx] != arr[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def is_palindrome2(string):
    reverse_char = []

    for i in reversed(range(len(string))):
        reverse_char.append(string[i])
    print(reverse_char, "".join(reverse_char))
    return string == "".join(reverse_char)


# strx = "abcdcba"
# print(is_palindrome2(strx))


def caesarCipherEncryptor(string, key):
    # Write your code here.
    new_letters = []
    new_key = key % 26

    for letter in string:
        new_letters.append(get_new_letter(letter, new_key))


def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)


# run length encoding
def runLengthEncoding(string):
    # Write your code here.
    encoded_string = []
    current_length = 1
    for i in range(1, len(string)):
        current_char = string[i]
        previous_char = string[i - 1]

        if (current_char != previous_char) or (current_length == 9):
            encoded_string.append(str(current_length))
            encoded_string.append(previous_char)
            current_length = 0

        current_length += 1

        # handle the last run
    encoded_string.append(str(current_length))
    encoded_string.append(string[len(string) - 1])
    return "".join(encoded_string)


# print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))


# GENERATE DOCUMENTS
def generateDocument(characters, document):
    # Write your code here.
    char_counts = {}
    for char in characters:
        char_counts[char] = characters.get(char, 0) + 1

    for char in document:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1
    return True


# anagram
def groupAnagrams(words):
    anagrams = {}

    for word in words:
        sorted_words = "".join(sorted(word))
        anagrams[sorted_words] = anagrams.get(sorted_words, []) + [word]

    return list(anagrams.values())


# Reverse words in a string

def reverseWordsInString(string):
    # Write your code here.
    characters = [char for char in string]
    reverse_list_range(characters, 0, len(string) - 1)

    start_word = 0
    while start_word < len(characters):
        end_of_word = start_word
        while end_of_word < len(characters) and characters[end_of_word] != " ":
            end_of_word += 1


def reverse_list_range(list1, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


# print(reverseWordsInString("AlgoExpert is the best!"))

#  Votes

Votes = ["john", "johnny", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie",
         "johnny", "john", "johnny"]


def election_winner(votes):
    votes_freq = {}
    for vote in votes:
        votes_freq[vote] = votes_freq.get(vote, 0) + 1
    winner = sorted([k for k, v in votes_freq.items() if v == max(list(votes_freq.values()))])[0]

    return winner


# print(election_winner(Votes))

def reverseWordsInString(string):
    # Write your code here.
    # start, end = 0, len(list) - 1
    words = []
    start_of_word = 0

    for idx in range(len(string)):
        char = string[idx]
        if char == " ":
            words.append(string[start_of_word:idx])
            start_of_word = idx
        elif string[start_of_word] == " ":
            words.append(" ")
            start_of_word = idx
    words.append(string[start_of_word:])
    reverse_list(words)
    return "".join(words)


def reverse_list(listx):
    start, end = 0, len(listx) - 1
    while start < end:
        listx[start], listx[end] = listx[end], listx[start]
        start += 1
        end -= 1


sz = "AlgoExpert is the best!"
print(reverseWordsInString(sz))


###################
