def main(wordOne, wordTwo, count):
    wordList = []
    if (wordOne.find(" ") == -1) and (wordTwo.find(" ") == -1):
        if len(wordTwo) < len(wordOne):
            a = wordTwo
            wordTwo = wordOne
            wordOne = a
    if " " in wordTwo:
        a = wordTwo
        wordTwo = wordOne
        wordOne = a
    wordOne = wordOne.split()
    with open("results.txt", "a") as f:
        for j in range(len(wordOne)):
            if wordOne[j] in wordTwo:
                wordList.append(wordTwo.index(wordOne[j][-1]) - len(wordOne[j]) + 1)
                wordList.append(wordTwo.index(wordOne[j][-1]))
                f.write(str(count) + ".\n" + "In the word \"" + wordTwo + "\":"
                        + "\n\t" + wordOne[j] + " = " + wordTwo + "[" + str(wordList[0]) + ":"
                        + str(wordList[-1]) + "]" + "\n\n")
            else:
                idx = ""
                newStr = ""
                for i in wordOne[j]:
                    idx += str(wordTwo.index(i))
                for i in idx:
                    newStr += "w[" + i + "]+"
                f.write(str(count) + ".\n" + "w = " + wordTwo + "\n"
                        + newStr[0:len(newStr) - 1] + "-->"
                        + wordOne[j] + "\n\n")

with open("wordinwords.txt", "r") as file:
    new_lines = []
    for line in file.readlines():
        if "HARE" not in line and "CONE" not in line:
            new_lines.append(line)
    with open("new_file.txt", "w") as file:
        file.writelines(new_lines)

with open("new_file.txt", "r") as file:
    uppercase_strings = []
    words = file.read().split()
    for word in words:
        for i in [".", ",", "?", "!", ";"]:
            word = word.replace(i, "")
        word = word.replace("PUERTO", "PUERTORICO")
        if word.isupper():
            if word != "A":
                uppercase_strings.append(word)
                if word == "EARTH":
                    uppercase_strings.append("HARE EAR HEART RAT HEAT HART TEAR HAT")
                elif word == "OCEAN":
                    uppercase_strings.append("ONE CONE CANE CAN ACE")
    for i in ["ARITHMETIC", "BUT", "ALL", "JULIUS", "CAESAR"]:
        uppercase_strings.remove(i)
    uppercase_strings.reverse()
    for i in ["MANY", "RICO"]:
        uppercase_strings.pop(uppercase_strings.index(i))
    uppercase_strings.reverse()

count = 0
for i in range(0, len(uppercase_strings), 2):
    count += 1
    main(uppercase_strings[i], uppercase_strings[i + 1], count)