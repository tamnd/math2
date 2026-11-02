---
tag: 88XF0NVBVG
kind: definition
name: Diagram
msc: [18A10, 18A30]
defines: HJK75HDWFE
uses: [A2DE66937D, 28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Diagram_(category_theory)
---

## Definition

Let $J$ and $\mathcal{C}$ be [[categories|A2DE66937D]].
A *diagram of shape $J$* in $\mathcal{C}$ is a [[functor|28NQ0KRHD3]] $D \colon J \to \mathcal{C}$.
The category $J$ is called the *index category* or *shape* of the diagram.
The diagram is *small* if $J$ is small, and *finite* if $J$ has finitely many objects and morphisms.

## Remarks

The objects $D(j)$ and morphisms $D(u)$ for $u$ in $J$ form the picture that the diagram draws in $\mathcal{C}$.
Because $D$ is a functor, $D(v \circ u) = D(v) \circ D(u)$, so every composite in $J$ is sent to the corresponding composite in $\mathcal{C}$.

Example: let $J$ have three objects $1, 2, 3$ and, besides identities, morphisms $u \colon 1 \to 3$ and $v \colon 2 \to 3$.
A diagram of shape $J$ in the category of sets is a pair of functions $f = D(u) \colon X \to Z$ and $g = D(v) \colon Y \to Z$; its limit is the pullback of $f$ and $g$.

Non-example: let $J$ have one object $\ast$ and one non-identity morphism $e$ with $e \circ e = e$.
Sending $\ast$ to $\Z$ and $e$ to the map $n \mapsto -n$ is not a diagram of shape $J$ in the category of sets.
The image of $e \circ e$ would have to be $n \mapsto -n$, but the composite of $n \mapsto -n$ with itself is the identity.
