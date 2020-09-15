class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


    def mass(road, mass_asph, width_asph):
        return road._length * road._width * mass_asph * width_asph


task = Road(2, 2)
print(task.mass(2, 2))