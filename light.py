import time
from OmegaExpansion import AdcExp
import threading

class Light:

  def __init__(self, address=None, lumens=None, parent=None):
    print('********** Light Module Starting **********');

    if address is None:
      raise ValueError("An Address must be passed into the Light constructor argument 1.");
    
    if lumens is None:
      raise ValueError("An Address must be passed into the Light constructor argument 2.");

    if parent is None:
      raise ValueError("An Address must be passed into the Light constructor argument 3.");

    self.address = address;
    self.lumens = lumens;
    self.adc = AdcExp.AdcExp(address=0x48)
    self.parent = parent;
    lightThread = threading.Thread(target=self.listen);
    lightThread.daemon = True;
    lightThread.start();

  def listen(self):
    while 1:
      value = self.adc.read_voltage(self.address);
      rPhoto = 5.0 / value * 1000 - 1000;
      lux = 500 / (rPhoto / 1000);

      if lux > self.lumens:
        self.parent.lightOff();
      else:
        self.parent.lightOn();
      time.sleep(0.5);


