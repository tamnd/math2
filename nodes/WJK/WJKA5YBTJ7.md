---
tag: WJKA5YBTJ7
kind: statement
role: theorem
name: Calabi conjecture
msc: [32Q25, 53C55, 32Q20]
uses: [CK1DCPC3D3, 4GTNM0WHDH, 6ETEBA8827, 0ZV14XRNF0]
about: [CK1DCPC3D3, 4GTNM0WHDH]
sources:
  - url: https://en.wikipedia.org/wiki/Calabi_conjecture
same_as:
  wikidata: Q5018293
  wikipedia: Calabi conjecture
---

## Statement

Let $M$ be a compact complex manifold of complex dimension $n$ with a Kähler metric $g$, whose fundamental form is $\omega$; see [[Hermitian manifold|CK1DCPC3D3]].
Let $c_1(M)$ be the first Chern class of $M$ in real de Rham cohomology.
Let $\rho'$ be a real closed $(1,1)$-form on $M$ whose [[de Rham class|0ZV14XRNF0]] is $2\pi c_1(M)$.
Then there is a unique Kähler form $\omega'$ on $M$ in the same cohomology class as $\omega$ whose Ricci form is $\rho'$.

## Remarks

Calabi proved uniqueness, and Yau proved existence; the result is often called the Calabi–Yau theorem.
Write $\omega' = \omega + i\partial\bar\partial\varphi$ for a real function $\varphi$, by the $\partial\bar\partial$-lemma.
Since the Ricci form is $-i\partial\bar\partial \log$ of the volume density, the problem becomes the complex Monge–Ampère equation
$$(\omega + i\partial\bar\partial\varphi)^n = e^{F} \omega^n,$$
for a given function $F$ normalized so that $\int_M e^F \omega^n = \int_M \omega^n$.
Yau solved it by the continuity method, and the key step is an a priori bound on $\sup \abs{\varphi}$.

The main application is the case $c_1(M) = 0$ in real cohomology.
Take $\rho' = 0$: each Kähler class then contains a unique Ricci-flat Kähler metric.
Such manifolds are the Calabi–Yau manifolds, for example K3 surfaces and quintic threefolds in $\C P^4$.
The same method gives [[Kähler–Einstein metrics|6ETEBA8827]] with negative constant when $c_1(M) < 0$, a result of Aubin and Yau.

## Explanations

### L1 human

The curvature of a Kähler metric is tied to the topology of the manifold through the first Chern class.
Calabi asked whether every curvature form allowed by this topology is actually the Ricci curvature of some Kähler metric.
Yau proved that the answer is yes, and that the metric is unique once its Kähler class is fixed.

### L2 human

The theorem is a statement about a fully nonlinear elliptic equation, and its proof was a landmark of geometric analysis.
Its best-known consequence is the existence of Ricci-flat metrics on compact Kähler manifolds with vanishing first Chern class.
These metrics have restricted holonomy in $SU(n)$ and are used in string theory and in mirror symmetry.
The positive case $c_1(M) > 0$ is not covered and is the subject of the [[Yau–Tian–Donaldson conjecture|DHYSPSYSCB]].
