import csv
from Regex import Automate


class MaintainCsvFile():
   
    records_lists_csv = []

    def read_from_csv(self,csv_file_name):
        file = open(csv_file_name, 'r')
        self.records_lists_csv.append(file.read())
        print(self.records_lists_csv)
        Automate().find_phone_number(self.records_lists_csv)

    
    def write_to_csv(self,define_csv_name):
        file = open(define_csv_name, 'a', newline='')
        newRecord = input("Define new record: ")
        file.write(str(newRecord + "\n"))

