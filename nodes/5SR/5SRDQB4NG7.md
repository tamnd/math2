---
tag: 5SRDQB4NG7
kind: definition
name: Ribbon Hopf algebra
msc: [16T05, 18M15, 57K16]
defines: K49YFHYCHA
uses: [NCRPWS9W5R, 7XFYP0N84H]
sources:
  - url: https://en.wikipedia.org/wiki/Ribbon_Hopf_algebra
---

## Definition

Let $(H, R)$ be a [[quasitriangular Hopf algebra|NCRPWS9W5R]] over a field $k$, with coproduct $\Delta$, counit $\varepsilon$ and antipode $S$.
Write $R = \sum_i a_i \otimes b_i$, let $R_{21} = \sum_i b_i \otimes a_i$, and let $u = \sum_i S(b_i)\, a_i$ be the Drinfeld element.
A *ribbon element* of $H$ is a central invertible element $v \in H$ such that:

1. $v^2 = u\, S(u)$.
2. $S(v) = v$.
3. $\varepsilon(v) = 1$.
4. $\Delta(v) = (R_{21} R)^{-1} (v \otimes v)$.

A *ribbon Hopf algebra* is a quasitriangular Hopf algebra together with a ribbon element.

## Remarks

Example: let $H = k[G]$ be the group algebra of a group $G$ with $R = 1 \otimes 1$.
Then $u = S(1) \cdot 1 = 1$, and $v = 1$ is central and invertible.
Clauses 1 to 3 read $1 = 1$, and clause 4 reads $1 \otimes 1 = (1 \otimes 1)^{-1}(1 \otimes 1)$.
Non-example: in the same algebra with $\operatorname{char} k \ne 2$, the element $v = -1$ satisfies clauses 1 and 2 but fails clause 3, since $\varepsilon(-1) = -1$.
The Drinfeld element $u$ is invertible and satisfies $S^2(x) = u x u^{-1}$ for all $x \in H$.
Some authors use $v^{-1}$ in place of $v$, which changes clause 4 to $\Delta(v) = (v \otimes v) R_{21} R$.
