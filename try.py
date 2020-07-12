import time

from OmegaExpansion import AdcExp

adc = AdcExp.AdcExp(address=0x48)

print(dir(time))
GAIN = 2/3

adc.start_adc(3, gain=GAIN)

print('Reading ADC expansion channel 3 for 5 seconds')

while 1:

#  value = adc.get_last_voltage()
#  rPhoto = 5.0 / value * 1000 - 1000
#  lux = 500/(rPhoto/1000)
#  print('Channel 3: %.02f V'%(lux))


adc.stop_adc()