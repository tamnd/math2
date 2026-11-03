---
tag: NNJRQ7TG8R
kind: definition
name: Syndrome decoding
msc: [94B35, 94B05]
defines: ZH3QHHP8H7
uses: [E85KREWV60, Y4JB44WWFG, 564VVAQTNR, K8ZHAQAK2B, EP5HNGSXFA]
sources:
  - url: https://en.wikipedia.org/wiki/Decoding_methods
---

## Definition

Let $C$ be a [[linear code|E85KREWV60]] of length $n$ and dimension $k < n$ over the finite field $\F_q$, with [[parity-check matrix|Y4JB44WWFG]] $H$.

1. The *syndrome* of a word $y \in \F_q^n$ is $s(y) = Hy^T \in \F_q^{n-k}$.
2. Two words have the same syndrome if and only if they lie in the same [[coset|564VVAQTNR]] $y + C$ of $C$ in $\F_q^n$.
3. For each syndrome $s$, a *coset leader* $e_s$ is a word of least [[Hamming weight|K8ZHAQAK2B]] among the words with syndrome $s$.

*Syndrome decoding* maps a received word $y$ to the codeword $y - e_{s(y)}$.

## Remarks

The output $y - e_{s(y)}$ lies in $C$, since it has syndrome $0$.
It is a codeword at least [[Hamming distance|EP5HNGSXFA]] from $y$: for $c \in C$, the word $y - c$ has syndrome $s(y)$, so its weight is at least that of $e_{s(y)}$.
Example: take the binary code $C = \set{000, 111}$ with
$$H = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}.$$
The coset leaders are $000, 100, 010, 001$, with syndromes $00, 11, 10, 01$.
For $y = 110$ the syndrome is $01$, the leader is $001$, and the decoder returns $110 - 001 = 111$, the nearest codeword.
Non-example: the word $011$ also has syndrome $11$, but it is not a coset leader, since its weight $2$ exceeds the weight $1$ of $100$.
Using it would decode $100$ to $111$ instead of $000$.
