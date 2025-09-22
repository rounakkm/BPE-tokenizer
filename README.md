# Byte Pair Encoding (BPE) Tokenizer – Python

An implementation in **Python** of the Byte Pair Encoding (BPE) algorithm for text tokenization, with **persistent vocabulary storage**.  

---

## Description
This Python project implements **Byte Pair Encoding (BPE)** for tokenizing text.  
It can handle large corpora efficiently and supports:  
- Training a tokenizer on a text corpus  
- Encoding new text using the trained vocabulary  
- Decoding tokens back into readable text  
- Saving/loading the vocabulary in JSON format for **persistent use**  

The added **persistent vocabulary** feature allows you to reuse the tokenizer without retraining, making it ideal for experiments or downstream applications.

---

## Contents 
- [How BPE Works](#how-bpe-works)  
- [File Structure](#file-structure)
- [Workflow](#workflow)
- [Training Data](#training-data)    
- [Components](#components)  
- [Bonus Feature](#bonus-feature)
- [Notes](#notes)  

---

## How BPE works
Byte Pair Encoding (BPE) is a **tokenization and compression technique** that merges the most frequent pair of consecutive symbols into a new token.  

**Example:**  

Input: `mississippi`  

1. Most frequent pair: `"ss"` → New token `A`  
   - Data: `miAissippi`  
   - Vocabulary: `A = ss`  
2. Most frequent pair: `"ii"` → New token `B`  
   - Data: `mABssippi`  
   - Vocabulary: `B = ii, A = ss`  
3. Most frequent pair: `"pp"` → New token `C`  
   - Data: `mABssICi`  
   - Vocabulary: `C = pp, B = ii, A = ss`  

The process continues until no pair occurs more than once.  

---

## File Structure

```
BPE-tokenizer/
├── src/
│   ├── main.py                # Train, encode, decode workflow script
│   └── tokenizer.py           # BPE implementation and helper functions
├── README.md           
├── alice.txt                  # Sample training corpus
├── output.txt                 
└── vocab.json                 # Persistent BPE vocabulary 
```



---


## Workflow
1. **Training**  
   - Load a text corpus  
   - Convert characters to base tokens  
   - Iteratively merge most frequent pairs to create vocabulary  
   - Save vocabulary (`vocab.json`) for future use  

2. **Encoding**  
   - Load saved vocabulary  
   - Convert new text to tokens  
   - Apply merge rules until no further merges are possible  

3. **Decoding**  
   - Use the reverse lookup of the vocabulary  
   - Expand merged tokens back to original character sequences  

---

## Training Data
The sample file `alice.txt` is used as a corpus. It is a plain text version of *Alice’s Adventures in Wonderland*. You can replace it with any text corpus to train a custom tokenizer.

---



## Components
**tokenizer.py**
- `tokenize(tokens, vocab, merge_count)` – Train BPE on a token sequence  
- `detokenize(tokens, lookup_table)` – Decode token sequence to text  
- `pair_gen(tokens)` – Generate frequency map of adjacent token pairs  
- `most_freq(freq_map)` – Find the most frequent pair  
- `merge_tokens(tokens, pair, new_token)` – Merge a token pair into a single token  

**main.py**
- Loads corpus (`alice.txt`)  
- Trains tokenizer with a configurable merge count  
- Saves vocabulary in `vocab.json`  
- Encodes and decodes example strings  
- Prints output and saves logs to `output.txt`
  
---

## Bonus Feature

**Persistent** Vocabulary Storage:

- Saves the learned BPE vocabulary in `.json` format

- Enables reuse without retraining

- Supports **reproducibility and experimentation** with large corpora

---


## Notes

- Supports Unicode characters and special symbols

- Merge count is **configurable** (merge_count in `main.py`)

- Output logs include:

   - `Learned vocabulary`

   - `Tokenized text`

   - `Detokenized text`
