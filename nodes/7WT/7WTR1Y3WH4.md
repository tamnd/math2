---
tag: 7WTR1Y3WH4
kind: definition
name: Saturated model
msc: [03C50]
defines: RMTZ5J64FX
uses: [9V71Q3SD1G, MVCH6N9SNW, 0EBACQFAZW, 0G0ASKNA6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
---

## Definition

Let $L$ be a signature, let $M$ be an $L$-structure, and let $\kappa$ be an infinite [[cardinal|0EBACQFAZW]].
The structure $M$ is *$\kappa$-saturated* if the following holds for every set $A$ of elements of $M$ with $\abs{A} < \kappa$.
Every complete $1$-[[type|9V71Q3SD1G]] over $A$ is realized in $M$.
The structure $M$ is *saturated* if it is infinite and $\abs{M}$-saturated, where $\abs{M}$ is the [[cardinality|0G0ASKNA6Z]] of its domain.

## Remarks

A $\kappa$-saturated structure also realizes every complete $n$-type over fewer than $\kappa$ parameters, for every $n \ge 1$.

Example: $(\Q, <)$ is saturated.
A complete $1$-type over a finite set $A \subseteq \Q$ says where $x$ lies relative to the elements of $A$.
Either $x$ equals some $a \in A$, or $x$ lies in one of the open intervals cut out by $A$, including the two unbounded ones.
Each of these intervals contains a rational number, so the type is realized.

Non-example: the field $\overline{\Q}$ of algebraic numbers is a model of the theory of algebraically closed fields of characteristic $0$, but it is not $\aleph_0$-saturated.
The set $\set{f(x) \ne 0 : f \in \Z[x], f \ne 0}$ is consistent with its theory over $A = \emptyset$, as $\C$ shows, and it extends to a complete type.
No element of $\overline{\Q}$ realizes it, since every algebraic number is a root of a nonzero integer polynomial.

Every structure has a $\kappa$-saturated elementary extension for each $\kappa$.
Saturated models of the same complete theory and the same cardinality are isomorphic.
