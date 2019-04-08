# led-ws2801

Python library for customizing light patterns run on an LED strip. The library acts as a higher-level API so that you only need to focus on coding the pattern logic.

The library offers built-in support for WS2801 LED strips driven by Adafruit's library and for simulating an LED strip using TkInter's GUI library.

See [led_desktop_patterns.py](https://github.com/leodenault/led-ws2801/blob/master/src/led_desktop_patterns.py) and [led_holiday_patterns.py](https://github.com/leodenault/led-ws2801/blob/master/src/led_holiday_patterns.py) for example usages of the library.

## Getting Started

To get started with using this library you'll need to clone or download the files in the repository. Once you have your project referencing the library you'll need to download the library for each of the devices on which you wish to display your patterns.

### Adafruit

This library offers built-in support for displaying patterns on a WS2801 LED strip using the [Adafruit library](https://github.com/adafruit/Adafruit_Python_WS2801). Please follow their [instructions](https://github.com/adafruit/Adafruit_Python_WS2801/blob/master/README.md) for installing their library. Once it is installed you will be able to use the API offered by this library to communicate with the LED strip.

### TkInter

This library also offers built-in support for displaying patterns on-screen using Python's [TkInter](https://wiki.python.org/moin/TkInter) library mainly for visually testing patterns before deploying them to the Raspberry Pi. Please follow the [instructions](https://tkdocs.com/tutorial/install.html) on installing TkInter on your development device before attempting to display patterns through a GUI using this library.

### Other Devices

If you wish to integrate with other devices using this library, you may do so by creating a new implementation of [Device](https://github.com/leodenault/led-ws2801/blob/master/src/display/device.py).
