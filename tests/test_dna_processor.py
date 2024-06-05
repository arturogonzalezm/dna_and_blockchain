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
    # Clean up the mock codon table JSON file
    if os.path.exists('data/codon_table.json'):
        os.remove('data/codon_table.json')


def test_complement_strategy():
    processor = DNAProcessor(ComplementStrategy())
    assert processor.process("ATGC") == "TACG"


def test_reverse_complement_strategy():
    processor = DNAProcessor(ReverseComplementStrategy())
    assert processor.process("ATGC") == "GCAT"


def test_transcription_strategy():
    processor = DNAProcessor(TranscriptionStrategy())
    assert processor.process("ATGC") == "AUGC"


def test_translation_strategy():
    processor = DNAProcessor(TranslationStrategy())
    assert processor.process("ATGGCC") == "MA"  # Assuming a simple codon table with "ATG" -> "M" and "GCC" -> "A"


def test_gc_content_strategy():
    processor = DNAProcessor(GCContentStrategy())
    assert processor.process("ATGC") == 50.0


def test_base_count_strategy():
    processor = DNAProcessor(BaseCountStrategy())
    assert processor.process("ATGC") == {'A': 1, 'T': 1, 'G': 1, 'C': 1}
