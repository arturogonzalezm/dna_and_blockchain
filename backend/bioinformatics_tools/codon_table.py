"""
This module contains the different strategies for processing DNA sequences.
"""
import json

from backend.logging_utils.singleton_logger import logger


class CodonTable:
    """
    Singleton class for loading the codon table.
    """
    _instance = None

    def __new__(cls):
        """
        Singleton class to load the codon table.
        :return: The instance of the CodonTable class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initialize the CodonTable class.
        :return: None
        """
        self.table = {}
        self.load_codon_table("data/codon_table.json")

    def load_codon_table(self, file_path):
        """
        Load the codon table from a JSON file.
        :param file_path: The path to the JSON file.
        :return: None
        """
        try:
            with open(file_path, "r") as file:
                self.table = json.load(file)
        except FileNotFoundError:
            logger.info(f"File not found: {file_path}")
        except json.JSONDecodeError:
            logger.info(f"Invalid JSON format in file: {file_path}")

    def get_amino_acid(self, codon):
        """
        Get the amino acid corresponding to a codon.
        :param codon: The codon.
        :return: The amino acid corresponding to the codon.
        """
        return self.table.get(codon, '')
