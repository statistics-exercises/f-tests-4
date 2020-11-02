import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) :
            myy = scipy.stats.f.pdf( this_x[i], 4, 5 )
            self.assertTrue( np.abs( this_y[i] - myy )<1e-7, "the plot you have generated is not corect" )
