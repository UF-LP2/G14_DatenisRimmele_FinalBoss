import unittest
from src.clase_ship import Ship
from src.clase_cruise import Cruise
from src.clase_cargo import Cargo
import pytest


def test_ship():
    ship1 = Ship(50, 10)
    assert ship1.is_worth_it() == 35
    ship2 = Ship(30, 4)
    assert ship2.is_worth_it() == 24
    with pytest.raises(Exception):
        ship3 = Ship(100, 70)
        assert ship3.is_worth_it() == Exception


def test_cruise():
    cruise1 = Cruise(10, 100, 10)
    assert cruise1.is_worth_it() == 62.5
    cruise2 = Cruise(30, 90, 10)
    assert cruise2.is_worth_it() == 7.5
    with pytest.raises(Exception):
        cruise3 = Cruise(100, 70, 20)
        assert cruise3.is_worth_it() == Exception


def test_cargo():
    cargo1 = Cargo(30, 90, 1000, 20)  # No crea el Cargo
    # assert cargo1.is_worth_it() == 7.5
    with pytest.raises(Exception):
        cargo2 = Cruise(100, 70, 20)
        assert cargo2.is_worth_it() == Exception
