class Polynom:
    def __init__(self, factors: list[float]) -> None:
        self.factors: list[float] = factors.copy()
        self.deg_polynom = len(factors) - 1
        self._pad_to_power_of_two()
    
    def _pad_to_power_of_two(self) -> None:
        n = len(self.factors)
        if n == 0:
            return
        next_power = 1
        while next_power < n:
            next_power <<= 1
        if next_power > n:
            self.factors.extend([0.0] * (next_power - n))