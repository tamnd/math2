---
tag: P1JVA39H5E
kind: concept
name: Maurer–Cartan form
msc: ["22E60", 53C05]
specializes: [0E3G0GRPZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Maurer%E2%80%93Cartan_form
same_as:
  wikidata: Q552787
  wikipedia: Maurer–Cartan form
---

## Summary

The Maurer–Cartan form of a [[Lie group|7JBRGCVJRB]] $G$ is a [[differential form|0E3G0GRPZ6]] of degree one on $G$ with values in its Lie algebra $\mathfrak{g}$.
It translates each tangent vector of $G$ back to the identity by a left translation.
It is left-invariant and satisfies the Maurer–Cartan equation $d\omega + \tfrac12 [\omega \wedge \omega] = 0$, which encodes the Lie bracket.
It is the model for connection forms and for Cartan's method of moving frames.

## Explanations

### L1 human

At each point $g$ of a Lie group there is a tangent space, and left translation by $g^{-1}$ moves it to the tangent space at the identity.
The Maurer–Cartan form does exactly this: it reads every velocity of the group as a vector in one fixed space, the Lie algebra.
For a group of matrices, a velocity $V$ at $g$ is read as $g^{-1} V$, so the form is written $g^{-1}\,dg$.
For the circle group $e^{i\theta}$, it is $e^{-i\theta}\, d(e^{i\theta}) = i\, d\theta$.
