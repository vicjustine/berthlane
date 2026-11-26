"""Yard slot allocation within a block."""

BLOCK_ROWS, BLOCK_TIERS = 20, 4


def slots_in_block() -> int:
    return BLOCK_ROWS * BLOCK_TIERS


def free_slots(occupied: int) -> int:
    if occupied > slots_in_block():
        raise ValueError("more containers than slots")
    return slots_in_block() - occupied


def utilisation(occupied: int) -> float:
    return round(100 * occupied / slots_in_block(), 1)
