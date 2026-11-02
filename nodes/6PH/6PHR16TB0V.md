---
tag: 6PHR16TB0V
kind: definition
name: Banach bundle
msc: [58B99, 57R22, 46T05]
defines: F4RH4MZQDG
uses: [VB95VVVDM8, 0BDTTM24DP, 0ZTEH055YF, 0QT00PB5G2, 0S3SMRH0Z5]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_bundle
---

## Definition

Let $M$ be a [[Banach manifold|VB95VVVDM8]] of class $C^p$, with $p \ge 0$.
Let $E$ be a topological space and $\pi \colon E \to M$ a continuous surjection, and assume each fibre $E_x = \pi^{-1}(x)$ carries the structure of a real [[Banach space|0BDTTM24DP]].
For Banach spaces $X$ and $Y$, let $\mathcal{L}(X; Y)$ be the Banach space of [[bounded linear maps|0S3SMRH0Z5]] with the [[operator norm|0ZTEH055YF]].
The map $\pi$ is a *Banach bundle* of class $C^p$ if there are data of the following kind.
There are an open cover $(U_i)_{i \in I}$ of $M$, Banach spaces $X_i$ and maps $\tau_i \colon \pi^{-1}(U_i) \to U_i \times X_i$ such that:


1. Each $\tau_i$ is a [[homeomorphism|0QT00PB5G2]] with $\mathrm{pr}_{U_i} \circ \tau_i = \pi$.
2. For each $x \in U_i$, the induced map $\tau_{i,x} \colon E_x \to X_i$ is a continuous linear isomorphism.
3. For all $i, j \in I$, the map $U_i \cap U_j \to \mathcal{L}(X_i; X_j)$, $x \mapsto \tau_{j,x} \circ \tau_{i,x}^{-1}$, is of class $C^p$.

## Remarks

Example: for a Banach manifold $M$ and a Banach space $X$, the product $M \times X \to M$ with the single trivialisation $\tau = \id$ is a Banach bundle; the transition map is constant.
The tangent bundle of a $C^{p+1}$ Banach manifold is a Banach bundle of class $C^p$, with transition maps given by derivatives of chart changes.

Non-example: clause 3 asks for continuity in the operator norm, not only pointwise.
On $X = L^2(\R)$ let $T_s f(t) = f(t - s)$ be the translation by $s$.
Then $s \mapsto T_s f$ is continuous for each $f$, but $\norm{T_s - T_{s'}} = 2$ for $s \ne s'$.
So gluing two trivial bundles $(-\infty, 1) \times X$ and $(0, \infty) \times X$ over $M = \R$ by $x \mapsto T_{1/x}$ on $(0, 1)$ violates clause 3.

When all $X_i$ are finite-dimensional, this is the notion of a vector bundle of class $C^p$.
