#sets the file as a string
def file_print(): 
    file_path = "books/frankenstein.txt"
    with open(file_path) as f: 
        file_contents = f.read()
    return file_contents, file_path

#counts the words
def count_words(): 
    file_contents, _ = file_print()
    words = file_contents.split() #splits each word 
    counter = len(words) #counts the amount of words
    return counter

#counts each letter
def count_chars(): 
    file_contents, _ = file_print()
    counter = {}
    for char in file_contents: #for each character...
        if char.isalpha(): #if character is a letter, then...
            char = char.lower() #lowers any caps
            if char in counter: #if letter is counted
                counter[char] += 1 #adds +1 to counter of that letter
            else:
                counter[char] = 1 #if new letter, then adds new key to dict
    return counter

#Aggregates letter dictionary
def generate_report(count_chars):
    sorted_chars = sorted(count_chars.items(), key=lambda item: item[1], reverse=True)
    lines=[]
    for letter, count in sorted_chars:
        lines.append(f"The letter {letter} was found {count} times.")
    return "\n".join(lines)




#calls functions and then prints
def main(): 
    file_contents, file_path = file_print()
    word_count = count_words()
    char_count = count_chars()
    report = generate_report(char_count)
    
    print(file_contents)
    print(f"\n---Report of {file_path}---")
    print(f"\nWord count: {word_count}")
    print(f"\n{report}")
    print("---End of Report---")

if __name__ == "__main__": #only runs if executes (and not imported)
    main()