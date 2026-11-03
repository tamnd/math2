---
tag: R9WFXME6GC
kind: object
name: Virasoro algebra
msc: [17B68, 81R10, 17B65]
instance_of: [5JJYBJ6A8K]
uses: [5JJYBJ6A8K, A7H11C2JMM, 8264A9XM74]
sources:
  - url: https://en.wikipedia.org/wiki/Virasoro_algebra
same_as:
  wikidata: Q1366201
  wikipedia: Virasoro algebra
---

## Description

The *Virasoro algebra* $\mathrm{Vir}$ is the complex [[Lie algebra|5JJYBJ6A8K]] with basis $L_n$ for $n \in \Z$ and $C$, and bracket
$$[L_m, L_n] = (m - n)\, L_{m+n} + \frac{C}{12}\, (m^3 - m)\, \delta_{m+n, 0}, \qquad [L_m, C] = 0,$$
for $m, n \in \Z$.
Here $\delta_{m+n, 0}$ is $1$ if $m + n = 0$ and $0$ otherwise.

The element $C$ is central.
The map $L_n \mapsto L_n$, $C \mapsto 0$ is a surjective Lie algebra homomorphism onto the [[Witt algebra|A7H11C2JMM]] with kernel $\C C$.
So $\mathrm{Vir}$ is a central [[extension|8264A9XM74]] of the Witt algebra by a one-dimensional abelian Lie algebra.
The extension does not split, and up to isomorphism it is the only nontrivial one-dimensional central extension of the Witt algebra.

Check on a small case: for $m \in \set{-1, 0, 1}$ the factor $m^3 - m$ vanishes.
So $L_{-1}, L_0, L_1$ have the same brackets as in the Witt algebra and span a copy of $\mathfrak{sl}_2(\C)$.
For $m = 2$ one gets $[L_2, L_{-2}] = 4 L_0 + \frac{C}{2}$.

## Remarks

In a representation where $C$ acts by a scalar $c$, the number $c$ is called the central charge.
Highest weight representations of $\mathrm{Vir}$ are labelled by the central charge $c$ and the eigenvalue $h$ of $L_0$ on a highest weight vector.
The Virasoro algebra acts on every vertex operator algebra, through the modes of the conformal vector.

## Explanations

### L1 human

The Virasoro algebra is the Witt algebra with one extra central element added.
The extra term in the bracket appears only for $[L_m, L_{-m}]$ and grows like $m^3$.
Physicists met this term when they quantized string theory and two-dimensional conformal field theories.
The classical symmetry algebra is the Witt algebra, but the quantum symmetries only close up to this central term.
The size of the central term, the central charge, is a basic invariant of such a theory.
