"""
day 20
"""


class Module(object):

    def __init__(self, name):
        self.name = name
        self.inputs = list()
        self.outputs = list()

    def proces(self):
        raise NotImplementedError()

    def send(self, pulse):
        for i in self.outputs:
            i.process(pulse)


class Broadcaster(Module):
    def __init__(self, name):
        super(Broadcaster, self).__init__(name)

    def push_button(self):
        """
        Entry point of the whole system
        """
        self.send(False)


class FlipFlop(Module):
    """
    prefix %
    """

    def __init__(self, name):
        super(FlipFlop, self).__init__(name)
        self.state = False

    def process(self, pulse):
        if not pulse:
            self.state = not self.state
            self.send(self.state)


class Conjunction(Module):
    """
    prefix &
    """

    def __init__(self, name):
        super(Conjunction, self).__init__(name)
        self.states = list()

    def process(self, pulse, n):
        """
        Todo: sender does not know n
        """
        self.states[n] = pulse
        out = sum([int(i) for i in self.states]) == len(self.states)
        self.send(not out)


fid = open('input_min.txt')
lines = fid.readlines()

modules = dict()

for line in lines:
    name, outputs = line.split(' -> ')
    outputs = outputs.split(',')

    if name.startswith('%'):
        mod = FlipFlop(name)
        name = name[1:]

    elif name.startswith('&'):
        mod = Conjunction(name)
        name = name[1:]

    elif name == 'broadcaster':
        mod = Broadcaster(name)

    modules.update({name: mod})
    modules[name].outputs.extend(outputs)

    for i in outputs:
        modules[i].inputs.append()


bc = modules['broadcaster']
