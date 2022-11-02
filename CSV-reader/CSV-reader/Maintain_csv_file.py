import csv
from enum import auto
from Regex import Automate

class MaintainCsvFile():
   
    records_lists_csv = []

    def read_from_csv(self,csv_file_name):

        file = open(csv_file_name, 'r')
        self.records_lists_csv.append(file.read())
        print(self.records_lists_csv)

        Automate().find_all_phones_number(self.records_lists_csv)
        Automate().find_area_code_number(self.records_lists_csv)
        Automate().maybe_find_this(self.records_lists_csv)
        Automate().optional_find_this(self.records_lists_csv)
        Automate().optional_find_this_star(self.records_lists_csv)
        Automate().optional_find_this_plus(self.records_lists_csv)
        Automate().repeat_regex(self.records_lists_csv)
        Automate().you_own_class_znak(self.records_lists_csv)
        Automate().sub_method()
    
    def write_to_csv(self,define_csv_name):

        file = open(define_csv_name, 'a', newline='')
        newRecord = input("Define new record: ")
        file.write(str(newRecord + "\n"))

