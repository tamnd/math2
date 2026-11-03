---
tag: TB7VCE0RS6
kind: definition
name: Murray–von Neumann equivalence
msc: [46L05, 46L80, 46L10]
defines: GT9S7APKG1
uses: [M2WFY1D3SZ, GGDSF85JPD]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Definition

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]].
A projection in $A$ is an element $p$ with $p = p^* = p^2$.
Two projections $p, q \in A$ are *Murray–von Neumann equivalent*, written $p \sim q$, if there is $v \in A$ with
$$v^* v = p \quad \text{and} \quad v v^* = q.$$

## Remarks

Such a $v$ is a [[partial isometry|GGDSF85JPD]] with initial projection $p$ and final projection $q$.
The relation is reflexive ($v = p$), symmetric ($v^*$ in place of $v$), and transitive (if $v^*v = p$, $vv^* = q$, $w^*w = q$, $ww^* = r$, then $wv$ works for $p$ and $r$).
Example: in $B(\ell^2(\N))$ let $s e_k = e_{2k}$; then $s^* s = 1$ and $s s^*$ is the projection onto the span of the $e_{2k}$, so this projection is equivalent to $1$.
Non-example: in $M_2(\C)$, the projections $\operatorname{diag}(1, 0)$ and $1$ are not equivalent, since $v^*v$ and $vv^*$ always have the same rank.
For K-theory one uses the same relation for projections in matrix algebras of different sizes, with $v$ a rectangular matrix over $A$.
Unitarily equivalent projections are Murray–von Neumann equivalent, but the converse fails in general, as the example above shows.
