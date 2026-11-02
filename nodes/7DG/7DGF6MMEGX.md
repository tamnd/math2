---
tag: 7DGF6MMEGX
kind: concept
name: Thin set
msc: [31C40, 31B15]
sources:
  - url: https://en.wikipedia.org/wiki/Fine_topology_(potential_theory)
---

## Summary

A set $E \subseteq \R^n$ is thin at a point $x$ if $E$ is very sparse near $x$.
Precisely, some [[superharmonic function|X4V2S56YQQ]] is strictly larger along $E$ near $x$ than at $x$ itself.
Thinness measures how visible a set is to Brownian motion and to harmonic functions near a point.
A boundary point of a domain is irregular for the Dirichlet problem exactly when the complement of the domain is thin there.
[[Wiener's criterion|STMT1K1865]] decides thinness by a series of capacities.

## Explanations

### L1 human

A set can come arbitrarily close to a point and still be almost invisible from it.
Thinness makes this precise with superharmonic functions, which may jump up along a thin set but not along a fat one.
A sequence of points converging to $x$ in space $\R^3$ is thin at $x$, because points have capacity zero.
A solid ball is never thin at a point of its boundary.
In $\R^3$, a sufficiently sharp spike, as in Lebesgue's example, is thin at its tip even though it reaches that point.
