---
tag: G1ZAWMBNE1
kind: statement
role: theorem
name: Kraft–McMillan inequality
msc: [94A45, 94A29, 68P30]
sources:
  - url: https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan_inequality
same_as:
  wikidata: Q371685
  wikipedia: Kraft–McMillan inequality
---

## Statement

Let $D \ge 2$ be an integer, let $\Sigma$ be an alphabet with $D$ symbols, and let $\ell_1, \dots, \ell_n$ be positive integers.

1. If there is a uniquely decodable code over $\Sigma$ with $n$ codewords of lengths $\ell_1, \dots, \ell_n$, then $\sum_{i=1}^{n} D^{-\ell_i} \le 1$.
2. If $\sum_{i=1}^{n} D^{-\ell_i} \le 1$, then there is a prefix code over $\Sigma$ with $n$ codewords of lengths $\ell_1, \dots, \ell_n$.

## Remarks

Part 1 is due to McMillan and part 2 to Kraft.
Since every prefix code is uniquely decodable, the inequality, the existence of a prefix code and the existence of a uniquely decodable code with the given lengths are all equivalent.

For part 2, sort the lengths so that $\ell_1 \le \dots \le \ell_n$ and pick codewords one by one as leaves of the complete $D$-ary tree.
The inequality guarantees that a free node of depth $\ell_i$ remains at each step.
For part 1, let $S = \sum_i D^{-\ell_i}$ and $\ell = \max_i \ell_i$.
Expanding $S^k$ groups the terms by the total length $m$ of $k$ codewords, and unique decodability allows at most $D^m$ such sequences for each $m$.
So $S^k \le k \ell$ for every $k$, which forces $S \le 1$.

Example: the binary variable-length code $\set{0, 10, 110, 111}$ is a prefix code, and $2^{-1} + 2^{-2} + 2^{-3} + 2^{-3} = 1$.
Without unique decodability part 1 fails: the code $\set{0, 1, 01}$ has $2^{-1} + 2^{-1} + 2^{-2} = 5/4 > 1$, and the string $01$ can be read as one codeword or as two.

## Explanations

### L1 human

Short codewords are precious: with two symbols there are only two codewords of length $1$, four of length $2$, and so on.
The inequality is a budget: a codeword of length $\ell$ costs $D^{-\ell}$, and the total cost cannot exceed $1$.
Any list of lengths within the budget can be realized by a code in which no codeword begins another one.
Even if one only asks that messages can be decoded unambiguously, one cannot do better.

### L2 human

The inequality turns questions about codes into questions about numbers.
For example, the minimum expected length of a uniquely decodable code is found by minimizing $\sum_i p_i \ell_i$ subject to $\sum_i D^{-\ell_i} \le 1$.
This leads to the lower bound by the entropy in Shannon's source coding theorem.
Part 1 also shows that nothing is lost by restricting to prefix codes, which can be decoded symbol by symbol.
