---
tag: 353YPJWBBR
kind: definition
name: Hermitian metric on a vector bundle
msc: [32L05, 53C55]
defines: Q6X6W2N29G
uses: [P4DZM975BV, 0NB0AWGJBW, WWX7H5W1RP]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_manifold
---

## Definition

Let $X$ be a smooth manifold and let $E \to X$ be a smooth complex [[vector bundle|P4DZM975BV]].
A *Hermitian metric* on $E$ is a family $h = (h_x)_{x \in X}$ such that:

1. For each $x \in X$, $h_x \colon E_x \times E_x \to \C$ is a [[Hermitian inner product|0NB0AWGJBW]] on the fibre $E_x$.
   So it is $\C$-linear in the first argument, $h_x(w, v) = \overline{h_x(v, w)}$, and $h_x(v, v) > 0$ for $v \ne 0$.
2. For any two smooth local [[sections|WWX7H5W1RP]] $s, t$ of $E$ over an open set $U$, the function $x \mapsto h_x(s(x), t(x))$ is smooth on $U$.

## Remarks

In a local frame $e_1, \dots, e_r$ of $E$ over $U$, a Hermitian metric is the same as a smooth map $H = (h(e_j, e_i))_{i,j}$ from $U$ to the positive definite Hermitian $r \times r$ matrices.
A vector bundle with a Hermitian metric is called a Hermitian vector bundle.
When $X$ is a complex manifold and $E$ is its holomorphic tangent bundle, a Hermitian metric on $E$ is a Hermitian metric on $X$ in the sense of [[Hermitian manifolds|CK1DCPC3D3]].

Example: on $\mathcal{O}(-1) \subset \mathbb{P}^n \times \C^{n+1}$, restrict the standard inner product $\sum_k v_k \bar w_k$ of $\C^{n+1}$ to each fibre.
Each restriction is a Hermitian inner product, and for a local holomorphic section such as $s(z) = (1, z_1, \dots, z_n)$ on $\set{z_0 \ne 0}$ one gets $h(s, s) = 1 + \abs{z_1}^2 + \cdots + \abs{z_n}^2$, which is smooth.

Non-example: on the trivial line bundle $\C \times \C \to \C$, the rule $h_z(v, w) = \abs{z}^2 v \bar w$ is smooth, but $h_0(v, v) = 0$ for all $v$, so clause 1 fails at $z = 0$.
