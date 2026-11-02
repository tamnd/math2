---
tag: VJVDDR8BCE
kind: concept
name: Köthe–Toeplitz dual
msc: [46A45]
sources:
  - url: https://en.wikipedia.org/wiki/Beta-dual_space
---

## Summary

The Köthe–Toeplitz duals of a [[sequence space|XYTN19EPF2]] $X$ are the sequence spaces of multipliers $a$ for which $\sum a_n x_n$ behaves well for every $x$ in $X$.
The $\alpha$-dual asks for absolute convergence of $\sum a_n x_n$, and the $\beta$-dual asks for convergence.
They play the role of a dual space that is again a space of sequences, without any topology.
For example, the $\beta$-dual of $\ell^1$ is $\ell^\infty$, which matches the dual space of $\ell^1$ in functional analysis.

## Explanations

### L1 human

Given a family of sequences $X$, ask which sequences $a$ can be multiplied term by term with every $x$ in $X$ so that the series $\sum a_n x_n$ still converges.
These $a$ form a new space of sequences, the dual of $X$.
If $X$ consists of the sequences with $\sum \abs{x_n} < \infty$, then any bounded $a$ works, and no unbounded $a$ does.
The bigger $X$ is, the smaller its dual.
