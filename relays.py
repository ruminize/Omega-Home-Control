from OmegaExpansion import relayExp

class Relays:

  def __init__(self, address):
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