# Trie-Autocomplete-Scrabble

This repository consists of two versions of a trie, a version of autocomplete, and a scrabble helper.

# Trie
This implementation consists of a data-structural approach to a trie, using nodes and arrays.

## Method Header:

```
// Provide a list of words upon initialization
class Trie(object):
    
    // add a word to trie
    def add(word)

    // remove a word from trie
    def remove(word)

    // find if a word exists in trie
    def find(word)

    // search all words with a prefix
    def search(prefix)

    // search all words with a prefix and how many times they occured
    def searchAndCount(prefix)

```

# DictTrie
This implementation uses dictionaries to create a trie. Refer to my [medium post](https://medium.com/nyc-design/the-secret-to-always-winning-at-scrabble-4f27843d9c44) for a visual explanation.

## Method Header:
```
// Provide a list of words upon initialization
class Trie(object):
    
    // add a word to trie
    def add(word)

    // remove a word from trie
    def remove(word)

    // find if a word exists in trie
    def find(word)

    // search all words with a prefix
    def search(prefix)

```
# Autocomplete
This is implemented by using the trie to find words that begin with a certain prefix. This is done through the search function inside the Trie and DictTrie classes.

## Method Header:
```
class Trie(object):

    // search all words with a prefix
    def search(prefix)

    // search all words with a prefix and how many times they occured
    def searchAndCount(prefix)

class DictTrie(object):

    // search all words with a prefix
    def search(prefix)

    // search all words with a prefix and how many times they occured
    def searchAndCount(prefix)
```

# Scrabble
This is implemented by using the trie to find words that begin with a certain prefix and uses only the letters that a player has in their hand (provided by the player)

## Method Header:
```
// Provide a list of words upon initialization to setup a trie with scrabble words
class Scrabble(object):
    
    // search all words with a prefix and only the letters given
    def findWords(prefix, letters)

```

# Testing Trie and DictTrie with time (A Comparison)
In order to test the trie, run test.py by entering

`python TestTrie.py yourPrefix`

in the terminal. Replace yourPrefix with a prefix of your choice.

This will show you the time it took to set up the Trie, to find the words, and the total time.

## Examples: 

### Finding words with prefix 'apple'

Run the following command:
`python TestTrie.py apple`

You should get this result:
```
Vocabulary size: 235886
Completions of apple: apple, appleberry, appleblossom, applecart, appledrane, applegrower, applejack, applejohn, applemonger, 
applenut, appleringy, appleroot, applesauce, applewife, applewoman
()
Initial setup time: 6.100565 sec
Autocomplete time:  0.000053 sec
Total time elapsed: 6.100618 sec
```

### Finding words with prefix 'zebra'

Run the following command:
`python TestTrie.py zebra`

You should get this result:
```
Vocabulary size: 235886
Completions of zebra: zebra, zebraic, zebralike, zebrawood
()
Initial setup time: 5.750774 sec
Autocomplete time:  0.000016 sec
Total time elapsed: 5.750790 sec
```

### Finding words with prefix 'code'

Run the following command:
`python autocomplete.py code`

You should get this result:
```
Vocabulary size: 235886
Completions of code: code, codebtor, codeclination, codecree, codefendant, codeine, codele, codelight, codelinquency, codelinq
uent, codenization, codeposit, coder, coderive, codescendant, codespairer, codex
()
Initial setup time: 5.750729 sec
Autocomplete time:  0.000037 sec
Total time elapsed: 5.750766 sec
```

# Testing Autocomplete in the terminal

Run the following command in your terminal:
`python Trie.py`

# Using Scrabble Helper

