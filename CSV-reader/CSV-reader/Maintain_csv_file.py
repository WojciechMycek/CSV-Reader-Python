import csv
import Regex

class MaintainCsvFile():
   
    records_lists_csv = []

    def read_from_csv(self,csv_file_name):
        file = open(csv_file_name, 'r')
        self.records_lists_csv.append(file.read())
        print(self.records_lists_csv[0])

    classmethod
    def write_to_csv(define_csv_name):
        file = open(define_csv_name, 'w')
        newRecord = input("Define new record: ")
        file.write(str(newRecord))