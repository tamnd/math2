---
tag: ZH3QHHP8H7
kind: concept
name: Syndrome decoding
msc: [94B35, 94B05]
sources:
  - url: https://en.wikipedia.org/wiki/Decoding_methods
---

## Summary

Syndrome decoding is a method to decode a [[linear code|E85KREWV60]] with a table indexed by syndromes.
The syndrome of a received word $y$ is $Hy^T$, where $H$ is a [[parity-check matrix|Y4JB44WWFG]].
It depends only on the error pattern, not on the codeword that was sent.
For each syndrome the table stores an error pattern of least weight with that syndrome, and the decoder subtracts it from $y$.
This gives a nearest codeword, and for an $[n, k]$ code over $\F_q$ the table has only $q^{n-k}$ entries instead of $q^n$.

## Explanations

### L1 human

When a codeword $c$ is sent and an error $e$ is added, the receiver sees $y = c + e$.
Applying the parity checks kills the codeword and leaves a fingerprint of the error alone.
So the receiver looks up the fingerprint in a table and reads off the most likely error.
For the binary code $\set{000, 111}$, each single-bit error has its own fingerprint, so any single error is found and undone.
