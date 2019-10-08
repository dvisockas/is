from neuron import Neuron

class Net(object):
  def __init__(self, inputs, outputs, hidden_dimensions, activation = 'sigmoid'):
    self.input_size = len(inputs[0])
    self.output_size = len(outputs[0])
    self.layers = []


    for idx, layer in enumerate(hidden_dimensions):
      in_count = self.input_size if idx == 0 else hidden_dimensions[idx - 1]

      layer_neurons = [Neuron(in_count) for layer in hidden_dimensions]

      self.layers.append(layer_neurons)

    self.layers.append([Neuron(hidden_dimensions[-1], activation = 'softmax')])

  def forward(self, input_vector):
    outs = input_vector

    for layer in self.layers:
      tmp_outs = []
      for neuron in layer:
        weighted_values = [neuron.weights[idx] * x_in for idx, x_in in enumerate(outs)]
        tmp_outs.append(sum(weighted_values) + neuron.bias)

      outs = tmp_outs

    return outs



  def backward(parameter_list):
    pass