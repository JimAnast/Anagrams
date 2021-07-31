all_words = []
with open(r'words.txt', 'r') as f:      #declare the local path for the opening of the file. 
    for line in f:                      
        for word in line.split():
            all_words.append(word)          #create a list that contains all of the words of the file.


def create_anagram_dict(all_words):
    d = {}                                  #create a new dictionary for all of the words.
    for word in all_words:
        word = word.lower()                 #convert all the letters of the word into lower case letters.
        key = ''.join(sorted(word))         #create the key from the sorted current word.
        if key in d:                        #check if the key already exists.
            d[key].append(word)             #in the dictionary, add the current word to the connections of that key.
        else:
            d[key] = [word]                 #in the dictionary, make a new matching of that key with that word.

    return d

def make_anagram_dict_with_num(all_words):   #this is for dictionary only for the words with n letters.
    d = {}
    for word in all_words:
      if len(word) == num:                  #keep only the words that have letters = num given by the user.
          word = word.lower()
          key = ''.join(sorted(word))
          if key in d:
              d[key].append(word)
          else:
              d[key] = [word]
    return d


if __name__ == '__main__':
    while True:
        answer = str(input("Do you want to print all the lists of words that are anagrams? (y/n): "))
        if answer == 'y':
            d = create_anagram_dict(all_words)
            lists = []
            for list_of_words in d.values():
                lists.append(list_of_words)
            lists.sort(key=len)
            count = 0
            for list_of_words in lists:
                if len(list_of_words) > 1:
                    print(len(list_of_words), (",["), ",".join(list_of_words), "]")
            break
        elif answer == 'n':
            print("Okay")
            break
        else:
            print("Please enter y or n.")


    print("Now we will print all the lists of words that are anagrams and contain n letters.")
    num = int(input("Enter the number of letters that the words will have: "))
    di = make_anagram_dict_with_num(all_words)
    new_lists = []                         #new lists that will contain only the groups of words with num letters.
    for list_of_words in di.values():
        new_lists.append(list_of_words)
    new_lists.sort(key=len)
    for list_of_words in new_lists:
        if len(list_of_words) > 1:
            print(len(list_of_words), (",["), ",".join(list_of_words), "]")




