---
tag: 1NYCGYDNTX
kind: statement
role: theorem
name: Gilbert–Varshamov bound
msc: [94B65]
uses: [TAE6K8NQ46, EP5HNGSXFA, M2X88AXM17, 6E7ZZ4DYX3, 0GBZM0MT0F, E85KREWV60, 95CYGNRQQ6]
about: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Gilbert%E2%80%93Varshamov_bound
same_as:
  wikidata: Q2454864
  wikipedia: Gilbert–Varshamov bound
---

## Statement

Let $A$ be an alphabet with $q \ge 2$ symbols, and let $n$ and $d$ be integers with $1 \le d \le n$.
Then there is a [[code|TAE6K8NQ46]] $C \subseteq A^n$ with [[minimum distance|M2X88AXM17]] at least $d$ and
$$\abs{C} \ge \frac{q^n}{\sum_{i=0}^{d-1} \binom{n}{i} (q - 1)^i}.$$

## Remarks

Take a code with minimum distance at least $d$ that cannot be enlarged without lowering the distance, for example by adding words greedily.
Then every word of $A^n$ is at [[Hamming distance|EP5HNGSXFA]] at most $d - 1$ from some codeword, or it could be added.
So the balls of radius $d - 1$ around the codewords cover the [[Hamming space|6E7ZZ4DYX3]] $A^n$, and $\abs{C}$ times the volume of one ball is at least $q^n$.
There is a version for [[linear codes|E85KREWV60]]: if $q$ is a prime power and $\sum_{i=0}^{d-2} \binom{n-1}{i}(q-1)^i < q^{n-k}$, then there is a linear $[n, k]$ code over $\F_q$ with minimum distance at least $d$.
There is also an asymptotic form; let $H_q$ be the [[q-ary entropy function|95CYGNRQQ6]] and let $0 \le \delta < 1 - 1/q$ and $\varepsilon > 0$.
Then for all large $n$ there are codes of relative distance at least $\delta$ and rate at least $1 - H_q(\delta) - \varepsilon$.
Example: for $q = 2$, $n = 7$, $d = 3$ the bound gives $\abs{C} \ge 128/29$, so a binary code with at least $5$ codewords exists; the Hamming code has $16$.

## Explanations

### L1 human

The Gilbert–Varshamov bound says that good codes exist.
If one picks codewords one at a time, each new codeword far from the previous ones, one can go on for a long time before the space is full.
The count of how long gives a lower bound on the best possible code size.

### L2 human

It is the main lower bound on $A_q(n, d)$, the largest size of a $q$-ary code of length $n$ and distance $d$.
It complements the upper bounds of Hamming, Plotkin and Elias–Bassalygo.
A random linear code meets it with high probability, but no explicit family of binary codes is known to meet it asymptotically.
For $q \ge 49$ a square, algebraic geometry codes beat it, by the Tsfasman–Vlăduț–Zink bound.
