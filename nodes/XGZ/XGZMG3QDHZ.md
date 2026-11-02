---
tag: XGZMG3QDHZ
kind: definition
name: Kähler manifold
msc: [32Q15, 53C55]
defines: X60JG9AEQJ
uses: [JSGWAN2RJV, CK1DCPC3D3, 48P4A1CX85, 0E3G0GRPZ6, 0ZV14XRNF0]
sources:
  - url: https://en.wikipedia.org/wiki/K%C3%A4hler_manifold
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of dimension $n$.
Let $h$ be a Hermitian metric on $X$: a smooth family of positive definite [[Hermitian forms|48P4A1CX85]] $h_p$ on the holomorphic tangent spaces $T^{1,0}_p X$.
In local holomorphic coordinates write $h = \sum_{j,k} h_{j\bar k}\, dz_j \otimes d\bar z_k$, where $(h_{j\bar k})$ is a positive definite Hermitian matrix of smooth functions.
The *fundamental form* of $h$ is the real $(1,1)$-[[form|0E3G0GRPZ6]]
$$\omega = \frac{i}{2} \sum_{j,k} h_{j\bar k}\, dz_j \wedge d\bar z_k.$$
The metric $h$ is *Kähler* if $\omega$ is [[closed|0ZV14XRNF0]], that is, $d\omega = 0$.
A *Kähler manifold* is a complex manifold together with a Kähler metric; $\omega$ is then called its Kähler form.

## Remarks

In coordinates, $d\omega = 0$ holds if and only if $\dfrac{\partial h_{j\bar k}}{\partial z_l} = \dfrac{\partial h_{l\bar k}}{\partial z_j}$ for all $j, k, l$.
Equivalent forms: locally $\omega = i\partial\bar\partial\varphi$ for a real smooth strictly plurisubharmonic function $\varphi$; or the complex structure is parallel for the Levi-Civita connection of the underlying Riemannian metric $\operatorname{Re} h$.
A compact complex manifold is called Kähler if it admits some Kähler metric.

Example: on $\C^n$, $h_{j\bar k} = \delta_{jk}$ gives $\omega = \frac{i}{2}\sum_j dz_j \wedge d\bar z_j$, which has constant coefficients and so is closed.
On a Riemann surface every Hermitian metric is Kähler, because every $3$-form on a manifold of real dimension $2$ is zero.
The Fubini–Study form on $\mathbb{CP}^n$, given on $\set{z_0 \ne 0}$ by $\omega = \frac{i}{2}\partial\bar\partial \log(1 + \abs{w}^2)$ in the coordinates $w_j = z_j/z_0$, is closed because $d = \partial + \bar\partial$ and $\partial^2 = \bar\partial^2 = 0$, $\partial\bar\partial = -\bar\partial\partial$.

Non-example: on $W = \C^2 \setminus \set{0}$, the form $\omega = \frac{i}{2}\abs{z}^{-2}\sum_j dz_j \wedge d\bar z_j$ is the fundamental form of a Hermitian metric invariant under $z \mapsto \lambda z$, so it descends to a [[Hopf surface|PNFNGBXRM3]].
It is not closed: $d\omega = d(\abs{z}^{-2}) \wedge \omega_0$ with $\omega_0 = \frac{i}{2}\sum_j dz_j \wedge d\bar z_j$, and the wedge product of a nonzero $1$-form with $\omega_0$ is nonzero in complex dimension $2$.
So this metric is a [[Hermitian metric|CK1DCPC3D3]] that is not Kähler; in fact the Hopf surface has no Kähler metric at all.
