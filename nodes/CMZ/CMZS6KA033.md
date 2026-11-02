---
tag: CMZS6KA033
kind: statement
role: theorem
name: Weil's converse to Haar's theorem
msc: [28C10, "22D05", "03E15"]
uses: [ABEFWF4JHH, WEBBT18D4X, FCNQP0A60D, AHV05ZBCYW, 03PPNCM9GG, VY0HXD3GC4]
about: [VY0HXD3GC4, AHV05ZBCYW]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Statement

Let $G$ be a group with a [[standard Borel|ABEFWF4JHH]] structure $\mathcal{B}$ such that the map $G \times G \to G$, $(x, y) \mapsto x y^{-1}$, is Borel.
Let $\mu$ be a nonzero [[σ-finite measure|WEBBT18D4X]] on $\mathcal{B}$ that is left [[quasi-invariant|FCNQP0A60D]]: for every $g \in G$ and $A \in \mathcal{B}$, $\mu(gA) = 0$ if and only if $\mu(A) = 0$.
Then there is exactly one topology on $G$ with the following two properties.

1. With it, $G$ is a Hausdorff [[locally compact group|AHV05ZBCYW]] that is [[second countable|03PPNCM9GG]].
2. Its Borel $\sigma$-algebra is $\mathcal{B}$.

For this topology, $\mu$ has the same null sets as a left [[Haar measure|VY0HXD3GC4]] of $G$.

## Remarks

[[Haar's theorem|KB792QTG4F]] goes from a topology to an invariant measure; this result goes back from an invariant measure to a topology.
Weil's original version starts from a group with a left-invariant measure that separates points in a suitable sense.
It defines a topology from the measure, called the Weil topology.
The completion of the group in this topology is locally compact, and the given measure is essentially a Haar measure on it.
The form stated here, for standard Borel groups and quasi-invariant measures, is due to Mackey.
The idea is that the sets $\set{g : \mu(gA \,\triangle\, A) < \varepsilon}$, for $A$ of finite positive measure and $\varepsilon > 0$, generate the neighbourhoods of the identity: their finite intersections form a base.
Example: a Polish group that is not locally compact, such as the additive group of an infinite-dimensional separable Hilbert space, carries no nonzero σ-finite left quasi-invariant Borel measure.
This explains why there is no analogue of Lebesgue measure on such a space.

## Explanations

### L1 human

Haar's theorem says that every locally compact group has a way to measure size that does not change under translation.
This theorem says the converse.
If a reasonable group has a translation-invariant way to measure size, at least up to sets of size zero, then the group is locally compact.
So invariant measures and local compactness go together.

### L2 human

The theorem is used to show that a group has no Haar-like measure: one checks that it cannot be locally compact.
A standard case is an infinite-dimensional Banach space, which is a Polish group under addition but is not locally compact.
In representation theory, the result lets one recover the topology of a locally compact group from its Borel structure and its measure class.
It connects to [[quasi-invariant measures|FCNQP0A60D]]: on a second countable locally compact group, every σ-finite left quasi-invariant measure has the same null sets as Haar measure.
