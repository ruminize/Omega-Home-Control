import time
from OmegaExpansion import AdcExp
import threading

class Temp:

  def __init__(self, address=None, temp=None, parent=None):
    print('********** Temp Module Starting **********');

    if address is None:
      raise ValueError("An Address must be passed into the constructor argument 1.");

    if threshold is None:
      raise ValueError("A Threshold must be passed into the constructor argument 2.");

    if parent is None:
      raise ValueError("A Parent self must be passed into the constructor argument 3.");

    self.address = address;
    self.temp = temp;
    self.adc = AdcExp.AdcExp(address=0x48)
    self.parent = parent;
    tempThread = threading.Thread(target=self.listen);
    tempThread..daemon = True;
    tempThread.start();

  def listen(self):
    time.sleep(5);
    while 1:
      signal = self.adc.read_voltage(self.address);
      cTemp = (signal - 0.5) * 100;
      fTemp = (cTemp * 9.0 / 5.0) + 32.0;

      if fTemp > self.temp and fTemp < 120:
        self.parent.tempOn();
      else:
        self.parent.tempOff();
      time.sleep(0.5);