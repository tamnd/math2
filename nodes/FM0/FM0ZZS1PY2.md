---
tag: FM0ZZS1PY2
kind: concept
name: Multiple gamma function
msc: ["33B15", "11M35"]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple_gamma_function
same_as:
  wikidata: Q6934934
  wikipedia: Multiple gamma function
---

## Summary

The multiple gamma functions $\Gamma_N(w \mid a_1, \ldots, a_N)$ of E. W. Barnes generalise the [[gamma function|0H5SYBSED9]] to $N$ periods.
They are built from the Barnes zeta function $\sum (w + n_1 a_1 + \cdots + n_N a_N)^{-s}$ by zeta regularisation, as the gamma function is built from the [[Hurwitz zeta function|G4SW7HJG88]].
Shifting $w$ by a period $a_j$ divides $\Gamma_N$ by a multiple gamma function of order $N - 1$.
The [[Barnes G-function|7E2JJWFF00]] is essentially the case $N = 2$ with $a_1 = a_2 = 1$.

## Explanations

### L1 human

The factorial $n!$ multiplies the numbers $1, \ldots, n$, which lie on a line with step $1$.
One can try to multiply all numbers $w + n_1 a_1 + n_2 a_2$ of a lattice in a quadrant, or in a higher-dimensional corner.
This infinite product diverges, but a standard regularisation trick gives it a finite meaning.
The result is the multiple gamma function.
For one period equal to $1$ it gives back $\Gamma(w)$, up to the constant factor $1/\sqrt{2\pi}$.
