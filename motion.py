import time
from OmegaExpansion import AdcExp
import threading

class Motion:

  def __init__(self, address, parent=None):
    print('start motion')
    if parent is None:
      raise ValueError("An Address must be passed into the constructor.");
    self.adc = AdcExp.AdcExp(address=0x48)
    self.parent = parent;
    motionThread = threading.Thread(target=self.listen);
    motionThread.daemon = True;
    motionThread.start();

  def listen(self):
    while 1:
      if self.adc.read_voltage(address) > 3:
        print('active Motion')
        self.parent.motionOn()
      else:
        self.parent.motionOff()
      time.sleep(0.5)