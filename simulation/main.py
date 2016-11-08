
import matplotlib
matplotlib.use('TkAgg')

from pylab import *
import numpy, pycxsimulator

rule = 30
n = 101
t = 0

def Rule (val = rule):
    global rule, rulebin
    rule = int(val)
    rulebin = bin(rule)[2:]
    rulelen = len(rulebin)
    rulebin = (8 - rulelen) * '0' + rulebin
    return val

def N (val = n):
    global n
    n = int(val)
    return val

def applyrule(window):
    return {
        '000': rulebin[7],
        '001': rulebin[6],
        '010': rulebin[5],
        '011': rulebin[4],
        '100': rulebin[3],
        '101': rulebin[2],
        '110': rulebin[1],
        '111': rulebin[0],
    }[window]

def initialize():
    global config, nextconfig, t, rulebin

    t = 0

    rulebin = bin(rule)[2:]
    rulelen = len(rulebin)
    rulebin = (8 - rulelen) * '0' + rulebin

    config = zeros([n, n])
    config[0] = numpy.random.randint(2, size=n)

    nextconfig = zeros([n, n])

def observe():
    global config, nextconfig
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary, interpolation='none')
    axis('off')

def update():
    global config, nextconfig, t

    if (t < n - 1):

        for x in xrange(n):
            window = []
            for dx in [-1, 0, 1]:
                window.append(int(config[t][(x + dx) % n]))
            window = ''.join(map(str, window))

            nextconfig[t] = config[t]
            nextconfig[t + 1][x] = applyrule(window)

        t = t + 1

        config, nextconfig = nextconfig, config

pycxsimulator.GUI(parameterSetters = [Rule, N]).start(
    func=[initialize, observe, update])
