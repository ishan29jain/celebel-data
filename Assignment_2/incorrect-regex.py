import re

def validate_regex():
    try:
        regex = input()
        re.compile(regex)
        print(True)
    except re.error:
        print(False)

validate_regex()
