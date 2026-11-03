---
tag: 528CPGFWF3
kind: definition
name: Perfect code
msc: [94B25, 94B65]
defines: 94K1WWWGF6
uses: [TAE6K8NQ46, EP5HNGSXFA, 6E7ZZ4DYX3, M2X88AXM17, RZEGDKR7C7]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_bound
---

## Definition

Let $A$ be a finite alphabet with at least two symbols, and let $C \subseteq A^n$ be an [[error-correcting code|TAE6K8NQ46]] of length $n$.
The code $C$ is *perfect* if there is an integer $t \ge 0$ with the following property.
Every word $y \in A^n$ is at [[Hamming distance|EP5HNGSXFA]] at most $t$ from exactly one codeword.

## Remarks

Equivalently, the balls of radius $t$ around the codewords form a partition of the [[Hamming space|6E7ZZ4DYX3]] $A^n$.
If $C$ has at least two codewords, then its [[minimum distance|M2X88AXM17]] is $d = 2t + 1$, and $C$ meets the [[Hamming bound|RZEGDKR7C7]] with equality.
Example: the binary code $\set{000, 111}$ is perfect with $t = 1$.
The words with at most one $1$ are within distance $1$ of $000$ only, and the others are within distance $1$ of $111$ only.
Non-example: the even-weight code $\set{000, 011, 101, 110}$ is not perfect.
With $t = 0$ the word $100$ is near no codeword, and with $t \ge 1$ the word $100$ is at distance $1$ from the three codewords $000$, $110$, $101$.
A code with one codeword, the whole space $A^n$ with $t = 0$, and the binary repetition codes of odd length are called trivial perfect codes.
