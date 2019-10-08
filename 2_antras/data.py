from math import sin, pi

def linspace(start, end, granularity):
  multiplier = int(1 / granularity)
  expanded_start = int(start * multiplier)
  expanded_end = int(end * multiplier + 1)
  expanded_range = range(expanded_start, expanded_end)
  return [x / multiplier for x in list(expanded_range)]

class Data(object):
  def generate():
    xs = linspace(0.1, 1, 1/22)
    ys = [(1 + 0.6*sin(2*pi*x/0.7)) + (0.3*sin(2*pi*x)/2) for x in xs]
    ys = [[y] for y in ys]
    xs = [[x] for x in xs]

    return [xs, ys]
