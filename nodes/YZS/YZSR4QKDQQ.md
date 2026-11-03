---
tag: YZSR4QKDQQ
kind: concept
name: G-theory
msc: [19A49, 19D99, "16E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

G-theory is the K-theory of all finitely generated modules over a Noetherian ring, rather than only the projective ones.
Its first group $G_0(R)$ is the [[Grothendieck group|2H7Y1XC93S]] of the abelian category of finitely generated $R$-modules, and the higher groups $G_n(R)$ come from Quillen's construction.
It is also called the K-theory of coherent sheaves, or K'-theory, and it has good localization properties.
For a regular Noetherian ring it agrees with [[algebraic K-theory|5GVFZWMWC8]], by the [[resolution theorem|DYV91576BQ]].

## Explanations

### L1 human

Algebraic K-theory uses only projective modules, which behave like vector bundles.
G-theory allows all finitely generated modules, including torsion modules such as $\Z/n\Z$.
A module built from a submodule and a quotient counts as their sum.
For the integers this gives $G_0(\Z) = \Z$, given by the rank, because every finite abelian group counts as zero.
Allowing all modules makes G-theory easier to cut into pieces, which is why it is used for localization arguments.
