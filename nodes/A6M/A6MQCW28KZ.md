---
tag: A6MQCW28KZ
kind: statement
role: theorem
name: Harish-Chandra's formula for spherical functions
msc: ["43A90", "22E46", "22E30"]
uses: [XJS07AJ50Y, T2EB8R9HEV, 4YDR9Q36DS, VY0HXD3GC4, BKZNC76RC8, W38ZDXDVYC]
about: [BKZNC76RC8]
sources:
  - url: https://en.wikipedia.org/wiki/Zonal_spherical_function
---

## Statement

Let $G$ be a connected noncompact [[semisimple Lie group|XJS07AJ50Y]] with finite centre and let $K$ be a [[maximal compact subgroup|T2EB8R9HEV]].
Let $G = K A N$ be an [[Iwasawa decomposition|4YDR9Q36DS]], let $\mathfrak a$ be the Lie algebra of $A$, and for $g \in G$ let $H(g) \in \mathfrak a$ be defined by $g \in K \exp(H(g)) N$.
Let $\rho \in \mathfrak a^*$ be half the sum of the positive restricted roots, counted with multiplicity.
Let $W$ be the Weyl group of the restricted roots, acting on the complex dual $\mathfrak a^*_\C$.
Let $dk$ be the [[Haar measure|VY0HXD3GC4]] of $K$ of total mass $1$.
For $\lambda \in \mathfrak a^*_\C$ define
$$\varphi_\lambda(g) = \int_K e^{(i \lambda - \rho)(H(g k))} \, dk, \qquad g \in G.$$

1. Each $\varphi_\lambda$ is a [[spherical function|BKZNC76RC8]] for the [[Gelfand pair|W38ZDXDVYC]] $(G, K)$.
2. Every spherical function for $(G, K)$ is equal to $\varphi_\lambda$ for some $\lambda \in \mathfrak a^*_\C$.
3. $\varphi_\lambda = \varphi_\mu$ if and only if $\mu = w \lambda$ for some $w \in W$.

## Remarks

The function $g \mapsto e^{(i \lambda - \rho)(H(g))}$ is left $K$-invariant and transforms by a character under right translation by $A N$.
Averaging its right translates over $K$ gives a bi-$K$-invariant function, and the functional equation $\int_K \varphi(x k y) \, dk = \varphi(x) \varphi(y)$ is checked with the Iwasawa decomposition.
For the converse one shows that spherical functions are joint eigenfunctions of the invariant differential operators on $G / K$, and Harish-Chandra's homomorphism identifies the possible eigenvalues with $W$-orbits in $\mathfrak a^*_\C$.

Examples: $\varphi_{-i\rho} = 1$, since then $i \lambda - \rho = 0$.
The function $\Xi = \varphi_0$ is Harish-Chandra's $\Xi$-function, used to define [[Harish-Chandra's Schwartz space|JCDV4FZ86G]].
The bounded spherical functions are the $\varphi_\lambda$ with $\operatorname{Im} \lambda$ in the convex hull of $W \rho$, and the positive definite ones include all $\varphi_\lambda$ with $\lambda \in \mathfrak a^*$ real.

## Explanations

### L1 human

Spherical functions are the basic building blocks of analysis on a symmetric space such as the hyperbolic plane.
Harish-Chandra's formula gives all of them at once, as averages over the compact group $K$ of simple exponential functions.
The parameter $\lambda$ plays the role of a frequency.

### L2 human

The formula is the starting point of the [[spherical transform|E06PG40SVD]] $\hat f(\lambda) = \int_G f(g) \varphi_{-\lambda}(g) \, dg$ on $G / K$.
The asymptotic behaviour of $\varphi_\lambda$ at infinity is governed by the [[Harish-Chandra c-function|4X2N0BN3M0]].
For $G = \mathrm{SL}(2, \R)$ the functions $\varphi_\lambda$ are Legendre functions of $\cosh$ of the hyperbolic distance.
