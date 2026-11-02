---
tag: 5F76XA1ABC
kind: statement
role: theorem
name: Brent's method
msc: [65H05]
uses: [00KAFBR32E, 7VMYC7MB3Q, 9ZC177PVPC, NW1XQ95R5P]
about: [TR4CNS5PMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Brent%27s_method
same_as:
  wikidata: Q905988
  wikipedia: Brent's method
---

## Statement

Let $f \colon [a, b] \to \R$ be continuous with $f(a) f(b) < 0$, and let $\varepsilon > 0$ be a tolerance.
*Brent's method* keeps at each step a bracket, an interval whose endpoints have values of opposite signs.
At each step it proposes a new point by [[inverse quadratic interpolation|NW1XQ95R5P]] or by the [[secant method|9ZC177PVPC]].
It falls back to a [[bisection|7VMYC7MB3Q]] step when the proposed point fails tests on its position or on the decrease of the bracket.
Then:

1. Every bracket contains a zero of $f$.
2. The method stops after finitely many evaluations of $f$ with a bracket of length at most $\varepsilon$, up to the rounding allowance in its tests.
3. If bisection needs $N$ steps to reach the tolerance, Brent's method needs at most about $N^2$ evaluations of $f$.

## Remarks

Claim 1 follows from the [[intermediate value theorem|00KAFBR32E]], since the method only keeps brackets with a sign change.
Claims 2 and 3 come from the safeguards: the tests force a bisection step whenever the interpolation steps have not shrunk the bracket enough over the last few steps.
The bound in claim 3 is a worst case.
For a smooth function with a simple zero, the method ends up taking interpolation steps only, and then it converges superlinearly.
So it combines the reliability of bisection with the speed of the interpolation methods.
It refines an earlier method of Dekker, which could take a very large number of tiny steps.
It is the standard root finder for one equation in many numerical libraries, for example as `fzero` in MATLAB.

## Explanations

### L1 human

Bisection is slow but cannot fail; interpolation is fast but can go wrong.
Brent's method tries a fast interpolation step first and checks that it behaves.
If it does not, the method takes a safe bisection step instead, so the root stays trapped in a shrinking interval.

### L2 human

The main design point is the bracket: the method never gives up the sign change, so convergence is guaranteed for every continuous $f$.
For well-behaved $f$ the interpolation steps dominate and the speed is close to that of inverse quadratic interpolation.
To use it, one needs a starting interval where $f$ changes sign.
