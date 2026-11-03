---
tag: JGCQX7ESVE
kind: definition
name: Spherical transform
msc: ["43A90", "43A32", "22E30"]
defines: E06PG40SVD
uses: [W38ZDXDVYC, BKZNC76RC8, VY0HXD3GC4]
sources:
  - url: https://en.wikipedia.org/wiki/Zonal_spherical_function
---

## Definition

Let $(G, K)$ be a [[Gelfand pair|W38ZDXDVYC]], with $G$ a locally compact group, $K$ a compact subgroup and $dg$ a [[Haar measure|VY0HXD3GC4]] on $G$.
Let $L^1(K \backslash G / K)$ be the space of integrable functions $f$ on $G$ with $f(k_1 g k_2) = f(g)$ for all $k_1, k_2 \in K$.
Let $\Phi$ be the set of bounded [[spherical functions|BKZNC76RC8]] of $(G, K)$.
The *spherical transform* of $f \in L^1(K \backslash G / K)$ is the function $\hat f \colon \Phi \to \C$ given by
$$\hat f(\varphi) = \int_G f(g) \, \varphi(g^{-1}) \, dg.$$

## Remarks

For a convolution $f_1 * f_2$ of two such functions, $\widehat{f_1 * f_2} = \hat f_1 \hat f_2$, and each map $f \mapsto \hat f(\varphi)$ is a character of the algebra $L^1(K \backslash G / K)$.
Every nonzero character of this algebra arises in this way from exactly one $\varphi \in \Phi$, so the spherical transform is the Gelfand transform of the algebra.

For a connected noncompact semisimple Lie group $G$ with finite centre and maximal compact subgroup $K$, the spherical functions are the $\varphi_\lambda$ of [[Harish-Chandra's formula|A6MQCW28KZ]], and $\varphi_\lambda(g^{-1}) = \varphi_{-\lambda}(g)$.
In this case one writes $\hat f(\lambda) = \int_G f(g) \varphi_{-\lambda}(g) \, dg$ for $\lambda \in \mathfrak a^*_\C$, a $W$-invariant function of $\lambda$.

Example: for $G = \R$ and $K = \set{0}$, the bounded spherical functions are $x \mapsto e^{i \xi x}$ with $\xi \in \R$, and $\hat f(\xi) = \int_\R f(x) e^{-i \xi x} \, dx$ is the Fourier transform.

Non-example: for the same $(G, K)$, the function $x \mapsto e^{x}$ is a spherical function, but it is unbounded, so it is not in $\Phi$.
Indeed the integral $\int_\R f(x) e^{-x} \, dx$ need not converge for $f \in L^1(\R)$.
