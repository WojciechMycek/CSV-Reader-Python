import csv

class MaintainCsvFile():
   
    classmethod
    def read_from_csv(csv_file_name):
        print("lol")
        file = open(csv_file_name, 'r')
        print(file.read())

    classmethod
    def write_to_csv(define_csv_name):
        file = open(define_csv_name, 'w')
        newRecord = input("Define new record: ")
        file.write(str(newRecord))