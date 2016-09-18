from pandas import Series
import numpy
def chi_sq(o_list,e_list):
    o = Series(o_list)
    e - Series(e_list)
    chi_sq = ((o-e)**2)/e

    return numpy.sum(chi_sq)

#Example of http://www.stat.berkeley.edu/~stark/SticiGui/Text/chiSquare.htm
#Exercise 31-4.

o = [1209,189,10,41,51]
e = [i*1500/100 for i  in [80.29,12.06,0.79,2.92,3.94]]
chi_sq_test_statistic = chi_sq(o,e)
print(chi_sq_test_statistic)
