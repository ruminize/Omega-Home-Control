import time

from OmegaExpansion import relayExp
from relays import Relays
from motion import Motion
from light import Light
from temp import Temp

class Switch:

  def __init__(self):

    self.motionDetected = False;
    self.relay = Relays(7);
    self.relay.setAllOff();
    self.motion = Motion(0, 3, self);
    self.light = Light(3, 1000, self);
    self.temp = Temp(1, 85, self);

    self.start = time.time();

    while True:
      print('********** Switch Module Starting **********');
      time.sleep(5);

  def motionOn(self):
    self.motionDetected = True;
    self.relay.set(0, 1);

  def motionOff(self):
    self.motionDetected = False;
    self.relay.set(0, 0);

  def tempOn(self):
    self.relay.set(1, 1);

  def tempOff(self):
    self.relay.set(1, 0);

  def lightOn(self):
    if self.motionDetected and self.relay.read(0) == 0:
      self.relay.set(0, 1);

  def lightOff(self):
    if not self.motionDetected and self.relay.read(0) == 1:
      self.relay.set(0, 0);
