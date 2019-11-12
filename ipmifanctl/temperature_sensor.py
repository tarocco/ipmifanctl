import subprocess


class TemperatureSensor:
    backend = 'ipmitool'
    _get_temp_prefix = ['ipmitool', 'sensor', 'reading']

    def __init__(self, id, units='degrees C'):
        self.id = id
        self.units = units

    def get_reading(self):
        cmd = self._get_temp_prefix + [self.id]
        proc = subprocess.run(cmd, capture_output=True)
        name, reading_str = proc.stdout.split('|')
        reading = int(reading_str.strip())
        return reading
