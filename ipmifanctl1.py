from argparse import ArgumentParser
from ipmifanctl import *


def main():
    parser = ArgumentParser()
    parser.add_argument("temp_sensor_id")
    parser.add_argument("lo_temp", type=int, default=30)
    parser.add_argument("hi_temp", type=int, default=50)
    parser.add_argument("lo_speed", type=int, default=5)
    parser.add_argument("hi_speed", type=int, default=50)
    parser.add_argument("power", type=float, default=2.0)
    args = parser.parse_args()


    print(dir(args))
    sensor = TemperatureSensor(args.temp_sensor_id)

    logic = Logic(
        args.lo_temp, args.hi_temp,
        args.lo_speed, args.hi_speed,
        args.power)

    fan_controller = RawFanControl()
    main_controller = Controller(sensor, logic, [fan_controller])

    main_controller.update()


if __name__ == '__main__':
    main()
