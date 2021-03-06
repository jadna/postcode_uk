import json
import requests
import sys
import re

def format_code(postcode, join: bool=True):

    """
    Input: a badly formatted postcode as string, possibly without spaces.
    Output: a standard formatted postcode.
    """
    # Minimum size is A99AA, 5 letters
    # Maximum size is DN55 1PT, 8 letters
    if len(postcode) < 5 or len(postcode) > 9:

        print('Postcode length "{}" is invalid'.format(len(postcode)))
        return False
    
    # Convert to UPPER the letters
    postcode = postcode.upper()

    # From start up to the last 3 letters
    outward_code = postcode[:-3].strip()
    # Only the last 3 letters
    inward_code = postcode[-3:].strip()
    if join:
        return outward_code + ' ' + inward_code
    return outward_code, inward_code


def is_postcode_valid(postcode):

    """
        Uses regular expressions to test the pattern of the postcode.
        Test inward and outward code seperately
    """

    inward_code = postcode.split(" ")[1]
    outward_code = postcode.split(" ")[0]

    if re.match("^[0-9][ABD-HJLNP-UW-Z]{2}$", inward_code) is None:
        return False
    if re.match("^[A-PR-UWYZ]{1}(([0-9]{1,2}|[0-9][A-HJKS-UW])|([A-HK-Y]{1}([0-9]{1,2}|[0-9][A-Z])))$", outward_code) is None:
        return False
    
    return True


def get_postcode_data(postcode):
    """
        Uses requests to retrieve data from postcode api.
    """
    try:
        url = requests.get('https://api.postcodes.io/postcodes/' + postcode)
        postcode_data = json.loads(url.text)

        return postcode_data

    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def show_details_postcode(postcode):
    """ The postcodes api provides latitude and longitude coordinates.
        I use these with the geopy api.
        Geopy can be found here: https://github.com/geopy/geopy
    """

    if is_postcode_valid(postcode):
        postcode_data = get_postcode_data(postcode)
        result = postcode_data["result"]

        inward_code = postcode.split(" ")[1]
        outward_code = postcode.split(" ")[0]
       
        print("\nShowing details for postcode: " + postcode.upper())
        print("     Valid Postcode: {}".format(str(is_postcode_valid(postcode))))
        print("     Outward Code: {}".format(outward_code))
        print("     Inward Code: {}".format(inward_code))
        print("     Parish: {}".format(result["parish"]))
        print("     Longitude: {} Latitude: {}\n".format(str(result["longitude"]), str(result["latitude"])))

 
        