import time
from OmegaExpansion import AdcExp
import threading

class Temp:

  def __init__(self, address, parent=None):
    print('start temp')
    if parent is None:
      raise ValueError("An Address must be passed into the Temp constructor.");
    self.address = address;
    self.adc = AdcExp.AdcExp(address=0x48)
    self.parent = parent;
    tempThread = threading.Thread(target=self.listen);
    tempThread..daemon = True;
    tempThread.start();


  def listen(self):
    while 1:
      signal = self.adc.read_voltage(self.address);
      cTemp = (signal - 0.5) * 100;
      fTemp = (cTemp * 9.0 / 5.0) + 32.0;
      print('temp: ', fTemp);
      if fTemp > 88:
        print('active Temp')
        self.parent.tempOn()
      else:
        self.parent.tempOff()
      time.sleep(0.5)


# import time
# from OmegaExpansion import AdcExp

# adc = AdcExp.AdcExp();

# voltsPerDegree = 0.01; # TMP35/36
# outputVoltage = 0.75; # TMP36
# offsetValue = outputVoltage - 25 * voltsPerDegree;

# while 1:

#   signal = adc.read_voltage(1);
#   cTemp = (signal - 0.5) * 100;
#   fTemp = (cTemp * 9.0 / 5.0) + 32.0;

#   # volts = signal * ((5.0 * 1000) / 1024.0);

#   # cTemp = (volts - offsetValue) / voltsPerDegree;
#   #  volts = signal * (5.0/1024);
#   # diff = (volts - 0.75)/0.01;
#   # cTemp = (25.0 * diff);
#   print('--------------')
#   # print(volts);
#   print(cTemp);
#   print(fTemp);

#   time.sleep(1);