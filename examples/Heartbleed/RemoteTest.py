#!/usr/bin/python2.7
from xshop import test

T = test.TestCase({},target='remote:74.125.21.100')
T.run()
print T.results
