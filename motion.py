import time
from OmegaExpansion import AdcExp
import threading

class Motion:

  def __init__(self, address=None, threshold=None, parent=None):
    print('********** Motion Module Starting **********');

    if address is None:
      raise ValueError("An Address must be passed into the constructor argument 1.");

    if threshold is None:
      raise ValueError("A Threshold must be passed into the constructor argument 2.");

    if parent is None:
      raise ValueError("A Parent self must be passed into the constructor argument 3.");

    self.address = address;
    self.threshold = threshold;
    self.adc = AdcExp.AdcExp(address=0x48)
    self.parent = parent;
    motionThread = threading.Thread(target=self.listen);
    motionThread.daemon = True;
    motionThread.start();

  def listen(self):
    while 1:
      if self.adc.read_voltage(address) > self.threshold:
        self.parent.motionOn();
      else:
        self.parent.motionOff();
      time.sleep(0.5);