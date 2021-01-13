import re

def prompt_filename():
    file_name = input("Please enter the filename: ")
    return file_name

def parse_file(filename,givenword):
    count = 0
    with open(filename,encoding="utf8") as file:
        for line in file:
            line = line.lower()
            words = line.split()
            for word in words:
                match = re.search(".*" + givenword,word)
                if match:
                #if word == givenword:
                    count += 1
                
    return count
    
def count_word():
    word = input("Enter a word: ")
    return word

def main():
    file_name = prompt_filename()
    word = count_word()
    print("Opening file",file_name)
    count = parse_file(file_name, word)
    print("The word %s occurs %i times in this file." % (word, count))


if __name__ == "__main__":
    main()
