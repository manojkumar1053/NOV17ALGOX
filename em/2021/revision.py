# Reverse the sentence

def reverse_sentence(str):
    # word_list = str.split()
    # reverse_list = word_list[::-1]
    # reverse_senetence = " ".join(reverse_list)
    print(" ".join(reversed(str.split())))
    return " ".join(str.split()[::-1])


word = "Hello World!"
print(reverse_sentence(word))


# Group anagram
def groupAnagrams1(words):
    anagrams = {}

    for word in words:
        sorted_words = "".join(sorted(word))
        anagrams[sorted_words] = anagrams.get(sorted_words, []) + [word]

    return list(anagrams.values())


# lx = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# print(groupAnagrams1(lx))


def groupAnagrams(words):
    anagrams = {}

    for word in words:
        sorted_words = "".join(sorted(word))
        if sorted_words in anagrams:
            anagrams[sorted_words].append(word)
        else:
            anagrams[sorted_words] = [word]

    return list(anagrams.values())
#
# lx = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# print(groupAnagrams(lx))
