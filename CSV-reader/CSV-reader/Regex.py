import re

class Automate():

    classmethod
    def find_phone_number(records_lists_to_search):
        phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        for i in records_lists_to_search:
            mo = phoneNumRegex(records_lists_to_search[i])
