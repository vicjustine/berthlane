import pytest, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from railout import wagons_needed, train_length


def test_exact_fit():
    assert wagons_needed(40) == 20


def test_rounds_up_odd_teu():
    assert wagons_needed(41) == 21


def test_train_length():
    assert train_length(40) == 394.0


def test_negative_raises():
    with pytest.raises(ValueError):
        wagons_needed(-1)
