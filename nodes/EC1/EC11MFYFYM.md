---
tag: EC11MFYFYM
kind: concept
name: Bloch group
msc: ["19D45", "11G55", "19F27"]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch_group
same_as:
  wikidata: Q4927103
  wikipedia: Bloch group
---

## Summary

The Bloch group $\mathcal{B}(F)$ of a field $F$ is an abelian group built from symbols $[x]$ for $x \in F \setminus \{0, 1\}$.
The symbols satisfy the five-term relation of the [[dilogarithm|G0X0NWSDB7]].
Suslin showed that it is closely related to the indecomposable part of $K_3(F)$.
For number fields the [[Bloch–Wigner function|Q8K5MWEXB9]] on the Bloch group gives the Borel regulator on $K_3$.
It therefore computes values of the Dedekind zeta function at $s = 2$.

## Explanations

### L1 human

The dilogarithm satisfies a famous identity with five terms.
The Bloch group takes formal symbols $[x]$, one for each element of a field other than $0$ and $1$, and imposes exactly this identity.
It then keeps only the combinations that pass a simple test involving $x$ and $1 - x$.
What remains turns out to be almost the same as the third K-group of the field, so the dilogarithm becomes a tool to compute in K-theory.
For the complex numbers, the Bloch–Wigner function gives a well-defined real number for each element of the Bloch group.
For a symbol $[z]$ with $z$ in the upper half-plane, this number is the volume of an ideal hyperbolic tetrahedron.
