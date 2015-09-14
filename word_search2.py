# problem description: https://leetcode.com/problems/word-search-ii/

ALPHABET_SIZE = 26

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None] * ALPHABET_SIZE 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_word = True
        

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[s]]
        :type words: List[s]
        :rtype: List[s]
        """
        m = len(board)
        if m == 0: return False
        n = len(board[0])
        trie = Trie()
        for w in words:
            trie.insert(w)
            
        res = []
        for i in xrange(m):
            for j in xrange(n):
                self.search(board, trie.root, i, j, '', set(), res)
        return res
        
    def search(self, board, node, i, j, s, visited, res):
        if node.is_word:
            res.append(s)
            node.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited: return
        node = node.children[ord(board[i][j])-ord('a')]
        if node is None: return

        s += board[i][j]
        visited.add((i, j))
        self.search(board, node, i-1, j, s, visited, res)
        self.search(board, node, i+1, j, s, visited, res)
        self.search(board, node, i, j-1, s, visited, res)
        self.search(board, node, i, j+1, s, visited, res)
        visited.discard((i, j))
        

