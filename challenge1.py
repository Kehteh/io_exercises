import csv
def count_mentions(some_colour_word: str):
    """The "colours_20_simple.csv" is a .csv file with a header. It lists facts 
    about 20 different colours, including their RGB values, hexadecimal 
    representation, and english name. 
    
    This function counts the number of times a given colour descriptor is 
    mentioned in the "English" column of the "colours_20_simple.csv" file.

    Arguments: 
        - some_colour_word: a string that describes a colour
    
    Returns: an integer representing the count of times that the 
    some_colour_word string appears in the "English" column of the 
    "colours_20_simple.csv" file. 

    Example: the input "beige" would return a result of 4, since there are 4 
    colours whose name includes the word beige. 
    """
    # hint - the .lower() method will convert a Python string to lowercase.
    # https://www.w3schools.com/python/ref_string_lower.asp


    
    # parse the file
    with open("colours_20_simple.csv") as color_csv:
        csv_reader = csv.reader(color_csv)
        next(csv_reader)
        # ^^^^^^^^^^^^^^^^ skip the headers

        # count the number of times some_colour_word appears
        count = 0
        for row in csv_reader:
            if row:
                colour_name_from_csv = row[2]
                if some_colour_word.lower() in colour_name_from_csv.lower():
                    count += 1
    return count