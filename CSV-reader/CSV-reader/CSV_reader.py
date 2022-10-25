from asyncio.windows_events import NULL
import csv

class MaintainCsvFile():
   
    classmethod
    def read_from_csv(csv_file_name):
        with open(csv_file_name,'r') as r:
            reader = csv.DictReader(r)
            items = list(reader)

        for item in items:
            print(item)


MaintainCsvFile.read_from_csv("Notatnik")
