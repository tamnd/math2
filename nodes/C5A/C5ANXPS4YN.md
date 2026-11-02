---
tag: C5ANXPS4YN
kind: definition
name: Cone
msc: [18A30]
defines: 7TPBQPPN97
uses: [A2DE66937D, 859F0TFVA3, HJK75HDWFE, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Cone_(category_theory)
---

## Definition

Let $J$ and $\mathcal{C}$ be [[categories|A2DE66937D]] and let $D \colon J \to \mathcal{C}$ be a [[diagram|HJK75HDWFE]].
A *cone* over $D$ is an object $N$ of $\mathcal{C}$, the *apex*, with a [[morphism|859F0TFVA3]] $\psi_j \colon N \to D(j)$ for each object $j$ of $J$.
The morphisms must satisfy $D(u) \circ \psi_j = \psi_k$ for every morphism $u \colon j \to k$ of $J$.
A *cocone* under $D$ is an object $N$ together with morphisms $\psi_j \colon D(j) \to N$ such that $\psi_k \circ D(u) = \psi_j$ for every $u \colon j \to k$.
A morphism of cones $(N, \psi) \to (N', \psi')$ over $D$ is a morphism $h \colon N \to N'$ with $\psi'_j \circ h = \psi_j$ for all $j$.

## Remarks

A cone with apex $N$ is the same as a [[natural transformation|KYCPCC57FT]] $\Delta N \Rightarrow D$, where $\Delta N \colon J \to \mathcal{C}$ is the constant functor with value $N$; the condition $D(u) \circ \psi_j = \psi_k$ is its naturality square.
Cones over $D$ and their morphisms form a category, written $\mathrm{Cone}(D)$.

Example: let $D$ be the diagram $f, g \colon X \rightrightarrows Y$ of two parallel functions between sets.
Let $N = \set{x \in X : f(x) = g(x)}$, let $\psi_X$ be the inclusion and let $\psi_Y = f \circ \psi_X$.
The conditions $f \circ \psi_X = \psi_Y$ and $g \circ \psi_X = \psi_Y$ hold because $f$ and $g$ agree on $N$, so this is a cone.

Non-example: in the same diagram take $N = X$, $\psi_X = \id_X$ and $\psi_Y = f$.
If $f \neq g$, then $g \circ \psi_X = g \neq \psi_Y$, so the condition fails for the morphism $g$ and this is not a cone.
