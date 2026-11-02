---
tag: 1XZJCGJ8B5
kind: definition
name: O-minimal theory
msc: [03C64]
defines: DTWHAW1N0V
uses: [983GZBQYT4, 0FRXBVVR03, 0Q1D85B8G6, CY1TXHF6KQ, 92SWXST1ZM]
sources:
  - url: https://en.wikipedia.org/wiki/O-minimal_theory
---

## Definition

Let $L$ be a first-order language that contains a binary relation symbol $<$.
Let $M$ be an $L$-[[structure|983GZBQYT4]] in which $<$ is interpreted as a [[total order|0FRXBVVR03]].
The structure $M$ is *o-minimal* if every subset of $M$ [[definable|CY1TXHF6KQ]] with parameters is a finite union of points and open [[intervals|0Q1D85B8G6]].
Here the endpoints of an interval $(a, b)$ lie in $M \cup \set{-\infty, +\infty}$.
An $L$-[[theory|92SWXST1ZM]] $T$ is *o-minimal* if every model of $T$ is o-minimal.

## Remarks

Example: the ordered field $(\R, +, \cdot, <, 0, 1)$ is o-minimal.
By the Tarski–Seidenberg theorem it has quantifier elimination, so a definable subset of $\R$ is a Boolean combination of sets $\set{x : p(x) > 0}$ and $\set{x : p(x) = 0}$ with $p$ a polynomial with real coefficients.
Each such set is a finite union of points and open intervals, because a nonzero polynomial has finitely many roots.

Non-example: the structure $(\Z, <, +)$ is not o-minimal.
The formula $\exists y \, (x = y + y)$ defines the set of even integers, which is not a finite union of points and intervals.

By a theorem of Knight, Pillay and Steinhorn, if a structure $M$ is o-minimal then its complete theory is o-minimal.
Dense linear orders without endpoints and real closed fields give o-minimal theories.
