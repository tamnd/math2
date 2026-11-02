---
tag: HTMCEARGDD
kind: concept
name: Singular integral operator
msc: [42B20, 47G10]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral
same_as:
  wikidata: Q888122
  wikipedia: Singular integral
---

## Summary

A singular integral operator is an integral operator $Tf(x) = \int K(x, y)f(y) \, dy$ whose kernel has a non-integrable singularity on the diagonal $x = y$, of size $\abs{x - y}^{-n}$ in $\R^n$.
The integral exists only as a principal value, thanks to cancellation in the kernel.
The Hilbert transform and the Riesz transforms are the basic examples.
Calderón–Zygmund theory shows that such operators are bounded on $L^p$ for $1 < p < \infty$, which is central in harmonic analysis and elliptic PDE.

## Explanations

### L1 human

Many natural operators, such as the map from the Laplacian of a function to its second derivatives, are given by integrals against kernels that blow up like $1/\abs{x}^n$.
Such an integral diverges if taken with absolute values, so it is not an ordinary integral.
It still makes sense because the kernel takes positive and negative values in balanced amounts near the singularity.
For example, the Hilbert transform on the line integrates $f(y)$ against $1/(\pi(x - y))$, which is positive on one side of $x$ and negative on the other.
