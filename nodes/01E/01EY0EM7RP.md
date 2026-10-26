---
tag: 01EY0EM7RP
kind: statement
role: proposition
name: Extensions of solvable groups are solvable
msc: [20F16]
uses: [0P3KZK0FTV, 0R3H35G96G, 027ZQS04SJ, 05Y0F9M0TS]
sources:
  - url: https://en.wikipedia.org/wiki/Solvable_group
    locator: Properties
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
If $N$ and $G/N$ are [[solvable|0FXJ7YFMMX]], then $G$ is solvable.

## Remarks

If $(G/N)^{(k)}$ is trivial, then $G^{(k)} \subseteq N$, so $G^{(k+m)} \subseteq N^{(m)}$ for each $m$.
Choose $m$ with $N^{(m)} = \{e\}$; then $G^{(k+m)} = \{e\}$.
With [[subgroups|05Y0F9M0TS]] and [[quotients|027ZQS04SJ]], this gives: $G$ is solvable if and only if $N$ and $G/N$ are solvable.
In particular, direct products and semidirect products of solvable groups are solvable.

## Explanations

### L1 human

If the bottom part and the top part of a group can both be built from abelian layers, then so can the whole group.
You stack the layers of the top part on the layers of the bottom part.
For example, $S_4$ is built from $V$, $A_4/V$ and $S_4/A_4$.
