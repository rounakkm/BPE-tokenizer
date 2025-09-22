from typing import List, Dict, Tuple
from collections import Counter

def most_freq(vocab: Dict[Tuple[int, int], int]) -> Tuple[int, int]:
    """Find the most frequent token pair"""
    if not vocab:
        return (0, 0)
    return max(vocab.items(), key=lambda x: x[1])[0]


def merge_tokens(tokens: List[int], most_freq_pair: Tuple[int, int], new_token: int) -> List[int]:
    """Replace most frequent pair with a new token"""
    new_tokens = []
    i = 0
    while i < len(tokens):
        if (
            i < len(tokens) - 1
            and tokens[i] == most_freq_pair[0]
            and tokens[i + 1] == most_freq_pair[1]
        ):
            new_tokens.append(new_token)
            i += 2
        else:
            new_tokens.append(tokens[i])
            i += 1
    return new_tokens


def tokenize(tokens: List[int], vocab: Dict[Tuple[int, int], int], merge_count: int):
    """Performs BPE tokenization"""
    new_pairs_count = 1
    freq_map = pair_gen(tokens)

    while new_pairs_count < merge_count:
        most_pair = most_freq(freq_map)

        if freq_map.get(most_pair, 1) == 1:
            print("\nStopping as max freq is 1")
            break

        new_token = 255 + new_pairs_count
        new_pairs_count += 1
        vocab[most_pair] = new_token
        print(f"\nSelected Pair: {most_pair} -> {new_token}")

        tokens = merge_tokens(tokens, most_pair, new_token)
        freq_map = pair_gen(tokens)

    print("Completed")
    return tokens, vocab


def detokenize(tokens: List[int], lookup_table: Dict[int, Tuple[int, int]]) -> str:
    """Reconstruct"""
    found_merged = True

    while found_merged:
        found_merged = False
        unmerged_tokens = []

        for t in tokens:
            if t > 255 and t in lookup_table:
                found_merged = True
                left, right = lookup_table[t]
                unmerged_tokens.extend([left, right])
            else:
                unmerged_tokens.append(t)

        tokens = unmerged_tokens

    return "".join(chr(tok) for tok in tokens)
