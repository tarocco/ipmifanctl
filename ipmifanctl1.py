from argparse import ArgumentParser
from ipmifanctl import *
from time import sleep


def main():
    parser = ArgumentParser()

    parser.add_argument('--temp-sensor-id')
    parser.add_argument('--lo-temp', type=int, default=30)
    parser.add_argument('--hi-temp', type=int, default=50)
    parser.add_argument('--lo-speed', type=int, default=5)
    parser.add_argument('--hi-speed', type=int, default=50)
    parser.add_argument('--power', type=float, default=2.0)
    parser.add_argument('--update-period', type=float, default=None)
    args = parser.parse_args()

    sensor = TemperatureSensor(args.temp_sensor_id)

    logic = Logic(
        args.lo_temp, args.hi_temp,
        args.lo_speed, args.hi_speed,
        args.power)

    fan_controller = RawFanControl()
    main_controller = Controller(sensor, logic, [fan_controller])

    if args.update_period is None:
        main_controller.update()
    else:
        while True:
            main_controller.update()
            sleep(args.update_period)


if __name__ == '__main__':
    main()
