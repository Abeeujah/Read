# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    
    with open("story.txt") as case:
     lines = case.read()
    return lines

def count_words():
    text = read_file_content("story.txt")
    text = text.split()
        
    # [assignment] Add your code here
    dict = {}
    for word in text:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

print(count_words())