---
tag: NEYHC1XZ14
kind: statement
role: theorem
name: Dulac's theorem on finiteness of limit cycles
msc: [34C07]
uses: [0AAQ73WRFB, 0673D85QKZ]
about: [0AAQ73WRFB]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_sixteenth_problem
---

## Statement

Let $P$ and $Q$ be real polynomials in two variables.
Then the planar [[autonomous system|0673D85QKZ]]
$$x' = P(x, y), \qquad y' = Q(x, y)$$
has only finitely many [[limit cycles|0AAQ73WRFB]].

## Remarks

Henri Dulac published a proof in 1923, but a gap was found in it much later.
Complete proofs were given independently by Yulij Ilyashenko and by Jean Écalle around 1991–1992.
The hard part is to exclude limit cycles that accumulate on a polycycle, a closed chain of equilibria joined by orbits.
Limit cycles cannot accumulate on a periodic orbit of an analytic field, because the Poincaré return map near that orbit is analytic.

The theorem bounds the number of limit cycles of each single system.
It gives no bound in terms of the degree of $P$ and $Q$.
Whether such a bound exists, even for degree $2$, is the second part of Hilbert's sixteenth problem, and it is open.
For example, the van der Pol system $x' = y - (x^3/3 - x)$, $y' = -x$ has exactly one limit cycle.

## Explanations

### L1 human

A limit cycle is an isolated closed loop of motion in the plane.
The theorem says that a system given by polynomial formulas can only have finitely many of them.
It does not say how many, and nobody knows a general bound in terms of the degrees of the polynomials.

### L2 human

The theorem is the finiteness part of the study of Hilbert's sixteenth problem on limit cycles.
Near a periodic orbit, finiteness follows from the analyticity of the return map.
The difficulty lies at polycycles, where the return map has an asymptotic expansion that is not convergent.
Ilyashenko and Écalle overcame this with a theory of such expansions.
