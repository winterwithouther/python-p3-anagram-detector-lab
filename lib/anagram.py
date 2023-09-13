class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, words):
        matchingWords = []
        charList = list(self.word)
        charList.sort()
        for word in words:
            charList2 = list(word)
            charList2.sort()
            if charList == charList2:
                matchingWords.append(word)
        return matchingWords
    
anagram1 = Anagram("word")
print(anagram1.match(["hello", "goodbye", "dowr", "drow", "wdro"]))