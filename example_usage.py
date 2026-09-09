"""Example usage for Canonical Huffman Prefix Coding Skill."""
from client import HuffmanCoder

def main():
    print("Executing Huffman Prefix Coder...")
    text = "autonomous agent swarm intelligence"
    codes, enc = HuffmanCoder.build_codes(text)
    print("Huffman Codes:", codes)
    print(f"Original text ({len(text) * 8} bits), Encoded ({len(enc)} bits)")

    dec = HuffmanCoder.decode(enc, codes)
    print("Decoded string:", dec)
    assert dec == text, "Decoded text does not match original"
    print("Canonical Huffman Coding verified successfully!")

if __name__ == "__main__":
    main()
