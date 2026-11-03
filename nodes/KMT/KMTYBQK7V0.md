---
tag: KMTYBQK7V0
kind: statement
role: theorem
name: Plotkin bound
msc: [94B65]
uses: [TAE6K8NQ46, EP5HNGSXFA, M2X88AXM17]
about: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Plotkin_bound
same_as:
  wikidata: Q1476195
  wikipedia: Plotkin bound
---

## Statement

Let $A$ be an alphabet with $q \ge 2$ symbols, and let $\theta = 1 - 1/q$.
Let $C \subseteq A^n$ be a [[code|TAE6K8NQ46]] of length $n$ with $M$ codewords and [[minimum distance|M2X88AXM17]] $d$.
If $d > \theta n$, then
$$M \le \frac{d}{d - \theta n}.$$

## Remarks

The proof counts the sum $S$ of the [[Hamming distances|EP5HNGSXFA]] $d(x, y)$ over all ordered pairs of distinct codewords in two ways.
Each of the $M(M - 1)$ pairs contributes at least $d$, so $S \ge M(M - 1)d$.
In one coordinate, if $m_a$ codewords have the symbol $a$, the pairs that differ there number $M^2 - \sum_a m_a^2 \le M^2 - M^2/q = \theta M^2$, by the Cauchy–Schwarz inequality.
So $M(M - 1)d \le \theta n M^2$, which rearranges to $M(d - \theta n) \le d$.
Example: the binary simplex code $[2^k - 1, k, 2^{k-1}]$ has $\theta n = 2^{k-1} - 1/2$, and the bound gives $M \le 2^{k-1}/(1/2) = 2^k$, which is its exact size.
For binary codes with $d$ even and $2d > n$, a sharper form is $M \le 2 \floor{d/(2d - n)}$.
In asymptotic form, codes with relative distance $\delta \le \theta$ have rate at most about $1 - \delta/\theta$, and codes with $\delta > \theta$ have rate tending to $0$.

## Explanations

### L1 human

If all codewords must be very far apart, more than a fraction $\theta$ of the length, then only a few codewords fit.
The reason is that the average distance between random words is about $\theta n$, so there is no room for many words that all beat the average.
The Plotkin bound turns this into an exact count.

### L2 human

The Plotkin bound is the strongest classical bound for codes of large relative distance, where the Hamming bound is weak.
Hadamard matrices give codes that meet it, and Levenshtein showed that, if suitable Hadamard matrices exist, the binary form is tight.
For relative distance below $\theta$ it is combined with shortening of codes to give the asymptotic rate bound $1 - \delta/\theta$.
