import sys

class DictTrie(object):
    def __init__(self, words=[]):
        self.d = dict()
        for word in words:
            word = word.strip('\n')
            word = word.strip('\r\n')
            self.add(word.strip('\n').lower())
    
     # MAIN HEADER FUNCTION TO ADD WORDS TO A TRIE
    def add(self, word):
        curr = self.d
        for i in range(len(word)):
            curr = self.addLetter(word[i], curr)
            if 'isWord' not in curr.keys():
                curr['isWord'] = False
        curr['isWord'] = True
        

    # returns the key dict the added letter points to
    # or if it already exists, returns the dict it points to
    def addLetter(self, letter, d):
        if letter in d.keys():
            return d[letter]
        else:
            d[letter] = dict()
            return d[letter]

    # finds the dictionary that the last letter of the prefix points to
    def findNode(self, prefix, node):
        if (len(prefix) <= 0):
            return node

        for key in node.keys():
            if key == prefix[0]:
                return self.findNode(prefix[1:], node[key])
        return None

    # MAIN HEADER FUNCTION TO CHECK IF WORD EXISTS IN A TRIE
    def find(self, word):
        node = self.findNode(word, self.head)
        if (node.isWord == True):
            return True
        return False

    def findWordsHelper(self, prefix, node, result):
        if (node['isWord'] == True):
            result.append(prefix)
        
        for key in node.keys():
            if (key != 'isWord'):
                self.findWordsHelper(prefix+key, node[key], result)
        
        return

    def findWordsWithPrefix(self, prefix):
        node = self.findNode(prefix, self.d)
        if (node == None):
            return None
        
        result = []
        self.findWordsHelper(prefix, node, result)
        return result

    # MAIN HEADER FUNCTION TO REMOVE WORDS TO A TRIE
    def remove(self, word):
        node = self.findNode(word, self.d)
        if (node != None):
            node['isWord'] = False
        return

    # MAIN HEADER FUNCTION TO GET WORDS WITH A PREFIX
    def search(self, prefix):
        return self.findWordsWithPrefix(prefix)


def gameLoop(trie):
    gameLoop = True
    while gameLoop == True:
        print('Type "auto" if you would like to try the autocomplete program.\n Type "scrabble" if you would like scrabble words.\nType "q" if you would like to quit')
        gameType = raw_input('Type here: ')
            
        if gameType.lower() == "auto":
            prefix = raw_input("Give me a prefix: ")
            result = trie.findWordsWithPrefix(prefix)
            print(result)
            print(" ")

        if gameType.lower() == "scrabble":
            print("Give me all the letters in your hand, separated by spaces: ")
            letters = raw_input("Type here: ")
            letters = letters.split(' ')
            prefix = raw_input("Give me a prefix: ")
            result = trie.scrabbleWordFinder(prefix, letters)
            print(result)
            print(" ")
        
        if gameType.lower() == 'q':
            gameLoop = False
            print(" ")
            print("Thanks, b-bye!")
        

if __name__ == '__main__':
    # content= ['hello', 'lone', 'hen', 'hear']
    # file = open('/usr/share/dict/words','r')
    file = open('scrabbleWords.txt','r')
    content = list(file)
    # print('')
    trie = DictTrie(content)
    
    gameLoop(trie)
        