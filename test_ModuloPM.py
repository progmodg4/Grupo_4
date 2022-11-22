from modulo_busca import busca 

def test_busca1():
    assert busca('coca', 'supermercado') == (2, 'coca', 3, 42)
def test_busca2():
    assert busca('coca', '') == None
def test_busca3():
    assert busca('coca', 'vulc') == None
def test_busca4():
    assert busca('coca', None) == None
def test_busca5():
    assert busca('', 'supermercado') == None
def test_busca6():
    assert busca('', '') == None
def test_busca7():
    assert busca('Pneu', 'vulc') == None
def test_busca8():
    assert busca('Pneu', 'supermercado') == None
def test_busca9():
    assert busca(None, None) == None
def test_busca10():
    assert busca('Pneu', 'supermercado') == None
