original = input("Enter the snippet you want to transform\n")

# split the string of words into a list of words
words = original.split();

# Swap the words and end when the index reaches or passes the middle of the list
for i in range(0, (len(words)//2)):
    temp = words[i]
    words[i] = words[len(words)-1-i]
    words[len(words)-1-i] = temp

# Iterate through each letter of each word
new_words = [""]*len(words)
count = 0
for w in words:
    new_word = ""
    for c in w:
        # swap the cases
        if c.islower():
            new_word+= c.upper()
        else:
            new_word+=c.lower()
    new_words[count] = new_word
    count+=1

# Make the list a continuous string of words, separated by spaces
new_words = " ".join(new_words)

print(new_words)