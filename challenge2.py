import csv
def generate_coloured_text(colour_name: str):
    """The "colours865.csv" file is a .csv file with a header. It lists facts 
    about 865 different colours, including their RGB values, hexadecimal 
    representation, and english name. 
    
    This function generates an html element to demonstrate a named colour from 
    the file.

    Arguments:
        - colour_name: a string representing a named colour from the 
        "colours_865.csv" file.
    
    Returns: a string representing an html <p> element that contains the 
    colour_name string as its text content, with inline css setting the "color" 
    property to that color.

    Example: supplying the argument "Alizarin Crimson" would result in a return 
    value of '<p style="color:#e32636;">Alizarin Crimson</p>'
    """
    with open("colours_865.csv") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row in reader:
            colour_name_from_csv = row[2]
            colour_hex_code_from_csv = row[1]
            if colour_name.lower() == colour_name_from_csv.lower():
                return f"<p style = 'color:{colour_hex_code_from_csv};'>{colour_name_from_csv}</p>"