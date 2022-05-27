# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word = input("Enter the word to compare: ")
anagram = input("Enter the anagram of the word entered: ")

def find_anagram(word, anagram):
     
    # sort the strings and comapre using sorted() function
    if(sorted(word) == sorted(anagram)):
        return True        #return True if they are the same
              
    else:
        
        return False      #return False if the are not the same

# calling the function to run the code: 

find_anagram(word, anagram)