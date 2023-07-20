from collections import defaultdict

def groupAnagrams(strs):
    myDict = defaultdict(list)

    for word in strs:
        #sorted is a function that retrns a list
        sorted_word = ''.join(sorted(word))
        myDict[sorted_word].append(word)
    
    return myDict.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])
