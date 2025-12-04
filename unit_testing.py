import pytest

def main():
    test_squ()
    test_str() # Call test_str to check for TypeError

# Subject function
def squ(n):
  return n*n

def test_squ():
  assert squ(3) == 9
  assert squ(4) == 16
  # assert squ("hello") #as it causes TypeError and should be handled by test_str

def test_str():
    with pytest.raises(TypeError):
        squ("hello")

if __name__ == "__main__":
    main()
