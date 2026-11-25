import pytest, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / "src"))
from gatein import lane_for, wait_minutes


def test_reefer_routes_to_C():
    assert lane_for("reefer", {"A": 0, "B": 0}) == "C"


def test_dry_picks_emptier_lane():
    assert lane_for("dry", {"A": 5, "B": 2}) == "B"


def test_wait_scales_with_queue():
    assert wait_minutes("A", {"A": 7}) == 21


def test_unknown_lane_raises():
    with pytest.raises(KeyError):
        wait_minutes("Z", {})
