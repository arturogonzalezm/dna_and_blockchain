"""
This module contains the different strategies for processing DNA sequences.
"""
from backend.bioinformatics_tools.codon_table import CodonTable


class DNAProcessingStrategy:
    def process(self, sequence):
        pass


class ComplementStrategy(DNAProcessingStrategy):
    def process(self, sequence):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return ''.join([complement[base] for base in sequence])


class ReverseComplementStrategy(DNAProcessingStrategy):
    def process(self, sequence):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return ''.join([complement[base] for base in sequence[::-1]])


class TranscriptionStrategy(DNAProcessingStrategy):
    def process(self, sequence):
        return sequence.replace('T', 'U')


class TranslationStrategy(DNAProcessingStrategy):
    def __init__(self):
        self.codon_table = CodonTable()

    def process(self, sequence):
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
    def process(self, sequence):
        gc_count = sequence.count('G') + sequence.count('C')
        return gc_count / len(sequence) * 100


class BaseCountStrategy(DNAProcessingStrategy):
    def process(self, sequence):
        base_counts = {
            'A': sequence.count('A'),
            'T': sequence.count('T'),
            'G': sequence.count('G'),
            'C': sequence.count('C')
        }
        return base_counts