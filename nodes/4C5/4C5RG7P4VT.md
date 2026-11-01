---
tag: 4C5RG7P4VT
kind: definition
name: Pointless topology
msc: [06D22, 18F70, 54A05]
defines: CYEMGH98WN
uses: [02BH3MCBQB, 0X3WGX95FE, 4N4DNDR22Z]
sources:
  - url: https://en.wikipedia.org/wiki/Pointless_topology
---

## Definition

A *frame* is a complete lattice $L$ such that $a \wedge \bigvee_{i \in I} b_i = \bigvee_{i \in I} (a \wedge b_i)$ for every $a \in L$ and every family $(b_i)_{i \in I}$ in $L$.
A *frame homomorphism* is a map between frames that preserves finite meets, including the top element, and arbitrary joins, including the bottom element.
The category of *locales* is the opposite of the category of frames and frame homomorphisms.
*Pointless topology* is the study of locales.
Each topological space $X$ gives the locale $\Omega(X)$, the frame of [[open sets|02BH3MCBQB]] of $X$ ordered by inclusion.
Each [[continuous map|0X3WGX95FE]] $f \colon X \to Y$ gives the frame homomorphism $f^{-1} \colon \Omega(Y) \to \Omega(X)$, hence a locale map $\Omega(X) \to \Omega(Y)$.

## Remarks

Example: for $X = \R$, the open sets form a frame, because $U \cap \bigcup_i V_i = \bigcup_i (U \cap V_i)$ for open sets $U, V_i$.
Non-example: the lattice of subspaces of $\R^2$ is complete but not a frame; for three distinct lines $a, b, c$ through $0$, $a \wedge (b \vee c) = a$ while $(a \wedge b) \vee (a \wedge c) = 0$.
A point of a locale $L$ is a frame homomorphism $L \to \set{0, 1}$; a locale is spatial if it is isomorphic to $\Omega(X)$ for some space $X$.
The functor $\Omega$ restricts to an equivalence between [[sober spaces|4N4DNDR22Z]] and spatial locales.
Every frame is a complete Heyting algebra; Mathlib calls frames `Order.Frame`.
