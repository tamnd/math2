---
tag: QW17YJ6ZCT
kind: definition
name: Galois representation
msc: [11F80, 11R34, 11S37]
defines: JQEYEQJY2G
uses: [0XTY86BZKY, WYGRXCG2RN, 0JYTG5K9Y4, 0FCHE902D7, 0X3WGX95FE, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_representation
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] with separable closure $K^{\mathrm{sep}}$, and let $G_K = \Gal(K^{\mathrm{sep}}/K)$ be its absolute [[Galois group|0XTY86BZKY]] with the Krull topology, a profinite group.
Let $A$ be a topological commutative ring and let $n \ge 1$.
Typical choices of $A$ are $\C$, a finite field, $\Z_\ell$, or a finite extension of $\Q_\ell$.
Give the [[general linear group|0FCHE902D7]] $\mathrm{GL}_n(A)$ the topology induced from $A^{n^2}$.
A *Galois representation* of $K$ of dimension $n$ over $A$ is a [[continuous|0X3WGX95FE]] [[group homomorphism|0JYTG5K9Y4]] $\rho \colon G_K \to \mathrm{GL}_n(A)$.

## Remarks

Equivalently, it is a continuous action of $G_K$ on a free $A$-module of rank $n$, by $A$-linear maps.
Two representations are isomorphic if they are conjugate by a matrix of $\mathrm{GL}_n(A)$.

Example: let $\ell$ be a prime different from the characteristic of $K$.
The $\ell$-adic cyclotomic character $\chi_\ell \colon G_K \to \Z_\ell^\times = \mathrm{GL}_1(\Z_\ell)$ is given by $\sigma(\zeta) = \zeta^{\chi_\ell(\sigma) \bmod \ell^k}$.
This holds for all $k$ and every root of unity $\zeta$ of order dividing $\ell^k$.
It is a homomorphism, and it is continuous because its reduction modulo $\ell^k$ factors through the finite quotient $\Gal(K(\mu_{\ell^k})/K)$.
Another example: the Tate module $T_\ell(E) = \varprojlim E[\ell^k]$ of an elliptic curve $E$ over $K$ gives a $2$-dimensional representation over $\Z_\ell$.

Non-example: the constant map $G_K \to \mathrm{GL}_n(A)$ with value $-I$, for $A$ of characteristic not $2$, is continuous but sends the identity to $-I \ne I$, so it is not a homomorphism.

With $A = \C$ and its usual topology, every continuous representation has finite image; these are the Artin representations.
For $K$ a number field, a Galois representation is unramified at a finite place $v$ if it is trivial on the inertia group at $v$.
Then the image of a Frobenius element at $v$ is defined up to conjugacy.
