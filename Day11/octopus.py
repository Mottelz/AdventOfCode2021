class Octopus:
    def __init__(self, value: int):
        self._value = value

    def needs_power(self) -> bool:
        return self._value < 10

    def reset(self):
        self._value = 0

    def increase(self):
        self._value += 1

    def end_of_round(self):
        if not self.needs_power():
            self.reset()
