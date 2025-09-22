import pickle
from tokenizer import tokenize, detokenize, pair_gen, most_freq, merge_tokens

# File paths
corpus_file = "alice.txt"
output_file = "output.txt"


with open(corpus_file, "r", encoding="utf-8") as f:
    text = f.read()
tokens = [ord(c) for c in text]

# Train tokenizer (set a large merge_count to get many merges)
merge_count = 5000  
tokens, vocab = tokenize(tokens, {}, merge_count=merge_count)

# Created lookup table
lookup_table = {v: k for k, v in vocab.items()}

# Save the vocab and tokens (opt)
with open("vocab.pkl", "wb") as f:
    pickle.dump(vocab, f)
with open("tokens.pkl", "wb") as f:
    pickle.dump(tokens, f)


with open(output_file, "w", encoding="utf-8") as f:
    # Write learnt vocabulary
    f.write("Learnt Vocabulary\n\n")
    for k, v in vocab.items():
        f.write(f"({k[0]}, {k[1]}) -> {v}\n")
    
    # Tokenized text
    f.write("\n\n---------- Tokenized Text ----------\n\n")
    f.write("[")
    f.write(", ".join(str(tok) for tok in tokens))
    f.write("]\n")
    
    # Detokenized text
    f.write("\n\n---------- Detokenized Text ----------\n\n")
    detok_text = detokenize(tokens, lookup_table)
    f.write(detok_text)

def encode_text(text: str, vocab: dict) -> list:
    """Encodes text using a pre-trained BPE vocabulary."""
    tokens = [ord(c) for c in text]
    

    sorted_merges = sorted(vocab.items(), key=lambda item: item[1])
    
   
    for pair, new_token in sorted_merges:
        while pair_gen(tokens).get(pair):
            tokens = merge_tokens(tokens, pair, new_token)
    
    return tokens

example_text = "A wizard is never late, Frodo Baggins. Nor is he early. He arrives precisely when he means to."

# Encode example
encoded_example_tokens = encode_text(example_text, vocab)

# Detokenize example
decoded_example = detokenize(encoded_example_tokens, lookup_table)

print(f"Training, tokenization, and detokenization done! Output saved to {output_file}")
print("\n--- Example Encoding and Decoding ---")
print(f"Original Text: {example_text}")
print(f"Encoded Tokens: {encoded_example_tokens}")
print(f"Decoded Text: {decoded_example}")
