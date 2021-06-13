from nose.tools import *
from vocabulario.funciones import *

def test_download():
    lista = [["hola", "hi", "", 0], ["hola", "hi", "", 4], ["hola", "hi", "", 5]]
    print(download(lista))
    assert_equal(download(lista), [[["hola", "hi", "", 0]], [["hola", "hi", "", 4]],[]])

def teardown():
    print('TEAR DOWN')

def test_basic():
    print('I RAN!')        