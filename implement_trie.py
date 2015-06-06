ALPHABET_SIZE = 26

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_word = False
        self.children = [None] * ALPHABET_SIZE 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        curr = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_word = True
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        curr = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.is_word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            idx = ord(c)-ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

def main():
    trie = Trie()
    trie.insert('something')
    print trie.search('something')
    print trie.search('some')
    print trie.startsWith('some')
    print trie.startsWith('ome')

if __name__ == '__main__':
    main()
