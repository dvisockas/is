from math import exp

class Neuron(object):
  def __init__(self, inputs, activation = 'sigmoid'):
    self.activation = activation
    self.weights = list(range(0, inputs))
    self.bias = 0.1

  def forward(self, ins):
    weighted_values = [self.weights[idx] * x_in for idx, x_in in enumerate(ins)]
    weight_bias = sum(weighted_values) + self.bias
    return self.activate(weight_bias)

  def activate(self, weight_bias):
    return activations[self.activation](weight_bias)

  def activations(weight_bias):
    return {
      'tanh': tanh,
      'sigmoid': tanh,
      'softmax': tanh,
    }

  def tanh(x):
    return (2 / ( 1 + exp( -1 * x ) ))-1


