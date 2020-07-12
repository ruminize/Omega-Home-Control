import time

from OmegaExpansion import AdcExp
from OmegaExpansion import relayExp

adc = AdcExp.AdcExp(address=0x48)

relayExp.driverInit(7)
relayExp.setAllChannels(7, 0)


def setRelay(num, state):
  relayExp.setChannel(defaultChannel, num, state)



print(dir(time))
GAIN = 2/3

adc.start_adc(3, gain=GAIN)

print('Reading ADC expansion channel 3 for 5 seconds')

while 1:

  value = adc.get_last_voltage()
  rPhoto = 5.0 / value * 1000 - 1000
  lux = 500/(rPhoto/1000)
  # print('Channel 3: %.02f V'%(lux))


adc.stop_adc()
  
  import time

from OmegaExpansion import AdcExp

adcModule = AdcExp.AdcExp()

while 1:
  # read from adc channel
  a3 = adcModule.read_voltage(3)

  # convert light sensor voltage to lux??
  rPhoto = 5.0 / a3 * 1000 - 1000
  lux = 500/(rPhoto/1000)

  print(lux);
  time.sleep(0.5)