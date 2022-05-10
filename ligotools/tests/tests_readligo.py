
from ligotools import readligo

# 4 different tests for the functions to load data /read hdf5 data
# that check to make sure the length of the array is correct (for the two different data sets)

# test 1
def test_read_hdf5_H():
    name = "H-H1_LOSC_4_V2-1126259446-32.hdf5"
	temp = read_hdf5(name)
	assert len(temp) == 131072

# test 2
def test_loaddata_H():
    name = "H-H1_LOSC_4_V2-1126259446-32.hdf5"
    temp = loaddata('data/'+fn_H1, 'H1')
    assert len(temp) == 131072

# test 3
def test_read_hdf5_L():
    name = "L-L1_LOSC_4_V2-1126259446-32.hdf5"
    temp = read_hdf5(name)
    assert len(temp) == 131072

# test 4
def test_loaddata_L():
    name = "L-L1_LOSC_4_V2-1126259446-32.hdf5"
    temp = loaddata('data/'+fn_H1, 'H1')
    assert len(temp) == 131072
