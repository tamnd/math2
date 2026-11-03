---
tag: YDSX9RDM1C
kind: concept
name: K0 of coherent sheaves
msc: ["19E08", "14C35"]
specializes: [5FDMY7PDYY]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck–Riemann–Roch_theorem
---

## Summary

The group $K_0$ of coherent sheaves on a Noetherian scheme $X$ is often written $G_0(X)$ or $K'_0(X)$.
It is the [[Grothendieck group|5FDMY7PDYY]] of the abelian category of [[coherent sheaves|56RXEJ8Z6S]] on $X$.
Each coherent sheaf gives a class, and a short exact sequence makes the middle class the sum of the outer two.
Grothendieck introduced it to state the [[Grothendieck–Riemann–Roch theorem|3HKREN3Y3F]], since it has pushforwards along proper morphisms.
On a regular separated Noetherian scheme it agrees with the K-group of vector bundles.

## Explanations

### L1 human

Think of a coherent sheaf as a family of finite-dimensional vector spaces spread over a space, whose dimension may jump at some points.
The group $G_0(X)$ keeps only the information that survives cutting such families into pieces by exact sequences.
Over a single point a coherent sheaf is a finite-dimensional vector space, and its class is just its dimension, so $G_0$ of a point is $\Z$.
Over $\operatorname{Spec} \Z$ the sequence $0 \to \Z \xrightarrow{p} \Z \to \Z/p \to 0$ shows that the torsion module $\Z/p$ has class $0$.
