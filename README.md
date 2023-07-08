# WordsInWords
Finding Different Words in Words

The code defines a function main that takes three parameters: wordOne, wordTwo, and count.
The function initializes an empty list wordList.
It checks if both wordOne and wordTwo do not contain any spaces. If true, it checks if the length of wordTwo is less than wordOne. If so, it swaps the values of wordOne and wordTwo.
It checks if wordTwo contains a space. If true, it swaps the values of wordOne and wordTwo.
It splits wordOne into a list of words using whitespace as the delimiter.

It opens a file named "results.txt" in append mode.
It iterates over the indices of wordOne using a for loop.
For each word wordOne[j] in wordOne, it checks if wordOne[j] is present in wordTwo. If true, it appends the start and end indices of wordOne[j] in wordTwo to the wordList list. It also writes the result to the "results.txt" file.
If wordOne[j] is not present in wordTwo, it constructs a new string newStr that represents the indices of wordOne[j] in wordTwo. It writes this result to the "results.txt" file.


It opens a file named "wordinwords.txt" in read mode.
It reads the lines from the file and filters out lines that do not contain the words "HARE" or "CONE". The filtered lines are stored in the new_lines list.
It opens a file named "new_file.txt" in write mode and writes the filtered lines to the file.
It opens the "new_file.txt" file in read mode.
It initializes an empty list uppercase_strings.
It reads the contents of the file, splits the words, and performs some replacements and filtering operations.

It iterates over the words in words.
For each word, it removes punctuation marks, replaces "PUERTO" with "PUERTORICO", and checks if the word is in uppercase.
If the word is in uppercase and not equal to "A", it appends it to uppercase_strings.
For the word "EARTH", it appends a specific string to uppercase_strings.
For the word "OCEAN", it appends a specific string to uppercase_strings.
It removes specific words from uppercase_strings.
It reverses uppercase_strings and removes specific elements.
It reverses uppercase_strings again.
It initializes a variable count to 0.
It iterates over the range from 0 to the length of uppercase_strings in steps of 2.
For each iteration, it increments count and calls the main function with appropriate arguments.
