---
tag: DHYS1W3Y4N
kind: definition
name: Group algebra of a locally compact group
msc: ["22D15", "43A20"]
defines: 6GD25S53ND
uses: [AHV05ZBCYW, VY0HXD3GC4, 63TX60RTRQ, 2Z29JN3VES, SASP14MA1Z, 9KYWN94QDN]
sources:
  - url: https://en.wikipedia.org/wiki/Group_algebra_of_a_locally_compact_group
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]] $\mu$ and [[modular function|63TX60RTRQ]] $\Delta$.
The *group algebra* of $G$ is the space [[$L^1(G) = L^1(G, \mu)$|SASP14MA1Z]] of integrable functions, with the following operations.

1. The product is [[convolution|2Z29JN3VES]]: $(f * h)(x) = \int_G f(y) \, h(y^{-1}x) \, d\mu(y)$.
2. The involution is $f^*(x) = \Delta(x^{-1}) \, \overline{f(x^{-1})}$.
3. The norm is $\norm{f}_1 = \int_G \abs{f} \, d\mu$.

## Remarks

With these operations $L^1(G)$ is a [[Banach algebra|9KYWN94QDN]] with an isometric involution, that is, a Banach $*$-algebra: $\norm{f * h}_1 \le \norm{f}_1 \norm{h}_1$, $(f * h)^* = h^* * f^*$ and $\norm{f^*}_1 = \norm{f}_1$.

Example: $G = \Z$ with counting measure.
Then $L^1(\Z) = \ell^1(\Z)$, $\Delta \equiv 1$, the product is $(f * h)(n) = \sum_m f(m) h(n - m)$ and $f^*(n) = \overline{f(-n)}$.
The sequence $\delta_0$ is a unit: $(\delta_0 * h)(n) = h(n)$.
Here $\ell^1(\Z)$ contains the [[group algebra|MNP2HBWB5Q]] $\C[\Z]$ of finitely supported sequences as a dense subalgebra.

Non-example of a unit: $L^1(\R)$ has no unit.
If $e * f = f$ for all $f \in L^1(\R)$, then taking Fourier transforms gives $\hat e = 1$ wherever some $\hat f$ is nonzero, so $\hat e \equiv 1$, which contradicts the Riemann–Lebesgue lemma $\hat e(\xi) \to 0$.
In general $L^1(G)$ has a unit exactly when $G$ is discrete, but it always has a bounded approximate unit.

$L^1(G)$ is commutative if and only if $G$ is abelian.
