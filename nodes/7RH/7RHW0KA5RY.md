---
tag: 7RHW0KA5RY
kind: problem
name: Hilbert's twenty-first problem
msc: [34M50, 34M35]
uses: [C8HD62AB6Q, ZBVH2YE50B, H96HXG6CA0, RY8YQ9JZF9]
about: [C8HD62AB6Q, ZBVH2YE50B]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_twenty-first_problem
same_as:
  wikidata: Q4155615
  wikipedia: Hilbert's twenty-first problem
history:
  posed_by: "David Hilbert"
  first_stated: "1900"
---

## Problem

Let $a_1, \ldots, a_m$ be distinct points of the Riemann sphere, let $U$ be the sphere with these points removed, and fix $z_0 \in U$.
Let $\rho \colon \pi_1(U, z_0) \to \mathrm{GL}_n(\C)$ be a group homomorphism.
Does there exist a linear differential equation of Fuchsian class whose singular points are $a_1, \ldots, a_m$ and whose [[monodromy representation|C8HD62AB6Q]] is $\rho$?

## Remarks

In the form used today, the question is asked for first-order systems $Y' = A(z) Y$ of Fuchsian type, $A(z) = \sum_{i} \frac{A_i}{z - a_i}$ with constant matrices $A_i$, which have simple poles only.
If one only asks for a system with [[regular singular points|H96HXG6CA0]], the answer is positive; this was shown by Plemelj in 1908.
Plemelj's work was long taken as a positive solution for Fuchsian systems.
In 1989 Bolibrukh found a counterexample: a representation that is not the monodromy of any Fuchsian system with the given singular points.
The answer is positive when $\rho$ is irreducible, a result of Bolibrukh and of Kostov.
For scalar equations of order $n$, extra apparent singular points are needed in general.
Plemelj's approach reduces the question to a matrix [[Riemann–Hilbert problem|RY8YQ9JZF9]] on a curve through the singular points.

## Explanations

### L1 human

A linear differential equation with a few singular points has a monodromy: a rule that says how its solutions get mixed when one walks around each singular point.
Hilbert asked for the converse.
Given the points and any prescribed mixing rule, is there a tame (Fuchsian) equation that produces exactly this rule?
For a long time the answer was believed to be yes, but in 1989 it turned out to be no in general.
