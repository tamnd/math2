---
tag: PMRGCQTFZC
kind: definition
name: Crossed product algebra
msc: [16S35, 16K50]
defines: G21MZQCME9
uses: [0QMZAQ6QQ4, 0XTY86BZKY, 5HRKJBAY2V, 9MPCZ3EAJM]
sources:
  - url: https://en.wikipedia.org/wiki/Crossed_product
---

## Definition

Let $L/K$ be a finite [[Galois extension|0QMZAQ6QQ4]] with [[Galois group|0XTY86BZKY]] $G$ and degree $n = [L : K]$.
A *factor set* (or $2$-cocycle) is a map $f \colon G \times G \to L^\times$ such that
$$f(\sigma, \tau) \, f(\sigma\tau, \rho) = \sigma\big(f(\tau, \rho)\big) \, f(\sigma, \tau\rho) \quad \text{for all } \sigma, \tau, \rho \in G.$$
The *crossed product algebra* $(L/K, f)$ is the $L$-vector space with basis $\set{u_\sigma : \sigma \in G}$, with the multiplication determined by
$$u_\sigma \, x = \sigma(x) \, u_\sigma \quad (x \in L), \qquad u_\sigma \, u_\tau = f(\sigma, \tau) \, u_{\sigma\tau}.$$

## Remarks

The cocycle condition is exactly what makes the multiplication associative.
The algebra $(L/K, f)$ is a [[central simple algebra|5HRKJBAY2V]] over $K$ of degree $n$, it contains $L$ as a maximal subfield, and $L$ splits it.
Two factor sets give isomorphic algebras if and only if they differ by a coboundary, so the classes correspond to $H^2(G, L^\times)$ in [[Galois cohomology|9MPCZ3EAJM]].
This gives $\mathrm{Br}(L/K) \cong H^2(G, L^\times)$.

Example: take $L = \C$, $K = \R$, $G = \set{1, \sigma}$ with $\sigma$ complex conjugation, and $f(\sigma, \sigma) = -1$, $f = 1$ otherwise.
With $j = u_\sigma$ one gets $j z = \bar{z} j$ and $j^2 = -1$, which are the relations of $\mathbb{H} = \C + \C j$.
With $f(\sigma, \sigma) = 1$ instead one gets an algebra isomorphic to $M_2(\R)$.

Non-example: for $L = \C$, $K = \R$ as above, the map with $f(\sigma, \sigma) = i$ and $f = 1$ otherwise is not a factor set.
The condition for $\sigma, \sigma, \sigma$ would give $i = \sigma(i) = -i$, and indeed $(u_\sigma u_\sigma) u_\sigma = i u_\sigma$ while $u_\sigma (u_\sigma u_\sigma) = \sigma(i) u_\sigma = -i u_\sigma$, so the product is not associative.

A central simple algebra is called a crossed product if it is isomorphic to some $(L/K, f)$; Amitsur showed that some central division algebras are not crossed products.
