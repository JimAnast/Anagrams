# Anagrams

An anagram is a word formed by rearranging the letters of a different word by using all the original letters exactly once. For example, the word bawl can be rearranged into 'blaw' or the word 'alerts' into 'salter'.

This program reads a word list from the file words.txt and as an output, it prints

1) all the lists of words that are anagrams ordered by the length of lists.
2) all the lists of words that are anagrams and contains n letters which is given as an input.

Note: All anagrams should also be in the words.txt file.

Example:

For 6 letters, we will have for example:

...

(2, ['append', 'napped'])

...

(12, ['enters', 'ernest', 'estren', 'nester', 'renest', 'rentes', 'resent', 'sterne', 'streen', 'tenser', 'ternes', 'treens'])

...



At first, we need to declare the local path for the opening of the file. I put it in the same folder that I keep the .py file for convenience and I just give the 'words.txt' as the local path of the words.txt file. 
As you may see in the python file, in the beginning I used a list to save all of the words of the txt file. Since we want the program to perform 2 tasks: (1)print all the lists of words that are anagrams ordered by the length of lists and (2) print all the lists of words that are anagrams and contains n letters which is given as an input, I created two functions, one for each of those 2 tasks. I ask the user if they want to print all the lists of words that are anagrams and then according to their answer the program prints them or not. 
We skip the lists that have length equal to 1 (one word lists), as these do not contain any anagrams. So the lists that appear are those that contain >=2 words. Then I ask for the number of letters that the words will contain and according to that number the program prints the only the lists those words. These lists are also ordered by their length with ascending order, as it is shown in the example of the description of Problem 2.



I used dictionary to keep the lists of words that are anagrams, as it was the fastest and most efficient way for me to do this. That is because with the dictionary I could create a key for each sorted word and check if it matches with another sorted word and the categorize these words together in the same group. 
Otherwise, it would create a new key for that word and, in case it would encounter that key in the future, it would categorize that word with that new key (you may check the code for higher cleanse). 
In that way, the program groups the words that are anagrams fast and efficiently and the code for each function (create_anagram_dict and
make_anagram_dict_with_num) is short and easy to read. Then, I used lists to print the values that I wanted, in the order and the format that I wanted, as I found this to be the easiest and the fastest way.
