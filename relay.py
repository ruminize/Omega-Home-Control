from OmegaExpansion import relayExp

relayExp.driverInit(7)
relayExp.setAllChannels(7, 0)

defaultChannel = 7;

def setRelay(num, state):
  relayExp.setChannel(defaultChannel, num, state)

# setRelay(1, 1)