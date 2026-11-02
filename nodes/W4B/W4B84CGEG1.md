---
tag: W4B84CGEG1
kind: definition
name: Elliptic operator on a compact manifold
msc: [58J05, 47F10, 35J46]
defines: MT9P2X85V8
uses: [CGBX1N9V8H, S8GC34D5ZG, XY8GEQSWPR, P4DZM975BV, F45VQ47GPV, F4NWZNTRMD, 0ZHSTAG8ZY]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
---

## Definition

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] without boundary, and let $E$ and $F$ be smooth [[vector bundles|P4DZM975BV]] over $M$.
Let $P \colon \Gamma(E) \to \Gamma(F)$ be a [[differential operator|CGBX1N9V8H]] of order $m$ with [[principal symbol|S8GC34D5ZG]] $\sigma_m(P)$.
The operator $P$ is *elliptic* if the linear map
$$\sigma_m(P)(x, \xi) \colon E_x \to F_x$$
is invertible for every $x \in M$ and every nonzero $\xi \in T^*_x M$.

## Remarks

When $\dim M \ge 1$, the condition forces $E$ and $F$ to have the same rank, since an invertible linear map exists only between spaces of equal dimension.
On an open subset of $\R^n$ with $E$ and $F$ trivial of rank $1$, it is the usual condition for an [[elliptic operator|XY8GEQSWPR]].

Example: let $(M, g)$ be a closed Riemannian manifold and let $\Delta = -\operatorname{div} \operatorname{grad}$ be the [[Laplace–Beltrami operator|F4NWZNTRMD]] on functions.
Its principal symbol is $\sigma_2(\Delta)(x, \xi) = -\abs{\xi}_g^2$, which is a nonzero number for $\xi \ne 0$, so $\Delta$ is elliptic.

Non-example: on a closed manifold $M$ of dimension $n \ge 2$, the [[exterior derivative|0ZHSTAG8ZY]] $d$ from functions to $1$-forms is not elliptic.
Its symbol at $\xi$ is the map $\R \to T^*_x M$, $c \mapsto c \, \xi$, which is injective but not surjective, since $T^*_x M$ has dimension $n > 1$.

## Explanations

### L1 human

An operator on bundles over a closed manifold is elliptic when its top-order part is an invertible matrix in every nonzero frequency direction.
