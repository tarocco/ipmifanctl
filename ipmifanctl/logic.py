from functools import reduce


class Logic:
    _temp_peak_window = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.75, 0.5, 0.25]

    @staticmethod
    def lerp(a, b, t):
        return a + (b - a) * t

    def __init__(self, lo_temp, hi_temp, lo_speed, hi_speed, curve_power=2.0,
                 hysteresis=2, feathering=0.5):
        self.lo_temp = lo_temp
        self.hi_temp = hi_temp
        self.lo_speed = lo_speed
        self.hi_speed = hi_speed
        self.curve_power = curve_power
        self.window = self._temp_peak_window
        self.hysteresis = hysteresis
        self.feathering = feathering
        # Initialize to 20 degrees celsius
        self._prior_readings = [20] * len(self._temp_peak_window)
        self._peak_reading = self._prior_readings[0]
        self._value = None

    def update(self, reading):
        reading = max(self.lo_temp, min(reading, self.hi_temp))
        self._prior_readings = [reading] + self._prior_readings[1:-1]
        pairs = zip(self._prior_readings, self._temp_peak_window)
        initial = self._prior_readings[0]
        peak_reading = reduce(lambda E, e: max(E, e[0] * e[1]), pairs, initial)
        difference = abs(peak_reading - self._peak_reading)
        if difference > self.hysteresis:
            self._peak_reading = peak_reading
        temp_range = (self.hi_temp - self.lo_temp)
        speed_range = (self.hi_speed - self.lo_speed)
        interpolant = (self._peak_reading - self.lo_temp) / temp_range
        t = pow(interpolant, self.curve_power) # Power-curved interpolant
        value = self.lo_speed + speed_range * t
        self._value = self.lerp(value, self.value, self.feathering)

    @property
    def value(self):
        return self._value
