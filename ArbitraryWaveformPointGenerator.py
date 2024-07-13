# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 22:55:45 2024

@author: carne
"""
import numpy as np

class ArbitraryWaveformPointGenerator:
    def __init__(self, amplitude=1.0, frequency=1.0, phase=0.0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase = phase

    def generate_sin_point(self, time):
        """
        Generates a single data point for the arbitrary waveform.

        Args:
            time (float): Time value in seconds.

        Returns:
            float: Value of the waveform at the specified time.
        """
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time + self.phase)

    def generate_triangle_point(self, time):
        """
        Generates a single data point for a symmetric triangle wave.

        Args:
            time (float): Time value in seconds.

        Returns:
            float: Value of the waveform at the specified time.
        """
        half_period = 1 / (2 * self.frequency)
        t_mod = (time + half_period) % (2 * half_period)
        if t_mod < half_period:
            return self.amplitude * (2 * t_mod / half_period - 1)
        else:
            return self.amplitude * (1 - 2 * (t_mod - half_period) / half_period)
