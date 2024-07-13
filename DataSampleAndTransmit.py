# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:05:07 2024

@author: carne
"""
import matplotlib.pyplot as plt

class DataSampleAndTransmit:
    def __init__(self, sample_rate=100, transmit_rate=100):
        self.sample_rate = sample_rate
        self.sample_period = 1/sample_rate
        self.next_sample_time = self.sample_period
        self.data_sample_buffer = []  # Store sample data here
        
        self.transmit_rate = transmit_rate
        self.transmit_period = 1/transmit_rate
        self.next_transmit_time = self.transmit_period
        self.transmitted_data = []  # Represent the transmitted data

    def sample(self, time, value):
        """
        Samples a data value at the specified time and adds it to the buffer.

        Args:
            value: The data value to sample.
            time (float): Time value in seconds.
        """
        if time >= self.next_sample_time:
            self.data_sample_buffer.append((time, value))  # Store (time, value) pairs
            self.next_sample_time = self.next_sample_time + self.sample_period
            

    def transmit_data(self, time):
        """
        Transmits a data value from the data sample buffer at the specified time

        Args:
            time (float): Time value in seconds.
        """
        if time >= self.next_transmit_time:
            if len(self.data_sample_buffer) > 0:
                t, data = self.data_sample_buffer[-1]
                self.transmitted_data.append((time, data))
            else:
                self.transmitted_data.append((time,0))
            self.next_transmit_time = self.next_transmit_time + self.transmit_period
            
    def plot_all(self):
        """
        Plots the data stored in the buffer.
        """
        if not self.data_sample_buffer:
            print("No data to plot.")
            return

        sample_indices, values = zip(*self.data_sample_buffer)
        plt.scatter(sample_indices, values, marker='o', color='b', label='Sample Data')
        sample_indices, values = zip(*self.transmitted_data)
        plt.scatter(sample_indices, values, marker='o', color='r', label='Transmitted Data')
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Sampled Data")
        plt.grid(True)
        plt.legend()
        plt.show()


    def plot_transmitted_data(self):
        """
        Plots the data stored in the buffer.
        """
        if not self.data_sample_buffer:
            print("No data to plot.")
            return

        sample_indices, values = zip(*self.transmitted_data)
        plt.scatter(sample_indices, values, marker='o', color='r', label='Transmitted Data')
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Sampled Data")
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_sampled_data(self):
        """
        Plots the data stored in the buffer.
        """
        if not self.data_sample_buffer:
            print("No data to plot.")
            return

        sample_indices, values = zip(*self.data_sample_buffer)
        plt.scatter(sample_indices, values, marker='o', color='b', label='Sample Data')
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Sampled Data")
        plt.grid(True)
        plt.legend()
        plt.show()
