import time
from OmegaExpansion import AdcExp
import threading

class Light:

  def __init__(self, address, parent=None):
    print('start motion')
    if parent is None:
      raise ValueError("An Address must be passed into the Light constructor.");
    self.address = address;
    self.adc = AdcExp.AdcExp(address=0x48)
    self.parent = parent;
    lightThread = threading.Thread(target=self.listen);
    lightThread.daemon = True;
    lightThread.start();

  def listen(self):
    while 1:
      if self.adc.read_voltage(self.address) > 3:
        print('active Light')
        self.parent.lightOn()
      else:
        self.parent.lightOff()
      time.sleep(0.5)


