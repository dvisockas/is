import pdb
from math import exp
from random import random

def activations(weight_bias):
  return {
    'tanh': tanh,
    'sigmoid': sigmoid,
  }

def tanh(x):
  return (2 / ( 1 + exp( -1 * x ) ))-1

def sigmoid(x):
  return 1 / (1 + exp(-x))

class Neuron(object):
  def __init__(self, inputs, activation = 'sigmoid'):
    self.activation = activation
    self.weights = [random() for weight in list(range(0, inputs))]
    self.bias = 0.1

  def forward(self, ins):
    weighted_values = [self.weights[idx] * x_in for idx, x_in in enumerate(ins)]
    weight_bias = sum(weighted_values) + self.bias
    return self.activate(weight_bias)

  def activate(self, weight_bias):
    output = weight_bias
    if self.activation == 'tanh':
      output = tanh(output)
    elif self.activation == 'sigmoid':
      output = sigmoid(output)
  
    return output
