from OmegaExpansion import relayExp

class Relays:

  def __init__(self, address=None):

    if address is None:
      raise ValueError("An Address must be passed into the constructor.");

    self.defaultAddress = address;
    relayExp.driverInit(address)
    self.setAllOff()

  def set(self, relay, state):
    relayExp.setChannel(self.defaultAddress, relay, state)

  def setAllOff(self):
    relayExp.setAllChannels(self.defaultAddress, 0)

  def setAllOn(self):
    relayExp.setAllChannels(self.defaultAddress, 1);

  def channel(self):
    return self.defaultAddress;

  def read(self, channel):
    return relayExp.readChannel(self.defaultAddress, channel);