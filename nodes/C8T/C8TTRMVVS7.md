---
tag: C8TTRMVVS7
kind: problem
name: Kadison–Singer problem
msc: [46L30, 46L05, 42C15]
uses: [F7MB2WREBJ, HM2HHE3J51]
about: [F7MB2WREBJ]
sources:
  - url: https://en.wikipedia.org/wiki/Kadison%E2%80%93Singer_problem
same_as:
  wikidata: Q25304456
  wikipedia: Kadison–Singer problem
history:
  posed_by: "Richard Kadison and Isadore Singer"
  first_stated: "1959"
---

## Problem

Let $H = \ell^2(\N)$ be the [[Hilbert space|HM2HHE3J51]] of square-summable sequences, and let $B(H)$ be the [[C*-algebra|M2WFY1D3SZ]] of bounded operators on $H$.
Let $D \subseteq B(H)$ be the C\*-subalgebra of diagonal operators with respect to the standard basis, which is isomorphic to $\ell^\infty(\N)$.
A pure [[state|F7MB2WREBJ]] on a C\*-algebra is a state that is not a proper convex combination of two other states.
Does every pure state on $D$ extend to a unique state on $B(H)$?

## Remarks

Every state on $D$ extends to some state on $B(H)$ by the Hahn–Banach theorem, so the question is about uniqueness.
Kadison and Singer posed the question in their 1959 paper "Extensions of pure states".
Over the following decades it was shown to be equivalent to many problems in other fields, among them Anderson's paving conjecture, the Feichtinger conjecture on frames, and Weaver's discrepancy conjecture.
Adam Marcus, Daniel Spielman and Nikhil Srivastava proved Weaver's conjecture, and so solved the problem with a positive answer; their proof was posted in 2013 and published in 2015.
Their method uses interlacing families of polynomials.

## Explanations

### L1 human

In quantum mechanics, a state assigns expected values to observables.
The question asks: if one knows the expected values of all diagonal observables in a very sharp way, does that determine the expected values of all observables?
The answer turned out to be yes.
The solution came from an unexpected direction, through a result about sums of random rank-one matrices and the roots of polynomials.
