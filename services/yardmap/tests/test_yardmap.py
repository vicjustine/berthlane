import pytest, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from yardmap import slots_in_block, free_slots, utilisation


def test_block_size():
    assert slots_in_block() == 80


def test_free_slots():
    assert free_slots(62) == 18


def test_utilisation():
    assert utilisation(62) == 77.5


def test_overfill_raises():
    with pytest.raises(ValueError):
        free_slots(81)
