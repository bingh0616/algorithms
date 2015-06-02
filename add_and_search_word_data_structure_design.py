# problem description: https://leetcode.com/discuss/questions/oj/add-and-search-word-data-structure-design

class WordDictionary:
    
    def __init__(self):
        self.trie = self.Trie()
    
    class Trie:
        def __init__(self):
            self.is_leaf = False
            self.children = [None] * 26
            
    def getIdx(self, ch):
        return ord(ch)-ord('a')

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        root = self.trie
        wl = len(word)
        for i in xrange(wl):
            idx = self.getIdx(word[i])
            if not root.children[idx]:
                root.children[idx] = self.Trie()
            root = root.children[idx]

        root.is_leaf = True
            

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.search_helper(word, self.trie)

    def search_helper(self, word, root):
        wl = len(word)
        if wl == 0: return root.is_leaf
        for i in xrange(wl):
            if word[i] != '.':
                idx = self.getIdx(word[i])
                if not root.children[idx]:
                    return False
                root = root.children[idx]
            else:
                for j in range(26):
                    if root.children[j] and self.search_helper(word[i+1:], root.children[j]):
                        return True
                return False
        return root.is_leaf
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


def main():
    wd = WordDictionary()
    wd.addWord('bad')
    wd.addWord('dad')
    wd.addWord('ca')
    print wd.search('hello')
    print wd.search('aab')
    print wd.search('bad')
    print wd.search('dad')
    print wd.search('bad')
    print wd.search('.a.')
    print wd.search('d.d')
    print wd.search('.')
    print wd.search('c')

if __name__ == '__main__':
    main()
