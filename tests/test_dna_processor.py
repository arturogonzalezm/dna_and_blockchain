"""
This module contains tests for the DNAProcessor class.
"""
import os
import json
from backend.dna_processing.dna_processor import DNAProcessor
from backend.dna_processing.dna_strategies import (
    ComplementStrategy,
    ReverseComplementStrategy,
    TranscriptionStrategy,
    TranslationStrategy,
    GCContentStrategy,
    BaseCountStrategy
)


def setup_module(module):
    """
    Set up the module by creating a mock codon table JSON file.
    :param module: The module to set up.
    :return: None
    """
    # Create a mock codon table JSON file
    os.makedirs('data', exist_ok=True)
    mock_codon_table = {
        "ATG": "M",
        "GCC": "A",
        "TAA": "Stop",
        "TAG": "Stop",
        "TGA": "Stop"
    }
    with open('data/codon_table.json', 'w') as f:
        json.dump(mock_codon_table, f)


def teardown_module(module):
    """
    Clean up the module by removing the mock codon table JSON file.
    :param module: The module to clean up.
    :return: None
    """
    # Clean up the mock codon table JSON file
    if os.path.exists('data/codon_table.json'):
        os.remove('data/codon_table.json')


def test_complement_strategy():
    """
    Test the ComplementStrategy class.
    :return: None
    """
    processor = DNAProcessor(ComplementStrategy())
    assert processor.process("ATGC") == "TACG"


def test_reverse_complement_strategy():
    """
    Test the ReverseComplementStrategy class.
    :return: None
    """
    processor = DNAProcessor(ReverseComplementStrategy())
    assert processor.process("ATGC") == "GCAT"


def test_transcription_strategy():
    """
    Test the TranscriptionStrategy class.
    :return: None
    """
    processor = DNAProcessor(TranscriptionStrategy())
    assert processor.process("ATGC") == "AUGC"


def test_translation_strategy():
    """
    Test the TranslationStrategy class.
    :return: None
    """
    processor = DNAProcessor(TranslationStrategy())
    assert processor.process("ATGGCC") == "MA"  # Assuming a simple codon table with "ATG" -> "M" and "GCC" -> "A"


def test_gc_content_strategy():
    """
    Test the GCContentStrategy class.
    :return: None
    """
    processor = DNAProcessor(GCContentStrategy())
    assert processor.process("ATGC") == 50.0


def test_base_count_strategy():
    """
    Test the BaseCountStrategy class.
    :return: None
    """
    processor = DNAProcessor(BaseCountStrategy())
    assert processor.process("ATGC") == {'A': 1, 'T': 1, 'G': 1, 'C': 1}
