import csv
def galactic_speed_percentile(galactic_speed: float):
    """The "galaxies.csv" file is a .csv file WITHOUT a header. It describes
    the speed of 82 different galaxies (identified by numbers). The first column
    in the .csv lists the number of a galaxy, and the second column lists that
    galaxy's speed in km/sec. For instance, galaxy number 1 is traveling at 
    9172km/sec relative to our sun.
    
    This function calculates the percentage of listed galaxies that are 
    travelling faster than a given speed.

    Arguments:
        - galactic_speed: a float representing a speed in km/sec

    Returns: a float representing the number of galaxies travelling faster 
    than that speed.

    Examples:
        - an input of 50.0 would result in a return value of 100.00, because
        100% of the listed galaxies are travelling faster than 50km/sec
        - an input of 20830.0 would result in a return value of 50.0, because
        50% of the listed galaxies are travelling faster than 20830km/sec
        - an input of 999999.0 would result in a return value of 0.0, because
        0% of the listed galaxies are travelling faster than 999999km/sec 
    """
    
    pass