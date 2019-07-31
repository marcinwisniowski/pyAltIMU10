# pyIMU

Python Library for **Pololu AltiMU-10** or **MinIMU-9** modules

This library provides an interface for reading data form sensors connected through I²C bus

### Supported sensors

#### Gyroscope

* L3GD20H

#### Accelerometer

* LSM303D

#### Magnetometer

* LSM303D

#### Pressure

* LPS25H
 
### Raspbery Pi 

To use it with Raspberry Pi, the I²C interface need to be enabled.
To verify if it was propery set up

```bash
ls /dev/i2c*
```

