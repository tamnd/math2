---
tag: HWGM5P7KCK
kind: definition
name: Gluing of schemes
msc: [14A15]
defines: ABVBHCA9VW
uses: [5A35TYZD02, JXRKH6P1Z4, GFC5YKSN5H]
sources:
  - url: https://en.wikipedia.org/wiki/Gluing_schemes
---

## Definition

Let $I$ be an index set, and for each $i \in I$ let $X_i$ be a [[scheme|5A35TYZD02]].
For all $i, j \in I$, let $U_{ij} \subseteq X_i$ be an open subscheme with $U_{ii} = X_i$.
Let $\varphi_{ij} \colon U_{ij} \to U_{ji}$ be isomorphisms of schemes such that:

1. $\varphi_{ii}$ is the identity of $X_i$ for every $i$.
2. $\varphi_{ij}(U_{ij} \cap U_{ik}) = U_{ji} \cap U_{jk}$ for all $i, j, k$.
3. $\varphi_{ik} = \varphi_{jk} \circ \varphi_{ij}$ on $U_{ij} \cap U_{ik}$ for all $i, j, k$ (the cocycle condition).

A *gluing* of these data is a scheme $X$ with [[open immersions|GFC5YKSN5H]] $\psi_i \colon X_i \to X$ such that:

1. the open sets $\psi_i(X_i)$ cover $X$;
2. $\psi_i(U_{ij}) = \psi_i(X_i) \cap \psi_j(X_j)$ for all $i, j$;
3. $\psi_i = \psi_j \circ \varphi_{ij}$ on $U_{ij}$ for all $i, j$.

Such a gluing always exists, and it is unique up to a unique isomorphism compatible with the maps $\psi_i$.

## Remarks

Example: let $k$ be a field, $X_1 = \operatorname{Spec} k[t]$, $X_2 = \operatorname{Spec} k[s]$, $U_{12} = D(t)$ and $U_{21} = D(s)$.
Let $\varphi_{12}$ be the isomorphism given by the ring map $k[s, s^{-1}] \to k[t, t^{-1}]$, $s \mapsto t^{-1}$, and $\varphi_{21} = \varphi_{12}^{-1}$.
With only two indices the cocycle condition holds, and the gluing is the projective line $\mathbb{P}^1_k$.
If instead $\varphi_{12}$ is given by $s \mapsto t$ on $D(t)$, the gluing is the affine line with a doubled origin, which is a scheme but not a separated one.
Non-example: with $\varphi_{12}$ as in the first example, take $\varphi_{21}$ to be given by $t \mapsto 2s^{-1}$ over a field $k$ with $2 \ne 0$.
The composite $\varphi_{21} \circ \varphi_{12}$ is given by $t \mapsto 2t$, so it is not $\varphi_{11} = \id$, and clause 3 fails for $i = k = 1$, $j = 2$.
