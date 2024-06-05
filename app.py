"""
Streamlit application that processes a DNA sequence and stores the results in a blockchain.
"""
import time
import pandas as pd
import streamlit as st
from backend.simple_blockchain.blockchain import Blockchain, Block
from backend.dna_processing.dna_processor import DNAProcessor
from backend.dna_processing.dna_strategies import (
    ComplementStrategy,
    ReverseComplementStrategy,
    TranscriptionStrategy,
    TranslationStrategy,
    GCContentStrategy,
    BaseCountStrategy
)


def main():
    st.title("DNA Blockchain Application")

    # Input DNA sequence
    dna_sequence = st.text_input("Enter a DNA sequence:", value="ATGCATGCATGCATGC")

    if st.button("Process DNA"):
        # Validate the DNA sequence
        if not all(base in 'ATGC' for base in dna_sequence):
            st.error("Invalid DNA sequence. Please enter a sequence containing only A, T, G, and C.")
            return

        # Create DNA processors
        complement_processor = DNAProcessor(ComplementStrategy())
        reverse_complement_processor = DNAProcessor(DNAProcessor(ReverseComplementStrategy()))
        transcription_processor = DNAProcessor(TranscriptionStrategy())
        translation_processor = DNAProcessor(TranslationStrategy())
        gc_content_processor = DNAProcessor(GCContentStrategy())
        base_count_processor = DNAProcessor(BaseCountStrategy())

        # Create a new blockchain
        blockchain = Blockchain()

        # Process the DNA sequence
        data = {
            "DNA Sequence": dna_sequence,
            "Complementary Sequence": complement_processor.process(dna_sequence),
            "Reverse Complement Sequence": reverse_complement_processor.process(dna_sequence),
            "Transcribed RNA Sequence": transcription_processor.process(dna_sequence),
            "Translated Protein Sequence": translation_processor.process(dna_sequence),
            "GC Content (%)": gc_content_processor.process(dna_sequence),
            "Base Counts": base_count_processor.process(dna_sequence)
        }

        # Create a new block with the processed data
        block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash)
        blockchain.add_block(block)

        # Display the blockchain
        st.subheader("Blockchain")
        for block in blockchain.chain:
            st.write(f"Block #{block.index}")
            st.write(f"Timestamp: {block.timestamp}")
            st.write("Data:")
            st.json(block.data)
            st.write(f"Previous Hash: {block.previous_hash}")
            st.write(f"Hash: {block.hash}")
            st.write("---")

        # Check the validity of the blockchain
        is_valid = blockchain.is_chain_valid()
        st.write(f"Is blockchain valid? {is_valid}")

        # Display the DNA processing results in a transposed DataFrame
        df = pd.DataFrame([data])
        transposed_df = df.transpose()
        transposed_df.columns = ['Value']
        st.subheader("DNA Processing Results")
        st.write(transposed_df)


if __name__ == "__main__":
    main()
