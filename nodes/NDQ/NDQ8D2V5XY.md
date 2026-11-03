---
tag: NDQ8D2V5XY
kind: statement
role: theorem
name: Error detection and correction capability
msc: [94B05, 94B25, 94B35]
uses: [EFGYF9P0PN, M2X88AXM17, K5287V64FH, 03HF5PMY5T]
about: [M2X88AXM17]
sources:
  - url: https://en.wikipedia.org/wiki/Error_detection_and_correction
---

## Statement

Let $C \subseteq \Sigma^n$ be a [[block code|EFGYF9P0PN]] with [[minimum distance|M2X88AXM17]] $d$, and let $s, t, e \ge 0$ be integers.
Distances are [[Hamming distances|K5287V64FH]].

1. Detection: $C$ detects every pattern of at most $s$ errors if and only if $d \ge s + 1$. That is, no codeword turns into a different codeword by changing at most $s$ symbols.
2. Correction: the balls of radius $t$ around the codewords are pairwise disjoint if and only if $d \ge 2t + 1$. Then nearest-codeword decoding corrects every pattern of at most $t$ errors.
3. Erasures: if $d \ge e + 1$, each codeword is determined by its symbols outside any $e$ known positions.

## Remarks

Part 1 is the definition of $d$ restated: changing at most $s$ symbols moves a codeword by distance at most $s$.
For part 2, if $y$ is within $t$ of two codewords $c \ne c'$, the [[triangle inequality|03HF5PMY5T]] gives $d(c, c') \le 2t$.
Conversely, if $d(c, c') = \delta \le 2t$, change $c$ in $\min(t, \delta)$ of the positions where it differs from $c'$, towards $c'$; the result is within $t$ of both.
For part 3, two codewords that agree outside $e$ positions are at distance at most $e < d$, so they are equal.

Example: the binary repetition code $\set{00000, 11111}$ has $d = 5$; it detects $4$ errors and corrects $2$, by majority vote.

## Explanations

### L1 human

The farther apart the codewords are, the more errors the code can handle.
A code whose codewords differ in at least $d$ places notices any $d - 1$ errors.
It can repair up to $(d - 1)/2$ errors, rounded down, because the damaged word stays closer to the original than to any other codeword.

### L2 human

This is why the minimum distance is the key parameter of a code, and why bounds such as the Hamming, Singleton and Gilbert–Varshamov bounds are stated in terms of it.
Part 2 is a packing statement: a $t$-error-correcting code is a packing of disjoint Hamming balls of radius $t$, which leads directly to the Hamming bound and to perfect codes.
Detection and correction can be traded: a code with $d \ge t + s + 1$ and $s \ge t$ corrects $t$ errors and at the same time detects $s$ errors.
