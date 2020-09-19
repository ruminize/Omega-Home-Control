import time

from switch import Switch

switch = Switch();

start = time.time();
# print(start)
# while (time.time() - start) <= 300.0:
print('start switch')

while 1:

  value = adc.get_last_voltage()
  print(value);
  # rPhoto = 5.0 / value * 1000 - 1000
  # lux = 500/(rPhoto/1000)
  # if lux < 1000:
  if value < 2:
    # relay.set(0, 1)
    # relay.set(1, 1)
    relay.setAllOn();
  else:
    relay.setAllOff()

  # print('Channel 3: %.02f V'%(lux))
  time.sleep(0.5)


.stop_adc()










import time

from OmegaExpansion import AdcExp
from OmegaExpansion import relayExp

defaultChannel = 7;
adc = AdcExp.AdcExp(address=0x48)

relayExp.driverInit(7)
relayExp.setAllChannels(7, 0)


def setRelay(num, state):
  relayExp.setChannel(defaultChannel, num, state)



# print(dir(time))
GAIN = 2/3

adc.start_adc(3, gain=GAIN)

print('Reading ADC expansion channel 3 for 5 seconds')

start = time.time();
print(start)
while (time.time() - start) <= 20.0:

  print('while start ----------')
  value = adc.get_last_voltage()
  rPhoto = 5.0 / value * 1000 - 1000
  lux = 500/(rPhoto/1000)
  if lux > 1000:
    setRelay(1, 1)
  else:
    setRelay(1, 0)

  print('Channel 3: %.02f V'%(lux))
  time.sleep(0.5)


adc.stop_adc()