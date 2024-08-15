import operations

def test_add():
    assert operations.add(1, 2) == 3
    assert operations.add(0, 0) == 0
    assert operations.add(-1, -1) == -2
    assert operations.add(1, 1, 4, 6) == 12
    
def test_sub():
    assert operations.sub(1, 2) == -1
    assert operations.sub(0, 0) == 0
    assert operations.sub(-1, -1) == 0
    
def test_mul():
    assert operations.mul(1, 2) == 2
    assert operations.mul(0, 0) == 0
    assert operations.mul(-1, -1) == 1
    
def test_div():
    assert operations.div(1, 2) == 0.5
    assert operations.div(0, 0) == ZeroDivisionError
    assert operations.div(-1, -1) == 1
