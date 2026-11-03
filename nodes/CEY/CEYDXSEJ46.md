---
tag: CEYDXSEJ46
kind: definition
name: Maximum likelihood decoding
msc: [94B35, 94A40]
defines: N5Y47ESTAJ
uses: [TAE6K8NQ46, 0990W5PN13, W773330RK7, EP5HNGSXFA]
sources:
  - url: https://en.wikipedia.org/wiki/Decoding_methods
---

## Definition

Let $A$ be a finite alphabet, and let $C \subseteq A^n$ be an [[error-correcting code|TAE6K8NQ46]] of length $n$.
Let a channel be given by the [[conditional probabilities|0990W5PN13]] $P(y \mid c)$ that the word $y \in A^n$ is received when the codeword $c \in C$ is sent.
A *maximum likelihood decoder* is a map $D \colon A^n \to C$ such that, for each $y \in A^n$,
$$P(y \mid D(y)) = \max_{c \in C} P(y \mid c).$$
When several codewords reach the maximum, the decoder picks one of them.

## Remarks

On the [[binary symmetric channel|W773330RK7]] with crossover probability $p$, a codeword $c$ at [[Hamming distance|EP5HNGSXFA]] $d$ from $y$ gives $P(y \mid c) = p^d (1 - p)^{n - d}$.
If $0 < p < 1/2$, this decreases as $d$ grows, so maximum likelihood decoding is the same as decoding to a nearest codeword.
Example: for $C = \set{000, 111}$ and $y = 010$, $P(y \mid 000) = p(1 - p)^2$ and $P(y \mid 111) = p^2(1 - p)$; for $p < 1/2$ the first is larger, so $D(010) = 000$.
Non-example: if $p > 1/2$, the nearest codeword decoder still returns $000$, but it is not maximum likelihood, since then $P(y \mid 111) > P(y \mid 000)$.
If the codewords are not equally likely, the decoder that minimizes the error probability is maximum a posteriori decoding, which maximizes $P(c \mid y)$ instead.
