from nose.tools import *
from vocabulario.funciones import *
import numpy as np

def test_download():
    lista = [["", "", "", 0], ["", "", "", 4], ["", "", "", 5]]
    assert_equal(download(lista), [[["", "", "", 0]],[],[],[], [["", "", "", 4]],[],[],[],[],[]])

def test_engine_if_non_nan():
    l2 = [["hi", "hola", np.nan, 1], ["box", "caja", np.nan, 1]]
    l1 = []
    l3 = []
    assert_equal(engine(l2, l3, l1, 0, 0), [[], [["hi", "hola", np.nan, 2]], [["box", "caja", np.nan, 0]], 1, 1])

