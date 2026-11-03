---
tag: N5Y47ESTAJ
kind: concept
name: Maximum likelihood decoding
msc: [94B35, 94A40]
sources:
  - url: https://en.wikipedia.org/wiki/Decoding_methods
---

## Summary

Maximum likelihood decoding maps a received word to a codeword that makes this received word most probable.
It depends on the code and on the model of the noisy channel.
When all codewords are sent with the same probability, it minimizes the probability of a decoding error.
On the [[binary symmetric channel|W773330RK7]] with error probability below $1/2$ it is the same as decoding to the nearest codeword in [[Hamming distance|EP5HNGSXFA]].

## Explanations

### L1 human

The receiver sees a damaged word and asks: which codeword, if it had been sent, would most likely produce what I see?
That codeword is the guess.
If each bit flips with a small probability, fewer flips are more likely than more flips, so the best guess is the closest codeword.
For example, with the code $\set{000, 111}$ the received word $010$ is decoded as $000$, since one flip is more likely than two.
