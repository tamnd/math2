---
tag: XAQSNBJSX4
kind: definition
name: Inverse limit
msc: [18A30]
defines: DZB378CNCK
uses: [D9RY4667K6, A2DE66937D, 859F0TFVA3, CHS5AFJGWE]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_limit
---

## Definition

Let $(I, \le)$ be a [[directed set|D9RY4667K6]] and let $\mathcal{C}$ be a [[category|A2DE66937D]].
An *inverse system* in $\mathcal{C}$ over $I$ is a family of objects $A_i$ for $i \in I$ with [[morphisms|859F0TFVA3]] $f_{ij} \colon A_j \to A_i$ for all $i \le j$, such that:

1. $f_{ii} = \id_{A_i}$ for all $i$.
2. $f_{ij} \circ f_{jk} = f_{ik}$ for all $i \le j \le k$.

An *inverse limit* of this system is an object $A$ with morphisms $\pi_i \colon A \to A_i$ such that:

1. $f_{ij} \circ \pi_j = \pi_i$ for all $i \le j$.
2. For every object $B$ with morphisms $g_i \colon B \to A_i$ such that $f_{ij} \circ g_j = g_i$ for all $i \le j$, there is a unique morphism $u \colon B \to A$ with $\pi_i \circ u = g_i$ for all $i$.

## Remarks

The inverse limit is written $\varprojlim A_i$.
It is the [[limit|CHS5AFJGWE]] of the diagram given by the system, and it is unique up to a unique isomorphism.
In sets, groups, rings and modules it always exists.
There it is the set of families $(a_i) \in \prod_i A_i$ with $f_{ij}(a_j) = a_i$ for all $i \le j$, with the projections as $\pi_i$.

Example: the rings $\Z/p^n\Z$ for $n \ge 1$, with the reduction maps, form an inverse system over $\N$.
Its inverse limit is the ring $\Z_p$ of $p$-adic integers.
Clause 1 holds because reducing a compatible sequence at level $n+1$ gives its entry at level $n$.

Non-example: $\Z$ with the reduction maps $\Z \to \Z/p^n\Z$ satisfies clause 1 but not clause 2.
Taking $B = \Z_p$, a morphism $u \colon \Z_p \to \Z$ with $\pi_n \circ u$ equal to reduction would have to be injective, which is impossible since $\Z_p$ is uncountable.
