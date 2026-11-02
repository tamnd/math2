---
tag: C1XNMMKZ1J
kind: problem
name: Hilbert's sixteenth problem
msc: [14P25, 34C07]
uses: [EWS4WFTA7W, 0AAQ73WRFB, 08J2M1JYAG]
about: [EWS4WFTA7W, 0AAQ73WRFB]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_sixteenth_problem
same_as:
  wikidata: Q2509489
  wikipedia: Hilbert's sixteenth problem
history:
  posed_by: "David Hilbert"
  first_stated: "1900"
---

## Problem

The problem has two parts.
The real points of a nonsingular real plane curve form finitely many closed curves in the real projective plane.
Those that bound a disc are called ovals.

1. For each $n$, determine the possible relative positions of the ovals of a nonsingular real [[plane algebraic curve|EWS4WFTA7W]] of degree $n$. Ask the same for real algebraic surfaces in space.
2. Consider planar vector fields $\dot{x} = P(x, y)$, $\dot{y} = Q(x, y)$ with $P, Q$ real polynomials of degree at most $n$. For each $n$, bound the number $H(n)$ of their [[limit cycles|0AAQ73WRFB]], and describe their possible positions.

## Remarks

Hilbert included the problem in his list of 1900.
For part 1, Harnack's curve theorem says that a real plane curve of degree $n$ has at most $(n-1)(n-2)/2 + 1$ connected components, and this bound is attained.
Gudkov completed the classification of the arrangements for degree $6$, and the classification is known up to degree $7$ and open beyond.
For part 2, Écalle and Ilyashenko proved independently that each single polynomial vector field has finitely many limit cycles.
Whether $H(n)$ is finite is unknown for every $n \ge 2$, and quadratic vector fields with $4$ limit cycles are known.

## Explanations

### L1 human

A real polynomial curve in the plane can consist of several closed loops, some nested inside others.
The first part asks which nesting patterns can occur for a given degree.
The second part asks how many isolated closed orbits a polynomial system of differential equations in the plane can have.
Both questions are easy to state and remain largely open after more than a century.
