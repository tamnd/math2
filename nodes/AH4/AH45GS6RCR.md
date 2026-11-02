---
tag: AH45GS6RCR
kind: concept
name: Separable Banach space
msc: [46B99, 54D65]
specializes: [06GZ956657, 0Z2P41SVDP]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_space
---

## Summary

A separable Banach space is a [[Banach space|06GZ956657]] that has a countable dense subset.
Most spaces met in analysis are of this kind, for example $\ell^p$ and $L^p[0, 1]$ for $1 \le p < \infty$, $c_0$ and $C[0, 1]$.
Separability allows arguments by sequences and diagonal extraction.
For instance, the closed unit ball of the dual of a separable Banach space is metrizable in the weak* topology.
The [[Banach–Mazur theorem|QC5MB5WM8F]] says that every separable Banach space is isometric to a closed subspace of $C[0, 1]$.

## Explanations

### L1 human

A space is separable if a countable list of its points comes as close as you like to every point.
The rationals play this role in the real line.
In the space $C[0, 1]$ of continuous functions with the sup norm, the polynomials with rational coefficients form such a list.
The space $\ell^\infty$ of bounded sequences is too big: it has uncountably many points at distance $1$ from each other.
