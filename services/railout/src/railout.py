"""Rail departure planning: wagons needed for a set of containers."""

TEU_PER_WAGON = 2


def wagons_needed(teu: int) -> int:
    if teu < 0:
        raise ValueError("negative TEU")
    return -(-teu // TEU_PER_WAGON)


def train_length(teu: int, wagon_metres: float = 19.7) -> float:
    return round(wagons_needed(teu) * wagon_metres, 1)
