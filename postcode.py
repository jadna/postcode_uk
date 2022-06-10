import json
import requests
import sys
import re

class ValidationError(Exception):
    """Validation error."""
    pass

def format_code(postcode, join: bool=True):

    """
    Input: a badly formatted postcode as string, possibly without spaces.
    Output: a standard formatted postcode.
    Raises ValidationError, if the postcode length is invalid.
    """
    # Minimum size is A99AA, 5 letters
    # Maximum size is DN55 1PT, 8 letters
    if len(postcode) < 5 or len(postcode) > 9:
        #return False, 'Postcode "{}" is invalid'.format(postcode)
        raise ValidationError('Postcode length "{}" is invalid'.format(len(postcode)))
    
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

    postcode = format_code(postcode)

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
