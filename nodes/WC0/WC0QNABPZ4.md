---
tag: WC0QNABPZ4
kind: concept
name: Wilf–Zeilberger pair
msc: [33F10, 05A19, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Wilf%E2%80%93Zeilberger_pair
same_as:
  wikidata: Q3147828
  wikipedia: Wilf–Zeilberger pair
---

## Summary

A Wilf–Zeilberger pair, or WZ pair, is a pair of hypergeometric terms $F(n, k)$ and $G(n, k)$ with $F(n + 1, k) - F(n, k) = G(n, k + 1) - G(n, k)$.
Summing this relation over $k$ makes the right side telescope, which proves that $\sum_k F(n, k)$ does not depend on $n$.
Many binomial and hypergeometric identities can be proved this way, and the pair can be found by computer, for example with [[Gosper's algorithm|NHMJQBS04M]].
The rational function $G/F$ is a short certificate that anyone can check by algebra.

## Explanations

### L1 human

To prove that a sum such as $\sum_k \binom{n}{k}$ equals $2^n$, divide by the right side so that the claim becomes "this sum is always $1$".
It is then enough to show that the sum does not change when $n$ goes to $n + 1$.
A WZ pair shows this by writing each change in a term as a difference of neighbouring terms of a second sequence, so the changes cancel in the sum.
The second sequence is the original one times a rational function, the certificate, and checking the proof reduces to simplifying a fraction.
