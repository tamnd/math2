---
tag: AE1VC00NZN
kind: definition
name: Right-angled Artin group
msc: [20F36, 20F65]
defines: 6D1DV09D6P
uses: [00C0BR7D7H, 0JGEQXQ4AC, 0KTW26C80J, 0WJX8MGG37]
sources:
  - url: https://en.wikipedia.org/wiki/Artin–Tits_group
---

## Definition

Let $\Gamma$ be a finite simple [[graph|00C0BR7D7H]] with vertex set $V$ and edge set $E$.
The *right-angled Artin group* $A(\Gamma)$ is the group with [[presentation|0JGEQXQ4AC]]
$$A(\Gamma) = \langle V \mid uv = vu \text{ for each edge } \set{u, v} \in E \rangle.$$
A group is a right-angled Artin group if it is isomorphic to $A(\Gamma)$ for some finite simple graph $\Gamma$.

## Remarks

Example: if $\Gamma$ has $n$ vertices and no edges, $A(\Gamma)$ is the [[free group|0KTW26C80J]] $F_n$; if $\Gamma$ is complete, $A(\Gamma)$ is the [[free abelian group|0WJX8MGG37]] $\Z^n$.
Example: if $\Gamma$ is the path $a - b - c$, the relations say that $b$ commutes with $a$ and $c$, and $a, c$ generate a free group, so $A(\Gamma) \cong F_2 \times \Z$.

Non-example: the braid group $B_3 = \langle a, b \mid aba = bab \rangle$ is an Artin group but not a right-angled one.
Its abelianisation is $\Z$, since the relation forces $a = b$ there; the only right-angled Artin group with abelianisation $\Z$ is $\Z$ itself, and $B_3$ is not abelian.

The abelianisation of $A(\Gamma)$ is $\Z^{V}$.
Two right-angled Artin groups $A(\Gamma)$ and $A(\Gamma')$ are isomorphic if and only if the graphs $\Gamma$ and $\Gamma'$ are isomorphic.
They are also called graph groups or partially commutative groups.
