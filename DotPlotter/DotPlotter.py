from pathlib import Path
import csv
import os.path


class Plotter:

    def __init__(self):
        pass

    def LoadCSV(self,csv_path):

        if os.path.isfile(csv_path)==False:
            print("File {} not found".format(csv_path))
            return False

        with open('file.csv', 'r') as f:
            reader = csv.reader(f)
            self.Points = list(reader)