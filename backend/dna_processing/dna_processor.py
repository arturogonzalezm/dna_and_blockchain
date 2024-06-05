"""
This module contains the different strategies for processing DNA sequences.
"""


class DNAProcessor:
    """
    DNAProcessor class for processing DNA sequences using a strategy.
    """
    def __init__(self, strategy):
        """
        Initialize the DNA processor with a strategy.
        :param strategy: The strategy to use for processing DNA sequences.
        :type strategy: DNAProcessingStrategy
        :return: None
        """
        self.strategy = strategy

    def process(self, sequence):
        """
        Process a DNA sequence using the strategy.
        :param sequence: The DNA sequence to process.
        :return: The processed DNA sequence.
        """
        return self.strategy.process(sequence)
