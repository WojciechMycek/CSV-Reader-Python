import re

class Automate():

    def find_phone_number(self,records_lists_to_search):
        phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        for i in range(len(records_lists_to_search)):
            mo = phoneNumRegex.findall(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo)