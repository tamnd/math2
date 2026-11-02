---
tag: 28DVNYNMZR
kind: definition
name: Tautological line bundle
msc: [14C20, 14M15]
defines: BDB06N91FN
uses: [05EGHEQZAW, ZT9A6JK8QF, P4DZM975BV, V93Y0XYPZD]
sources:
  - url: https://en.wikipedia.org/wiki/Tautological_bundle
---

## Definition

Let $k$ be a field, $V$ a [[vector space|05EGHEQZAW]] over $k$ of dimension $n + 1$, and $\mathbb{P}(V)$ the [[projective space|ZT9A6JK8QF]] of lines in $V$.
The *tautological line bundle* on $\mathbb{P}(V)$ is the closed subvariety
$$L = \set{(\ell, v) \in \mathbb{P}(V) \times V : v \in \ell}$$
together with the projection $L \to \mathbb{P}(V)$.
Its fibre over a point $\ell$ is the line $\ell \subseteq V$ itself.
Its sheaf of sections is a [[vector bundle|P4DZM975BV]] of rank $1$, isomorphic to $\mathcal{O}_{\mathbb{P}(V)}(-1)$.

## Remarks

For $V = k^2$, a point of $\mathbb{P}^1$ is $\ell = [a : b]$, and the fibre of $L$ over it is $\set{t(a, b) : t \in k}$.
Over the open set $a \ne 0$, the map $(\ell, t(1, b/a)) \mapsto (\ell, t)$ trivializes $L$, so $L$ is locally a product with a line.
The projection $L \to \mathbb{P}(V)$ is a line bundle but not the trivial one when $n \ge 1$.
Indeed, $\mathcal{O}(-1)$ has no nonzero global sections, while a trivial bundle has a nowhere-zero section.
The dual of $L$ corresponds to [[Serre's twisting sheaf|V93Y0XYPZD]] $\mathcal{O}(1)$, whose global sections are the linear forms on $V$.
Some authors write $\mathbb{P}(V)$ for the space of hyperplanes of $V$, which changes the sign conventions.
