class Neuron(object):
  def __init__(self, inputs, activation = 'sigmoid'):
    self.weights = list(range(0, inputs))
    self.bias = 0.1
