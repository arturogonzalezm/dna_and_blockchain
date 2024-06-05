"""
This module contains the different strategies for processing DNA sequences.
"""
import json

from backend.logging_utils.singleton_logger import logger


class CodonTable:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.table = {}
        self.load_codon_table("data/codon_table.json")

    def load_codon_table(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.table = json.load(file)
        except FileNotFoundError:
            logger.info(f"File not found: {file_path}")
        except json.JSONDecodeError:
            logger.info(f"Invalid JSON format in file: {file_path}")

    def get_amino_acid(self, codon):
        return self.table.get(codon, '')
