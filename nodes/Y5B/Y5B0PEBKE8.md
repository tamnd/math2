---
tag: Y5B0PEBKE8
kind: concept
name: Galerkin method
msc: [65N30, 35A15]
sources:
  - url: https://en.wikipedia.org/wiki/Galerkin_method
same_as:
  wikidata: Q1491980
  wikipedia: Galerkin method
---

## Summary

The Galerkin method approximates the solution of a problem in weak form, $B(u, v) = f(v)$ for all $v$ in a [[Hilbert space|HM2HHE3J51]].
It solves the same problem on a finite-dimensional subspace.
This turns a partial differential equation into a finite system of linear equations.
For a bounded and [[coercive|86KRHS6X22]] form, the [[Lax–Milgram theorem|85KK79FCN5]] gives existence and uniqueness of the approximation.
Its error is within a fixed factor of the best possible approximation from the subspace.
The finite element method and spectral methods are Galerkin methods, and Galerkin approximations are also used to prove existence of [[weak solutions|SJZX81A783]].

## Explanations

### L1 human

The true solution lives in an infinite-dimensional space of functions.
The Galerkin method picks a few simple functions, such as polynomials or piecewise linear "hat" functions, and looks for the best combination of them.
"Best" means that the equation holds when tested against each of the chosen functions.
This gives as many equations as unknown coefficients, which a computer can solve.
