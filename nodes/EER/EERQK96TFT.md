---
tag: EERQK96TFT
kind: concept
name: Lyndon basis
msc: [17B01, 68R15]
specializes: [R1VQ49E4JA]
sources:
  - url: https://en.wikipedia.org/wiki/Lyndon_word
---

## Summary

The Lyndon basis is a basis of a [[free Lie algebra|NNAXK7BM3H]] indexed by Lyndon words.
A Lyndon word is a word that is strictly smaller, in lexicographic order, than each of its proper suffixes.
Each Lyndon word gets a bracketing from its standard factorization, and these brackets form a basis.
It is a [[Hall basis|R1VQ49E4JA]].
It explains why the number of Lyndon words of length $n$ equals the dimension of the degree $n$ part of the free Lie algebra.

## Explanations

### L1 human

Order the letters, say $a < b$, and compare words as in a dictionary.
A word is a Lyndon word when it comes strictly before every one of its tails; for example $aab$ comes before $ab$ and $b$.
The word $aba$ is not a Lyndon word, because its tail $a$ comes first.
Each Lyndon word splits in a canonical way into two shorter Lyndon words, and this split tells how to place brackets.
For example $aab$ becomes $[a, [a, b]]$ and $abb$ becomes $[[a, b], b]$.
