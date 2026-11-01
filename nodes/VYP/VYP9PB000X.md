---
tag: VYP9PB000X
kind: concept
name: Macdonald polynomial
msc: ["05E05", 33D52]
specializes: [PAJEHWXW6M]
sources:
  - url: https://en.wikipedia.org/wiki/Macdonald_polynomials
same_as:
  wikidata: Q17098676
  wikipedia: Macdonald polynomials
---

## Summary

Macdonald polynomials $P_\lambda(x; q, t)$ are [[symmetric functions|PAJEHWXW6M]] with coefficients in the field $\Q(q, t)$ of rational functions in two parameters, indexed by [[partitions|0JV30XN73Z]].
They are characterized by a triangularity condition and orthogonality for a two-parameter inner product.
Special values and limits of $q$ and $t$ give the [[Schur polynomials|43VFMJCDYJ]], the Hall–Littlewood polynomials and the Jack polynomials.
Macdonald introduced them in the 1980s, and they connect combinatorics with representation theory and special functions.

## Explanations

### L1 human

Many classical families of symmetric polynomials are special cases of one family with two extra parameters $q$ and $t$.
Setting $q = t$ gives back the Schur polynomials, and setting $q = 0$ gives the Hall–Littlewood polynomials.
For example, for the partition $(2)$ the Macdonald polynomial is $m_{(2)} + \frac{(1+q)(1-t)}{1-qt} m_{(1,1)}$, where $m_{(2)} = \sum_i x_i^2$ and $m_{(1,1)} = \sum_{i<j} x_i x_j$.
At $q = t$ the fraction equals $1$, and the result is the Schur polynomial $s_{(2)}$.
