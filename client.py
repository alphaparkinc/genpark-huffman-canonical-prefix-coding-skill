"""
Autonomous Agent Canonical Huffman Prefix Coding Skill
Pure Python Standard Library implementation.
"""
import heapq
from collections import Counter
from typing import Dict, Tuple, List, Any

class HuffmanCoder:
    """
    Optimal prefix-code generation and canonical Huffman coding.
    """
    class Node:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None
        def __lt__(self, other):
            return self.freq < other.freq

    @staticmethod
    def build_codes(text: str) -> Tuple[Dict[str, str], str]:
        if not text:
            return {}, ""
        freqs = Counter(text)
        if len(freqs) == 1:
            char = text[0]
            return {char: "0"}, "0" * len(text)

        heap = [HuffmanCoder.Node(c, f) for c, f in freqs.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)
            merged = HuffmanCoder.Node(None, n1.freq + n2.freq)
            merged.left = n1
            merged.right = n2
            heapq.heappush(heap, merged)

        root = heap[0]
        codes = {}

        def traverse(node, prefix):
            if node.char is not None:
                codes[node.char] = prefix
                return
            traverse(node.left, prefix + "0")
            traverse(node.right, prefix + "1")

        traverse(root, "")
        encoded = "".join(codes[c] for c in text)
        return codes, encoded

    @staticmethod
    def decode(encoded_bits: str, codes: Dict[str, str]) -> str:
        rev_codes = {v: k for k, v in codes.items()}
        curr = ""
        decoded = []
        for bit in encoded_bits:
            curr += bit
            if curr in rev_codes:
                decoded.append(rev_codes[curr])
                curr = ""
        return "".join(decoded)
