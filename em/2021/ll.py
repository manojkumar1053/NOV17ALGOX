def firstNonRepeatingChar(str):
    # for i in range(len(str)):
    #     foundDuplicate = False
    #     for j in range(len(str)):
    #         if str[i] == str[j] and i != j:
    #             foundDuplicate = True
    #
    #     if not foundDuplicate:
    #         return i
    # return -1

    charFreq = {}

    for char in str:
        charFreq[char] = charFreq.get(char, 0) + 1

    for ele in str:
        print(ele)
        if charFreq[char] == 1:
            return str.index(ele)
    return -1

#print(firstNonRepeatingChar("manoja"))
#===========LCS

def lcs(str1,str2):
