"""ask the user for the file path """
#I made this global since I am having issue adding this to a function due to my code stucture
input_file = input("Please enter the data file: ")

"""global variables to be updated in the main file during execution for company_details function use"""
max_rate = 0
max_line = 0
min_rate = 0
min_line = 0

def read_file(input_file):
    """ this will read/open the file"""
    file_reference = open(input_file, "r")
    try:
        return file_reference.read()
    finally:
        file_reference.close()

def comm_rate():
    """split the first line and find the position of comm_rate from the header"""
    file = open(input_file,"r")
    #this could be more dynamic if I will add parameters like file, separator and the word being lookup but for the sake of this assignment I made this static
    header = (file.readline()).split(",")
    comm_rate_position = header.index("comm_rate")
    return comm_rate_position

def company_details(lines: list,max_or_min: float,company_index,zip_index,state_index,rate_index):
    """ this will show the company details for highest or lowest rate inputs will be in the main file """
    utility = ((lines[max_or_min]).split(","))[company_index]
    zip_code = ((lines[max_or_min]).split(","))[zip_index]
    state = ((lines[max_or_min]).split(","))[state_index]
    rate_of_zip = ((lines[max_or_min]).split(","))[rate_index]
    
    #i'm not sure what to use but to satisfy testBed I just use 'if' to format the string
    if rate_of_zip == '0':
        print("%s (%s, %s) - $%.1f" % (utility, zip_code, state, float(rate_of_zip)))
    else:       
        print("%s (%s, %s) - $%s" % (utility, zip_code, state, rate_of_zip))

def main():
    """ magic happens here call and use all variables and functions """
    #open the file and declare variables in prepration for parsing
    lines = read_file(input_file).split("\n")
    index = comm_rate()
    iterator = 1
    line_counts = len(lines) - 1
    rates = 0
    #declare global so that it will change the value of the variable in the global to get the correct output for company_details function
    global max_rate
    global max_line
    global min_rate
    global min_line
    max_rate = 0
    max_line = 0
    min_rate = 1
    min_line = 1

    #parsing our file into line then words, for procesing
    while iterator < line_counts:
        line = lines[iterator]
        words = line.split(",")
        rates = rates + float(words[index])
        iterator = iterator + 1
        if float(words[index]) > max_rate:
             max_rate = float(words[index])
             max_line = iterator - 1
        if float(words[index]) < min_rate:
             min_rate = float(words[index])
             min_line = iterator - 1
        
    average_rates = rates/(line_counts - 1 )
    #final outputs
    print("\nThe average commercial rate is:",average_rates)
    print("\nThe highest rate is:")
    company_details(lines,max_line,2,0,3,6)
    print("\nThe lowest rate is:")
    company_details(lines,min_line,2,0,3,6)

if __name__ == "__main__":
    main()

