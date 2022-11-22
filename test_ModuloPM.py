from modulo_busca import *

def test_busca_nome1():
    assert busca_nome('coca', 'supermercado') == (2, 'coca', 3, 42)
def test_busca_nome2():
    assert busca_nome('coca', '') == None
def test_busca_nome3():
    assert busca_nome('coca', 'vulc') == None
def test_busca_nome4():
    assert busca_nome('coca', None) == None
def test_busca_nome5():
    assert busca_nome('', 'supermercado') == None
def test_busca_nome6():
    assert busca_nome('', '') == None
def test_busca_nome7():
    assert busca_nome('Pneu', 'vulc') == None
def test_busca_nome8():
    assert busca_nome('Pneu', 'supermercado') == None
def test_busca_nome9():
    assert busca_nome(None, None) == None



def test_busca_numero1():
    assert busca_numero('2', 'supermercado') == (2, 'coca', 3, 42)
def test_busca_numero2():
    assert busca_numero('2', '') == None
def test_busca_numero3():
    assert busca_numero('2', None) == None
def test_busca_numero4():
    assert busca_numero('2', 'vulc') == None
def test_busca_numero5():
    assert busca_numero('', 'supermercado') == None
def test_busca_numero6():
    assert busca_numero('', '') == None
def test_busca_numero7():
    assert busca_numero('850', 'vulc') == None
def test_busca_numero8():
    assert busca_numero('850', 'supermercado') == None
def test_busca_numero9():
    assert busca_numero(None, None) == None
