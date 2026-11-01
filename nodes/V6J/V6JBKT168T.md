---
tag: V6JBKT168T
kind: definition
name: Length of a module
msc: ["13C05", "16D10", "13E10"]
defines: CZSCNZH8VY
uses: [0894J980RK, 09VDS2W1E8, 0RGZ10DFPG, 0NB8VPB93V]
sources:
  - url: https://en.wikipedia.org/wiki/Length_of_a_module
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $M$ be a left [[module|09VDS2W1E8]] over $R$.
A chain of [[submodules|0RGZ10DFPG]] $M_0 \subsetneq M_1 \subsetneq \cdots \subsetneq M_n$ of $M$ has length $n$.
The *length* $\ell_R(M)$ of $M$ is the supremum of the lengths of all such chains, an element of $\set{0, 1, 2, \dots} \cup \set{\infty}$.

## Remarks

Example: for a finite-dimensional vector space $V$ over a field $k$, $\ell_k(V) = \dim_k V$.
Indeed, a strict chain of subspaces raises the dimension at each step, and a chain built from a basis has $\dim_k V$ steps.
Non-example of finite length: $\ell_\Z(\Z) = \infty$, because $2^n\Z \subsetneq 2^{n-1}\Z \subsetneq \cdots \subsetneq \Z$ has length $n$ for every $n$.
A composition series of $M$ is a chain $0 = M_0 \subsetneq \cdots \subsetneq M_n = M$ whose factors $M_i/M_{i-1}$ are simple modules.
A module $M$ has finite length if and only if it has a composition series, and then $\ell_R(M) = n$ by the [[Jordan–Hölder theorem for modules|M1ABX18FC4]].
For a short exact sequence $0 \to M' \to M \to M'' \to 0$, one has $\ell_R(M) = \ell_R(M') + \ell_R(M'')$.
The group version of a composition series is the [[composition series of a group|0NB8VPB93V]].

## Explanations

### L1 human

The length of a module counts the steps in the longest strict chain of submodules.
It is the module version of dimension.
