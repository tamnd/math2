---
tag: BE3XK5ERC1
kind: statement
role: theorem
name: Conjugacy of maximal tori
msc: ["22E15", 22C05]
uses: [9TFC6ADC1C, 3JVGZVVTB0, 0DEBXAJ5SA]
about: [3JVGZVVTB0]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_torus
---

## Statement

Let $G$ be a connected [[compact Lie group|9TFC6ADC1C]] and let $T$ be a [[maximal torus|3JVGZVVTB0]] of $G$.

1. For every maximal torus $T'$ of $G$ there is $g \in G$ with $T' = gTg^{-1}$.
2. Every element of $G$ lies in some maximal torus; equivalently, $G = \bigcup_{g \in G} gTg^{-1}$.

## Remarks

One proof uses the Lefschetz fixed point theorem on the manifold $G/T$.
For $x \in G$, the map $gT \mapsto xgT$ of $G/T$ is homotopic to the identity, since $G$ is connected.
So its Lefschetz number is the Euler characteristic of $G/T$, which equals the order of the Weyl group and is nonzero.
A fixed point $gT$ means $xgT = gT$, that is, $g^{-1}xg \in T$; this gives part 2, and part 1 follows by taking for $x$ a generator of a dense cyclic subgroup of $T'$.
Example: for $G = U(n)$ and $T$ the diagonal unitary matrices, part 2 is the spectral theorem: every unitary matrix is $g D g^{-1}$ with $g$ unitary and $D$ diagonal.
Connectedness is needed for part 2: in $O(2)$, every torus lies in the identity component $SO(2)$, so a reflection lies in no maximal torus.

## Explanations

### L1 human

In a compact connected Lie group there is essentially only one maximal torus: all of them are rotated copies of each other.
Moreover these copies cover the whole group.
For unitary matrices this is the familiar fact that every unitary matrix becomes diagonal in a suitable orthonormal basis.

### L2 human

Part 2 implies that a continuous class function on $G$ is determined by its restriction to $T$, and that restriction is invariant under the [[Weyl group|EZGTEK3HQN]].
This is why characters of representations are studied on $T$, and why the [[Weyl integration formula|QMH530N27M]] reduces integrals of class functions to integrals over $T$.
It also implies that the exponential map of a compact connected Lie group is surjective, since it is surjective on each torus.
