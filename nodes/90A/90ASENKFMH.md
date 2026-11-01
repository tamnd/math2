---
tag: 90ASENKFMH
kind: definition
name: Fractional ideal
msc: [13A15, 11R04]
defines: YB4JTB4WJN
uses: [0QVD7WBFGN, 0F2PTGX1A2, 0NZ8JA25WK, 096Z9MP2ME, 05WDSN597C]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_ideal
---

## Definition

Let $R$ be an [[integral domain|0QVD7WBFGN]] and $K$ its [[field of fractions|0F2PTGX1A2]].
A *fractional ideal* of $R$ is a subset $I \subseteq K$ such that:

1. $I$ is an $R$-[[submodule|05WDSN597C]] of $K$;
2. $I \ne \set{0}$;
3. there is a nonzero $r \in R$ with $rI \subseteq R$.

The product of fractional ideals $I$ and $J$ is the set $IJ$ of finite sums $\sum x_k y_k$ with $x_k \in I$ and $y_k \in J$.
A fractional ideal $I$ is *invertible* if $IJ = R$ for some fractional ideal $J$.

## Remarks

Example: $I = \tfrac12 \Z \subseteq \Q$ for $R = \Z$; it is a nonzero $\Z$-submodule, and $2I = \Z \subseteq \Z$, so it is a fractional ideal, with inverse $2\Z$.
Non-example: $\Z[\tfrac12] = \set{a/2^k : a \in \Z, k \ge 0}$ is a nonzero $\Z$-submodule of $\Q$, but it fails clause 3: for any nonzero integer $r$, choose $k$ with $2^k > \abs{r}$; then $r/2^k \in r\Z[\tfrac12]$ is not an integer.
Every nonzero [[ideal|096Z9MP2ME]] of $R$ is a fractional ideal, with $r = 1$; these are the integral ideals.
For $x \in K^{\times}$, the set $xR$ is a principal fractional ideal, with inverse $x^{-1}R$.
When $R$ is Noetherian, clause 3 is equivalent to $I$ being a finitely generated $R$-module.
Some authors, and Mathlib, also count $\set{0}$ as a fractional ideal.
