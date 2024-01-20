1. Write program demonstrates how to use regular expressions in Python to match and search for patterns in text.

PROGRAM :-

import re
def basic_regex_example():
    text = input("Enter the text : ")
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_match = re.search(email_pattern, text)
    if email_match:
        print("Email found:", email_match.group())
    else:
        print("Email not found")
    phone_pattern = r'\b\d{10}\b'
    phone_matches = re.findall(phone_pattern, text)
    if phone_matches:
        print("Phone numbers found:", phone_matches)
    else:
        print("Phone numbers not found")
if __name__ == "__main__":
    basic_regex_example()
