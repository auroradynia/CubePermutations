# CubePermutations
Python script to calculate the number of possible cominations of any size rubiks cube.

If you want to be able to say these numbers use http://www.isthe.com/cgi-bin/chongo/number.cgi to convert them to english names.

Currently I have added cubes and megaminxes.

Printing falls apart when the output value has over 100,000 digits in it (over 9.99e+99999), you can edit the source code and set sys.set_int_max_str_digits(0) to remove the limit but it can take a long time or crash if you ask for a value too large.
