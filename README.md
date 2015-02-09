# project01

Command Usage:
$ python hamming.py <type> <command> <arg1> <arg2>

Where <type> is one of:
asc - ASCII encoding
bin - Binary encoding
Where <command> is one of:
enc <infile> <outfile>
dec <infile> <outfile>
chk <infile>
fix <infile> <outfile>
err <pos> <infile> <outfile>

I also create a compare.py which will used for compare whether the two files are the same. The will test whether my hamming.py works correctly.

Command Usage:
$ python compare.py <arg1> <arg2>

Where arg1 is file_name_1 and arg2 is file_name_2
