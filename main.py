import spidev

ad420 = spidev.SpiDev()

bus = 0
device = 0
ad420.open(bus, device)

ad420.max_speed_hz = 100000
ad420.lsbfirst = False

ad420.mode = 0b00


ad420.writebytes([0x7f, 0x0])
