# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:58:39 2024

@author: carne
"""

import ArbitraryWaveformPointGenerator
import DataSampleAndTransmit


# constants
DATA_FREQUENCY = 0.1
SAMPLE_RATE = 1
TRANSMIT_RATE = 1.25
TIME_STEP = .05
DATA_AMPLITUDE = 1
NUM_ITERATIONS = 1000

# create the Arbitrary waveform generator
awpg1 = ArbitraryWaveformPointGenerator.ArbitraryWaveformPointGenerator(DATA_AMPLITUDE, DATA_FREQUENCY, 0)
data1 = DataSampleAndTransmit.DataSampleAndTransmit(SAMPLE_RATE, TRANSMIT_RATE)


# main loop
t = 0
for i in range(NUM_ITERATIONS):
    s = awpg1.generate_sin_point(t)
    print(i, t, s)
    data1.sample(t,s)
    data1.transmit_data(t)
    t = t + TIME_STEP


data1.plot_transmitted_data()
data1.plot_sampled_data()
    