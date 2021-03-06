import numpy as np
from numpy.testing import (assert_almost_equal,
                           assert_equal)

from gridData import Grid


def test_ccp4():
    g = Grid('gridData/tests/test.ccp4')
    POINTS = 192
    assert_equal(g.grid.flat, np.arange(1, POINTS+1))
    assert_equal(g.grid.size, POINTS)
    assert_almost_equal(g.delta, [3./4, .5, 2./3])
    assert_equal(g.origin, np.zeros(3))
