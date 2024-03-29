class Controller:
    def __init__(self, sensor, logic, fan_controllers):
        self.sensor = sensor
        self.logic = logic
        self.fan_controllers = fan_controllers

    def set_manual_fan_control(self, enabled):
        for fan_controller in self.fan_controllers:
            fan_controller.set_manual(enabled)

    def update(self):
        reading = self.sensor.get_reading()
        self.logic.update(reading)
        if self.logic.value is not None:
            for fan_controller in self.fan_controllers:
                fc_value = int(self.logic.value)
                fan_controller.set_value(fc_value)
