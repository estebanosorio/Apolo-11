from main import main_menu, mostrar_menu
from report import Report
from parameters_editor import ParametersEditor
from unittest.mock import patch
import pytest

def test_main_menu_option_1():
    rp = Report()
    with patch("builtins.input", side_effect=["1"]):
        main_menu(1, rp) 

def test_main_menu_option_2():
    rp = Report()
    with patch("builtins.input", side_effect=["2"]):
        main_menu(2, rp)

def test_main_menu_option_5():
    rp = Report()
    with patch("builtins.input", side_effect=["5"]):
        assert main_menu(5, rp) is None
