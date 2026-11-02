---
tag: SSCJWAQ7AX
kind: definition
name: Seeley–DeWitt coefficients
msc: [58J35, 58J50, 81T20]
defines: R72NAFZ722
uses: [7CBT4SM83Y, P4DZM975BV, 5ZYRRVE8BW, 327NP6S7H5, 45P2SEGGR1, ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_kernel
---

## Definition

Let $(M, g)$ be a closed [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$ and let $E$ be a Hermitian [[vector bundle|P4DZM975BV]] over $M$.
Let $L$ be a Laplace-type operator on $E$, that is, a second-order operator with principal symbol $\abs{\xi}^2 \id_E$.
Equivalently, $L = \nabla^* \nabla + F$ for a unique [[connection|5ZYRRVE8BW]] $\nabla$ on $E$ and a unique endomorphism field $F$.
Let $K_L(t, x, y)$ be the [[heat kernel|327NP6S7H5]] of $L$.
There are unique smooth sections $a_k(L)$ of $\End(E)$, $k = 0, 1, 2, \ldots$, such that for every $N$
$$K_L(t, x, x) = (4\pi t)^{-n/2} \left( \sum_{k = 0}^{N} a_k(L)(x) \, t^k + O(t^{N+1}) \right) \quad \text{as } t \to 0^+,$$
uniformly in $x$.
The $a_k(L)$ are the *Seeley–DeWitt coefficients* of $L$.

## Remarks

Existence follows by the same parametrix construction as for the [[Minakshisundaram–Pleijel expansion|45P2SEGGR1]], and uniqueness from the uniqueness of asymptotic expansions.
The first two are $a_0 = \id_E$ and $a_1 = \tfrac16 S \, \id_E - F$, where $S$ is the [[scalar curvature|ZHX2VYQDZ3]].
Some authors call the integrated traces $\int_M \operatorname{tr} a_k(L) \, dv$ the heat invariants, and on manifolds with boundary there are also half-integer powers $t^{k/2}$.

Example: take the scalar Laplacian on a flat torus, so $F = 0$.
Its heat kernel on the diagonal is $(4\pi t)^{-n/2}$ times $1$ plus exponentially small terms, so $a_0 = 1$ and $a_k = 0$ for $k \ge 1$.

Non-example: a Dirac operator $D$ is of first order, so it is not Laplace-type and has no Seeley–DeWitt coefficients in this sense.
Its square $D^2$ is Laplace-type, and the coefficients of $D^2$ are the ones used in index theory.
