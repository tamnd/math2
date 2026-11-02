---
tag: 3S7HJ5GQRF
kind: concept
name: Dissipative operator
msc: [47B44, 47D06]
sources:
  - url: https://en.wikipedia.org/wiki/Dissipative_operator
same_as:
  wikidata: Q1229326
  wikipedia: Dissipative operator
---

## Summary

A dissipative operator is a linear operator $A$ on a Banach space such that $\norm{(\lambda - A)x} \ge \lambda \norm{x}$ for every $\lambda > 0$.
On a Hilbert space this means $\operatorname{Re}\ip{Ax}{x} \le 0$ for every $x$ in the domain.
The densely defined maximal dissipative operators are exactly the generators of semigroups that do not increase norms, by the [[Lumer–Phillips theorem|Z2N8MPD8DH]].
The name comes from physics: the evolution $u' = Au$ loses energy and never gains it.

## Explanations

### L1 human

Think of $u' = Au$ as a law of motion and of $\norm{u}^2$ as an energy.
On a Hilbert space, the derivative of $\norm{u(t)}^2$ is $2 \operatorname{Re}\ip{Au}{u}$, so dissipativity says the energy can only go down.
The heat equation is the main example: heat spreads out and the total squared temperature decreases.
In one dimension, $\ip{f''}{f} = -\int \abs{f'}^2 \, dx \le 0$ for smooth $f$ that vanish at the ends, so the second derivative is dissipative.
The operator $-A$ of a dissipative $A$ is called accretive.
