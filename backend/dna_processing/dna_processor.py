"""
This module contains the different strategies for processing DNA sequences.
"""


class DNAProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, sequence):
        return self.strategy.process(sequence)
