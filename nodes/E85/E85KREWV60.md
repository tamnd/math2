---
tag: E85KREWV60
kind: concept
name: Linear code
msc: [94B05]
specializes: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_code
same_as:
  wikidata: Q1752667
  wikipedia: Linear code
---

## Summary

A linear code is an [[error-correcting code|TAE6K8NQ46]] whose codewords form a [[linear subspace|00YC1D652K]] of $\F_q^n$.
Here $\F_q$ is a [[finite field|0ZXZ82FTX2]], and $\F_q^n$ is the space of words of length $n$ over it.
Its parameters are written $[n, k, d]$: the length $n$, the [[dimension|03GSZ8RTZJ]] $k$ and the [[minimum distance|M2X88AXM17]] $d$.
Linearity makes codes easy to describe, by a [[generator matrix|8TXKFC5PRD]] or a [[parity-check matrix|Y4JB44WWFG]], and easy to decode, by [[syndrome decoding|ZH3QHHP8H7]].
Most codes used in practice, such as Hamming, Reed–Solomon and BCH codes, are linear.

## Explanations

### L1 human

Think of codewords as strings of bits in which the sum of two codewords, taken bit by bit modulo $2$, is again a codeword.
Then the whole code is fixed by a few basic codewords, and every other codeword is a sum of some of them.
For example, the strings $000$, $011$, $101$, $110$ form a linear code: adding any two of them gives one of the four.
A code with $2^k$ codewords needs only $k$ basic codewords to be stored, instead of the full list.
