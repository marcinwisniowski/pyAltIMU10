# coding=utf-8
"""
pyIMU: Main module

Copyright 2019 Marcin Filip Wiśniowski
Licensed under Apache Software License
"""


class IMU(object):
    """
    Generic class for Pololu IMU modules
    """

    def __init__(self):
        super(IMU, self).__init__()

    def __del__(self):
        pass

    def enable(self, sensor):
        pass


class MinIMU9v3(IMU):
    """
    Class that combines sensors:
     * L3GD20H - Gyroscope
     * LSM303D - Accelerometer and Magnetometer
    """


class AltIMU10v4(MinIMU9v3):
    """
    Class extends MinIMU9v3 with access to additional sensor:
     * LPS25H - Barometer
    """