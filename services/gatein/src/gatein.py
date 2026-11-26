"""Truck gate-in: assigns an arriving truck to a queue lane. """
""" Will add an overflow lane """

LANES = {"A": 12, "B": 12, "C": 8, "D": 8}


def lane_for(truck_class: str, occupancy: dict) -> str:
    """Reefer and hazardous go to C; everything else to the emptier of A/B."""
    if truck_class in ("reefer", "hazmat"):
        return "C"
    return "A" if occupancy.get("A", 0) <= occupancy.get("B", 0) else "B"


def wait_minutes(lane: str, occupancy: dict) -> int:
    """Three minutes of processing per truck already queued."""
    if lane not in LANES:
        raise KeyError(f"unknown lane: {lane}")
    return occupancy.get(lane, 0) * 3
