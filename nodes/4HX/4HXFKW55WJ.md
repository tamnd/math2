---
tag: 4HXFKW55WJ
kind: concept
name: K-groups of rings of integers
msc: ["11R70", "19F27", "19D50"]
specializes: [5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

The K-groups of the ring of integers $\mathcal{O}_F$ of a number field $F$ are Quillen's [[algebraic K-groups|5GVFZWMWC8]] $K_n(\mathcal{O}_F)$.
In low degrees they recover classical invariants: $K_0$ contains the ideal class group and $K_1$ is the unit group.
Quillen proved that all of them are finitely generated, and Borel computed their ranks.
Their orders and regulators are tied to special values of the Dedekind zeta function.

## Explanations

### L1 human

The ring of integers of a number field, such as $\Z$ or $\Z[i]$, is the basic object of algebraic number theory.
Its K-groups are a sequence of abelian groups that extend two classical invariants: the class group, which measures failure of unique factorization, and the group of units.
For $\Z$ the first ones are $K_0(\Z) = \Z$, $K_1(\Z) = \{\pm 1\}$, $K_2(\Z) = \Z/2$ and $K_3(\Z) = \Z/48$.
Higher K-groups carry deep arithmetic information, for instance about values of zeta functions at negative integers.
