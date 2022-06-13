# PostCodes

## Description
Write a library that supports validating and formatting post codes for UK.
The details of which post codes are valid and which are the parts they consist of can be found at
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.

This library uses the fastApi and postcodes.io API.

## Contents of Library

The postcodes library file is postcode.py
Inside the library there is a number of methods available to use.

## Contents of Library

The postcodes library file is postcode.py
Inside the library there is a number of methods available to use.

```python

def format_code(postcode: str, join: bool=True):

```

This function returns a string, or a tuple, depending if the join param is True.

```python

def is_postcode_valid(postcode):

```

This function takes in a postcode as an argument and returns true if it is a valid postcode and false if it is invalid. This uses regular expressions to test both the inward code and outward code seperately.


```python

def show_details_postcode(postcode):

```

This function takes in a postcode as an argument and prints the following:

Validity of Postcode
Latitude and Longitude
Parish
Outward Code
Inward Code


## Installation

###### Clone the Repository

`https://github.com/jadna/postcode_uk.git`

###### Installing and Running

```python

   #Project using Python3

   # Install pip dependencies
   pip install -r requirements.txt

   # Run the Project
   python3 main.py 

   # Run the tests.py file with the unittest module
   python3 -m unittest tests.py

```

###### Running with fastApi

```python

   #Project using Python3

   # Install pip dependencies
   pip install -r requirements.txt

   # Run the Project
   python3 postcode_api.py

   # Access the api with the following urls
   
   # Documentation
   http://127.0.0.1:8000/docs

   # Formatted postcode
   http://127.0.0.1:8000/formatted/details/B33 208TH

   # Valid postcode
   http://127.0.0.1:8000/valid/details/B33 208TH

   # Details postcode
   http://127.0.0.1:8000/postcode/details/B33 208TH

```

## Usage

To import any function from the postcode library:

```python

# if file is at root directory
from postcode import [function_name(s)]

```

for example
```python
# In tests.py (at root)
from postcode import *

```
This imports all functions from our library.

Simply call these imported functions as you wish.


# ThreeFive

It prints the numbers from 1 to 100. But for multiples of three it prints “Three” instead of the number and for multiples of five it prints “Five”. For numbers that are multiples of three and five, prints “ThreeFive”.

###### Running

```python

    python3 threefive.py

```