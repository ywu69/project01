__author__ = 'Yuefeng Wu'

import sys

if __name__ == '__main__':
    def file_read(input_filename):
        infile = open(input_filename)
        text = infile.read()
        infile.close()
        return text
    if file_read(sys.argv[1]) == file_read(sys.argv[2]):
        print('Successfully!')
    else:
        print('Unsuccessfully...')