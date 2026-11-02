---
tag: 2BDH4RQZQ9
kind: definition
name: Unitary dual
msc: ["22D10", "43A40"]
defines: 95Q8WZMN0W
uses: [AHV05ZBCYW, 74BPYJNZTM, FX3NEFYFFN]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_representation
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]].
Two [[unitary representations|74BPYJNZTM]] $\pi_1$ on $H_1$ and $\pi_2$ on $H_2$ are *unitarily equivalent* if there is a unitary operator $T \colon H_1 \to H_2$ with $T\pi_1(g) = \pi_2(g)T$ for all $g \in G$.
The *unitary dual* $\widehat{G}$ of $G$ is the set of unitary equivalence classes of [[irreducible|FX3NEFYFFN]] unitary representations of $G$.

## Remarks

Unitary equivalence is an equivalence relation, so $\widehat{G}$ is well defined.
It is usually given the Fell topology, which comes from the identification of $\widehat{G}$ with the spectrum of the group C\*-algebra $C^*(G)$.

Example: $G = \R$.
By Schur's lemma, every irreducible unitary representation of an abelian group is one-dimensional, so it is a continuous homomorphism $\R \to \set{z \in \C : \abs{z} = 1}$.
These are the maps $x \mapsto e^{ixy}$ with $y \in \R$, and different $y$ give inequivalent representations, so $\widehat{\R}$ is in bijection with $\R$.

Non-example: the representation of $\R$ on $L^2(\R)$ by translations $f \mapsto f(\cdot - t)$ does not define a point of $\widehat{\R}$, since it is not irreducible.
The closed subspace of functions whose Fourier transform vanishes on $(-\infty, 0)$ is invariant under all translations and is neither $0$ nor $L^2(\R)$.

For a locally compact abelian group, $\widehat{G}$ is the group of continuous characters, the Pontryagin dual.
For a compact group, every element of $\widehat{G}$ is finite-dimensional.
