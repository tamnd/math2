---
tag: Y3R22D3SZY
kind: definition
name: Helgason Fourier transform
msc: ["43A85", "43A90", "22E30"]
defines: K533EAPKKY
uses: [XJS07AJ50Y, T2EB8R9HEV, 4YDR9Q36DS, PAA93R4WYD, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_theorem_for_spherical_functions
---

## Definition

Let $G$ be a connected noncompact [[semisimple Lie group|XJS07AJ50Y]] with finite centre, and $K$ a [[maximal compact subgroup|T2EB8R9HEV]].
Let $X = G / K$ be the associated Riemannian [[symmetric space|PAA93R4WYD]], with $G$-invariant measure $dx$.
Let $G = N A K$ be an [[Iwasawa decomposition|4YDR9Q36DS]], with $\mathfrak a$ the Lie algebra of $A$, and for $g \in G$ let $A(g) \in \mathfrak a$ be defined by $g \in N \exp(A(g)) K$.
Let $M$ be the centralizer of $A$ in $K$, and let $B = K / M$.
Let $\rho$ be half the sum of the positive restricted roots, counted with multiplicity.
For $x = g K \in X$ and $b = k M \in B$ put $A(x, b) = A(k^{-1} g)$.
The *Helgason Fourier transform* of a [[smooth|0V33BNKZ9S]] function $f$ with compact support on $X$ is the function on $\mathfrak a^*_\C \times B$ given by
$$\tilde f(\lambda, b) = \int_X f(x) \, e^{(-i \lambda + \rho)(A(x, b))} \, dx.$$

## Remarks

The quantity $A(x, b)$ is well defined: replacing $g$ by $g k'$ with $k' \in K$, or $k$ by $k m$ with $m \in M$, does not change $A(k^{-1} g)$, because $M$ normalizes $N$ and commutes with $A$.
Geometrically, $A(x, b)$ is a vector-valued signed distance from the origin to the horocycle through $x$ with normal $b$.

If $f$ is bi-$K$-invariant, that is, radial on $X$, then $\tilde f(\lambda, b)$ does not depend on $b$ and equals the [[spherical transform|E06PG40SVD]] $\hat f(\lambda)$, by Harish-Chandra's integral formula for spherical functions.
With suitable normalizations of the measures, the inversion formula is
$$f(x) = \frac{1}{\abs{W}} \int_{\mathfrak a^*} \int_B \tilde f(\lambda, b) \, e^{(i \lambda + \rho)(A(x, b))} \, \abs{c(\lambda)}^{-2} \, d\lambda \, db,$$
where $W$ is the Weyl group and $c$ the [[Harish-Chandra c-function|4X2N0BN3M0]].

Example: for $\mathrm{SL}(2, \R)$ acting on the upper half plane $\set{z : \operatorname{Im} z > 0}$, $B$ is the boundary circle.
For the boundary point $b = \infty$, the function $e^{\rho(A(z, b))}$ is a power of $\operatorname{Im} z$, constant on the horocycles $\operatorname{Im} z = \text{const}$.

