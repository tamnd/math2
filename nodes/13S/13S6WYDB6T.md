---
tag: 13S6WYDB6T
kind: definition
name: Unit-regular ring
msc: ["16E50", 16U90]
defines: H4K920SVYT
uses: [0894J980RK, 019NFGFPR5, DEV24TSWQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_regular_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with unit $1$.
The ring $R$ is *unit-regular* if for every $a \in R$ there is a [[unit|019NFGFPR5]] $u$ of $R$ such that
$$a u a = a.$$

## Remarks

A unit-regular ring is [[von Neumann regular|DEV24TSWQZ]].
Example: a division ring $D$; for $a \ne 0$ take $u = a^{-1}$, and for $a = 0$ take $u = 1$.
Example: the matrix ring $M_n(F)$ over a field $F$.
Write $A = PEQ$ with $P, Q$ invertible and $E = \operatorname{diag}(1, \ldots, 1, 0, \ldots, 0)$; then $u = Q^{-1} P^{-1}$ gives $AuA = PE^2Q = PEQ = A$.
A unit-regular ring is Dedekind-finite: if $ab = 1$ and $a = aua$, then $1 = ab = auab = au$, so $a = u^{-1}$ and $ba = 1$.
Non-example: let $V$ be a vector space with countable basis $e_1, e_2, \ldots$ over a field, and $R = \End(V)$.
The ring $R$ is von Neumann regular, but the shift $s(e_i) = e_{i+1}$ and $t$ with $t(e_1) = 0$, $t(e_{i+1}) = e_i$ satisfy $ts = 1 \ne st$.
So $R$ is not Dedekind-finite, hence not unit-regular.
