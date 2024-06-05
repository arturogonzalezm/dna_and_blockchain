"""
This module contains the different strategies for processing DNA sequences.
"""
from backend.bioinformatics_tools.codon_table import CodonTable


class DNAProcessingStrategy:
    """
    DNAProcessingStrategy class for processing DNA sequences.
    """
    def process(self, sequence):
        """
        Process a DNA sequence.
        :param sequence: The DNA sequence to process.
        :return: The processed DNA sequence.
        """
        pass


class ComplementStrategy(DNAProcessingStrategy):
    """
    Strategy for getting the complement of a DNA sequence.
    """
    def process(self, sequence):
        """
        Get the complement of a DNA sequence.
        :param sequence: The DNA sequence.
        :return: The complement of the DNA sequence.
        """
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return ''.join([complement[base] for base in sequence])


class ReverseComplementStrategy(DNAProcessingStrategy):
    """
    Strategy for getting the reverse complement of a DNA sequence.
    """
    def process(self, sequence):
        """
        Get the reverse complement of a DNA sequence.
        :param sequence: The DNA sequence.
        :return: The reverse complement of the DNA sequence.
        """
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return ''.join([complement[base] for base in sequence[::-1]])


class TranscriptionStrategy(DNAProcessingStrategy):
    """
    Strategy for transcribing DNA to RNA.
    """
    def process(self, sequence):
        """
        Strategy for transcribing DNA to RNA.
        :param sequence: The DNA sequence.
        :return: The transcribed RNA sequence.
        """
        return sequence.replace('T', 'U')


class TranslationStrategy(DNAProcessingStrategy):
    """
    Strategy for translating DNA to protein.
    """
    def __init__(self):
        """
        Initialize the TranslationStrategy with a codon table.
        :param codon_table: The codon table to use for translation.
        :type codon_table: dict
        :return: None
        """
        self.codon_table = CodonTable()

    def process(self, sequence):
        """
        Translate a DNA sequence to a protein sequence.
        :param sequence: The DNA sequence to translate.
        :return: The translated protein sequence.
        """
        protein = []
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i + 3]
            if len(codon) == 3:
                amino_acid = self.codon_table.get_amino_acid(codon)
                if amino_acid == 'Stop':
                    break
                protein.append(amino_acid)
        return ''.join(protein)


class GCContentStrategy(DNAProcessingStrategy):
    """
    Strategy for calculating the GC content of a DNA sequence.
    """
    def process(self, sequence):
        """
        Calculate the GC content of a DNA sequence.
        :param sequence: The DNA sequence.
        :return: The GC content of the DNA sequence.
        """
        gc_count = sequence.count('G') + sequence.count('C')
        return gc_count / len(sequence) * 100


class BaseCountStrategy(DNAProcessingStrategy):
    """
    Strategy for counting the occurrences of each base in a DNA sequence.
    """
    def process(self, sequence):
        """
        Count the occurrences of each base in a DNA sequence.
        :param sequence: The DNA sequence.
        :return: A dictionary containing the base counts.
        """
        base_counts = {
            'A': sequence.count('A'),
            'T': sequence.count('T'),
            'G': sequence.count('G'),
            'C': sequence.count('C')
        }
        return base_counts