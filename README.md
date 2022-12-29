# CubePermutations
Python script to calculate the number of possible cominations of any size rubiks cube.

If you want to be able to say these numbers use http://www.isthe.com/cgi-bin/chongo/number.cgi to convert them to english names.

Currently I have added cubes and megaminxes.

Accuracy falls apart when the output value has over 100,000 digits in it (over 9.99e+99999), you can edit the source code and increase mpmath.mp.dps but it makes calculations take longer.
