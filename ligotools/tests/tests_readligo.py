
from ligotools import readligo

def test_read_hdf5():
name = "H-H1_LOSC_4_V2-1126259446-32.hdf5"
strain_H1, time_H1, chan_dict_H1 = read_hdf5(name)

    assert len(strain_H1) == 131072

def test_toy_0():
    assert toy(0) == 1

def test_toy_1():
    assert toy(1) == 2