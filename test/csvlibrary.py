#-*- coding: utf-8 -*-
import sys
import csv
from time import localtime, strftime
reload(sys)
sys.setdefaultencoding('utf-8')

def write_CSV_file(filename,*itemlist):
    """ This Keyword saves list to 'csv' File with timestamp.\n
    If you input file name like "query" and then output file name will be "Test.csv".\n
    Return value is full name with timestamp. e.g. "Test.csv"\n
    """
    items = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in itemlist]
    fi=filename + ".csv"
    with open(fi, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(items)
    return fi

def read_CSV_file(filename):
	'''This creates a keyword named "Read CSV File"

	This keyword takes one argument, which is a path to a .csv file. It
	returns a list of rows, with each row being a list of the data in 
	each column.
	'''
	data = []
	with open(filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)
	return data
