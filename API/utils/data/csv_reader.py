import csv
import os
import sys

from models.connect_to_cluster import Conn
from models.vehicle_by_serial_number import VehicleBySerialNumber


class CSVReader(object):

    def __init__(self, infile=None):
        Conn()
        if infile is None:
            self.csv_walker('vsn_data_noheader.csv')
        else:
            self.csv_walker(infile)

    def csv_walker(self, file):
        if os.path.isfile(os.getcwd() + '/utils/data/' + file):
            with open((os.getcwd() + '/utils/data/' + file),
                      'r') as csvfile:
                # next(csvfile)  # Needed for CSV's with a header
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.populate_vehicle_by_serial_number(row)

        elif os.path.isfile(os.path.abspath(sys.path[0] + '/utils/data/' + file)):
            with open(os.path.abspath(sys.path[0] + '/utils/data/' + file),
                      'r') as csvfile:
                # next(csvfile)  # Needed for CSV's with a header
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    print(row)
                    self.populate_vehicle_by_serial_number(row)

    def populate_vehicle_by_serial_number(self, row):
        vbsn = VehicleBySerialNumber()
        vbsn.prefix = row[0][:4]
        vbsn.remainder = row[0][4:]
        vbsn.serial_number = row[0]
        vbsn.vehicle_trim = row[1]
        vbsn.year = row[2]
        vbsn.make = row[3]
        vbsn.model = row[4]
        vbsn.trim_name = row[5]
        vbsn.save()
