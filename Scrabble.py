from DictTrie import DictTrie
from Trie import Trie

class Scrabble(object):
    def __init__(self, words):
        self.trie = DictTrie(words)

    def helper(self, prefix, letters, result, node):
        if (len(letters) <= 0):
            return
        
        if ('isWord' in node.keys() and node['isWord'] == True):
            result.append(prefix)
        
        for i in range(len(letters)):
            l = letters[i]
            if l in node.keys():
                self.helper(prefix + l, letters[:i]+letters[i+1:], result, node[l])
        return

    # given a prefix and a list of letters that can be used, give all possible words
    def findWords(self, prefix, letters):
        node = self.trie.findNode(prefix, self.trie.d)
        if (node == None):
            return None
        
        result = []
        self.helper(prefix, letters, result, self.trie.d)
        return result


def gameLoop(scrabble):
    gameLoop = True
    while gameLoop == True:
        print('Type "p" to get scrabble help.\nType "q" if you would like to quit')
        gameType = raw_input('Type here: ')
            
        if gameType.lower() == "p":
            print("Give me all the letters in your hand, separated by spaces: ")
            letters = raw_input("Type here: ")
            letters = letters.split(' ')
            prefix = raw_input("Give me a prefix: ")
            result = scrabble.findWords(prefix, letters)
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
    scrabble = Scrabble(content)
    
    gameLoop(scrabble)
        