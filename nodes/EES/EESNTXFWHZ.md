---
tag: EESNTXFWHZ
kind: definition
name: Galois cohomology
msc: [12G05, 20J06, 11R34]
defines: 9MPCZ3EAJM
uses: [JJ91A1V8NQ, PGKWBJDTKX, KA0YDB6QXE, 071DDFVG4J, 0YSE802YCQ]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_cohomology
---

## Definition

Let $K$ be a field, $K^s$ a [[separable closure|JJ91A1V8NQ]] of $K$, and $G_K = \Gal(K^s/K)$ the [[absolute Galois group|PGKWBJDTKX]] with its Krull topology, a [[profinite group|KA0YDB6QXE]].
A *discrete $G_K$-module* is an [[abelian group|071DDFVG4J]] $M$ with a [[group action|0YSE802YCQ]] of $G_K$ by group automorphisms.
The stabilizer of each $m \in M$ must be an open subgroup of $G_K$.

For $n \ge 0$, let $C^n(G_K, M)$ be the group of continuous maps $G_K^n \to M$, where $M$ has the discrete topology and $C^0(G_K, M) = M$.
Define $d \colon C^n(G_K, M) \to C^{n+1}(G_K, M)$ by
$$(d\varphi)(g_1, \ldots, g_{n+1}) = g_1 \varphi(g_2, \ldots, g_{n+1}) + \sum_{i=1}^{n} (-1)^i \varphi(g_1, \ldots, g_i g_{i+1}, \ldots, g_{n+1}) + (-1)^{n+1} \varphi(g_1, \ldots, g_n).$$
Then $d \circ d = 0$.
The *Galois cohomology groups* of $K$ with coefficients in $M$ are
$$H^n(K, M) = H^n(G_K, M) = \ker\big(d \colon C^n \to C^{n+1}\big) / \im\big(d \colon C^{n-1} \to C^n\big),$$
with $C^{-1} = 0$.

## Remarks

The group $H^0(K, M)$ is the group $M^{G_K}$ of fixed elements.
The group $H^n(K, M)$ is also the direct limit, over finite Galois extensions $L/K$ inside $K^s$, of the group cohomology groups $H^n(\Gal(L/K), M^{\Gal(K^s/L)})$.
Example: $M = (K^s)^\times$ is a discrete $G_K$-module, since each element of $K^s$ lies in a finite extension of $K$, and its stabilizer contains the open subgroup fixing that extension.
For it, $H^0(K, (K^s)^\times) = K^\times$, $H^1(K, (K^s)^\times) = 0$ by [[Hilbert's Theorem 90|YFF8B5A0QG]], and $H^2(K, (K^s)^\times)$ is the [[Brauer group|BEW48TA9WZ]] of $K$.
For an integer $m$ not divisible by the characteristic of $K$, with $\mu_m$ the group of $m$-th roots of unity in $K^s$, [[Kummer theory|XZQENYV15Y]] gives $H^1(K, \mu_m) \cong K^\times / (K^\times)^m$.
Non-example: let $\ell$ be a prime and $\Z_\ell(1)$ the inverse limit of the groups $\mu_{\ell^n}$ in $\overline{\Q}$, with $G_\Q$ acting on each $\mu_{\ell^n}$.
With the discrete topology, $\Z_\ell(1)$ is not a discrete $G_\Q$-module.
The stabilizer of a generator is the subgroup fixing all $\ell$-power roots of unity.
It is closed but not open, because the field of all $\ell$-power roots of unity has infinite degree over $\Q$.
For such modules one uses continuous cochains for the $\ell$-adic topology instead.
