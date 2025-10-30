def palindromes(words):
    result = {"palindrome": [], "non-palindrome": []}
    
    for word in words:   
        reversed_word = ''      #empty should be under the for loop
        #reverse the word and check if it is the orginal word
        for letter in word:
            reversed_word = letter + reversed_word
            if reversed_word == word:
                result["palindrome"].append(word) #palindrome qu lieu de non-
            else:
                result["non-palindrome"].append(word)  #here non-palindromes
    
    return result
print(palindromes(["level","word", "reader", "python"]))