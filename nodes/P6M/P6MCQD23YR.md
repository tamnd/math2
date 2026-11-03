---
tag: P6MCQD23YR
kind: definition
name: Algebraic K-theory of schemes
msc: ["19E08", 14C35]
defines: Y2467453Q5
uses: [5A35TYZD02, P4DZM975BV, TFADSC9YPZ, 0YMSEZE1VH]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Definition

Let $X$ be a [[scheme|5A35TYZD02]], and let $\mathcal{P}(X)$ be the category of [[vector bundles|P4DZM975BV]] on $X$, that is, locally free $\mathcal{O}_X$-modules of finite rank.
With the short exact sequences of $\mathcal{O}_X$-modules, $\mathcal{P}(X)$ is an [[exact category|TFADSC9YPZ]].
For $n \ge 0$, the *$n$-th algebraic K-group* of $X$ is $K_n(X) = \pi_{n+1}\big(B Q \mathcal{P}(X), 0\big)$.
This is a homotopy group of the classifying space of Quillen's [[Q-construction|J9XP7CS943]] on $\mathcal{P}(X)$, at the base point given by the zero bundle.

## Remarks

The group $K_0(X)$ is the [[Grothendieck group of vector bundles|A4393CW9G4]].
It is the quotient of the [[free abelian group|0YMSEZE1VH]] on isomorphism classes $[E]$ of vector bundles by the following relations.
For every short exact sequence $0 \to E' \to E \to E'' \to 0$, one sets $[E] = [E'] + [E'']$.
The tensor product makes $K_0(X)$ a commutative ring.
Example: for $X = \operatorname{Spec} k$ with $k$ a field, every exact sequence of finite-dimensional vector spaces splits, and $K_0(X) \cong \Z$ through the dimension; also $K_1(X) \cong k^{\times}$.
For $X = \mathbb{P}^n_k$, $K_0(X)$ is free of rank $n + 1$ with basis $[\mathcal{O}], [\mathcal{O}(-1)], \ldots, [\mathcal{O}(-n)]$.
Non-example: using all coherent sheaves instead of vector bundles gives the groups $G_n(X)$, which differ in general.
For a regular separated Noetherian scheme the natural maps $K_n(X) \to G_n(X)$ are isomorphisms, but for a singular one they need not be.
For general schemes, Thomason and Trobaugh gave a better-behaved version using perfect complexes, which agrees with this one when $X$ has an ample family of line bundles.
