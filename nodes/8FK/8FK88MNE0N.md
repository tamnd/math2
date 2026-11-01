---
tag: 8FK88MNE0N
kind: concept
name: WZ theory
msc: [05A19, 33F10]
sources:
  - url: https://en.wikipedia.org/wiki/Wilf%E2%80%93Zeilberger_pair
---

## Summary

WZ theory, named after Herbert Wilf and Doron Zeilberger, is a method to prove identities of the form $\sum_k F(n, k) = 1$ by computer, see the [[definition|4HP429BZQ5]].
The proof consists of one rational function, the WZ certificate.
The certificate turns $F$ into a Wilf–Zeilberger pair, whose defining equation can be checked by algebra alone.
It applies to sums of hypergeometric terms, such as most identities for [[binomial coefficients|0GBZM0MT0F]], and it relates to Zeilberger's algorithm and Gosper's algorithm.

## Explanations

### L1 human

Many identities for sums of binomial coefficients have tricky proofs by hand.
WZ theory replaces the trick by a mechanical certificate.
A computer finds a rational function, and anyone can check by simple algebra that it satisfies one equation.
That equation forces the sum to be the same for all $n$, so it is enough to check the case $n = 0$.
