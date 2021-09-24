class Motorsykkel:
    def __init__(self, reg_nr, model, km):
        self._reg_nr = reg_nr
        self._model = model
        self._km = km

    def drive(self,km):
        self._km += km

    def get_km(self):
        return self._km

    def print_info(self):
        print(f"Model: {self._model}")
        print(f"Register number: {self._reg_nr}")
        print(f"Km: {self._km}")
        print()