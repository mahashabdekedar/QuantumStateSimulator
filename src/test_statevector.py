from src.statevector import statevector
import pytest

def test_collapse():
    sv = statevector(2)
    a = sv.measure()
    for i in range(100):
        assert a == sv.measure()

def test_statecreation():
    sv = statevector(2)
    assert sv.is_valid()
    assert sv.is_pure()