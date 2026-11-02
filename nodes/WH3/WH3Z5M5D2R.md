---
tag: WH3Z5M5D2R
kind: definition
name: Completeness in order theory
msc: [06B23, 06A06]
defines: Q72NHN7ATC
uses: [0QV2JS9RJ3, 0R3H5PANRQ, 0QF1MZ9FRG, D9RY4667K6, D7A0ZGZT5S, CZPBQY67ZJ, 7TSXP95QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Completeness_(order_theory)
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]] and let $\mathcal{C}$ be a class of subsets of $P$.
The poset $P$ is *complete for* $\mathcal{C}$, or has all $\mathcal{C}$-joins, if every $S \in \mathcal{C}$ has a [[supremum|0R3H5PANRQ]] in $P$.
Dually, $P$ has all $\mathcal{C}$-meets if every $S \in \mathcal{C}$ has an [[infimum|0QF1MZ9FRG]] in $P$.
The standard choices of $\mathcal{C}$ are:

1. all subsets, giving a [[complete lattice|D7A0ZGZT5S]];
2. all finite nonempty subsets, giving a join-semilattice, and with meets as well, a lattice;
3. all nonempty subsets with an upper bound, giving (with the dual condition on lattices) a [[conditionally complete lattice|CZPBQY67ZJ]];
4. all [[directed subsets|D9RY4667K6]], giving a [[directed-complete partial order|7TSXP95QN6]];
5. all chains, giving a chain-complete poset.

## Remarks

Example: the power set of a set is complete for every class $\mathcal{C}$, since unions always exist.
Non-example: $\N$ with its usual order has all finite nonempty joins but is not directed-complete, because $\N$ itself is directed and has no supremum.
The empty set has a supremum if and only if $P$ has a least element.
If $P$ has all joins of arbitrary subsets, it also has all meets, so in case 1 one condition suffices.
