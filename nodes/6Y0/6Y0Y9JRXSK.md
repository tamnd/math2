---
tag: 6Y0Y9JRXSK
kind: definition
name: Dimension of an algebraic variety
msc: [14A10, 13C15]
defines: 36X2WTHYCB
uses: [HV6YBS0YDH, SY2MWC434Z, 0ZCK8DQYN1, MVGBS3J1P7, G9WB27VWP7, JERVQT4C12, D7TR0YWR9H, 2D5SS6WM14]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_of_an_algebraic_variety
---

## Definition

Let $X$ be an [[algebraic variety|HV6YBS0YDH]] over an algebraically closed field $k$, with its Zariski topology.
The *dimension* $\dim X$ is the supremum of the integers $n$ such that there is a chain
$$Z_0 \subsetneq Z_1 \subsetneq \cdots \subsetneq Z_n$$
of [[irreducible|SY2MWC434Z]] [[closed subsets|0ZCK8DQYN1]] $Z_i$ of $X$.

## Remarks

For every variety this supremum is finite.
If $X$ is an [[affine variety|JERVQT4C12]], then $\dim X$ is the [[Krull dimension|MVGBS3J1P7]] of its [[coordinate ring|G9WB27VWP7]] $k[X]$.
The reason is that irreducible closed subsets of $X$ correspond to prime ideals of $k[X]$, with inclusions reversed.
For every variety, $\dim X$ equals the [[transcendence degree|D7TR0YWR9H]] of the [[function field|2D5SS6WM14]] $k(X)$ over $k$.
A nonempty open subset $U$ of $X$ has $\dim U = \dim X$.

Example: $\dim \mathbb{A}^n = \dim \mathbb{P}^n = n$, since $k(x_1, \dots, x_n)$ has transcendence degree $n$ over $k$.
The chain $\set{0} \subsetneq V(x_2, \dots, x_n) \subsetneq \cdots \subsetneq V(x_n) \subsetneq \mathbb{A}^n$ of linear subspaces has length $n$.

Example: if $f \in k[x_1, \dots, x_n]$ is irreducible and not constant, the hypersurface $V(f) \subseteq \mathbb{A}^n$ has dimension $n - 1$.

The dimension of a reducible algebraic set is the largest dimension of its irreducible components.
