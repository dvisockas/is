from neuron import Neuron

class Net(object):
  def __init__(self, inputs, outputs, hidden_dimensions, activation = 'sigmoid'):
    self.input_size = len(inputs[0])
    self.output_size = len(outputs[0])
    self.hidden_dimensions = hidden_dimensions
    self.create_neurons()

  def create_neurons(self):
    dims = self.hidden_dimensions
    self.layers = []

    for idx, layer in enumerate(dims):
      in_count = self.input_size if idx == 0 else dims[idx - 1]

      layer_neurons = [Neuron(in_count) for layer in dims]

      self.layers.append(layer_neurons)

    self.layers.append([Neuron(dims[-1], activation = 'tanh')])

  def forward(self, input_vector):
    outs = input_vector

    for layer in self.layers:
      tmp_outs = []

      for neuron in layer:
        tmp_outs.append(neuron.forward(outs))

      outs = tmp_outs

    return outs

  def backward(parameter_list):
    pass