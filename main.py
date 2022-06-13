from postcode import *


def test_formatting(code):
    result = format_code(code)
    print("Formatted postcode " + result)
    return result
   
def test_validate(code):

    result = is_postcode_valid(code)
    if result:
        print("\nThe postcode " + code + " is valid!")
    else: 
         print("\nThe postcode " + code + " is not valid!")

def test_show_details(code):
    show_details_postcode(code)

   

if __name__ == '__main__':

    code = test_formatting('CR26XH')
    test_validate(code)
    test_show_details(code)