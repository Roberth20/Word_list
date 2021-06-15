from nose.tools import *
from vocabulario.classes import *
import numpy as np

def test_download():
    lista = [["", "", "", 0], ["", "", "", 4], ["", "", "", 5]]
    assert_equal(download(lista), [[["", "", "", 0]],[],[],[], [["", "", "", 4]],[],[],[],[],[]])

def test_open():
    
