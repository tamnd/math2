---
tag: ZZP31F3VPK
kind: definition
name: Étale cohomology
msc: [14F20]
defines: 7YX76G0838
uses: [5A35TYZD02, H84VHC8PX2, NYE0Z94MME, RT8A8FJ566, NPMC3K6J2F, EESNTXFWHZ]
sources:
  - url: https://en.wikipedia.org/wiki/%C3%89tale_cohomology
---

## Definition

Let $X$ be a [[scheme|5A35TYZD02]].
The *small étale site* $X_{\text{ét}}$ is the [[site|NYE0Z94MME]] defined as follows.

1. Its objects are the [[étale morphisms|H84VHC8PX2]] $U \to X$.
2. Its morphisms are the morphisms $U \to V$ over $X$.
3. A family $\set{U_i \to U}$ is a covering when the union of the images of the $U_i$ is $U$.

An *étale sheaf* on $X$ is a [[sheaf on the site|RT8A8FJ566]] $X_{\text{ét}}$.
The category of étale sheaves of abelian groups on $X$ has enough injectives.
For such a sheaf $F$, the *étale cohomology groups* $H^i_{\text{ét}}(X, F)$, for $i \ge 0$, are the right [[derived functors|NPMC3K6J2F]] of the global section functor $F \mapsto F(X)$.

## Remarks

Example: let $X = \operatorname{Spec} k$ for a field $k$ with separable closure $k^{s}$ and Galois group $G = \Gal(k^{s}/k)$.
Étale $X$-schemes are disjoint unions of spectra of finite separable extensions of $k$.
An étale sheaf $F$ is then the same as the discrete $G$-module $M = \varinjlim F(\operatorname{Spec} k')$ over finite subextensions $k'$.
The global sections are $M^G$, so $H^i_{\text{ét}}(X, F) = H^i(G, M)$ is [[Galois cohomology|EESNTXFWHZ]].
Non-example: if the étale morphisms in clause 1 are replaced by open immersions, one gets the Zariski site.
For an irreducible $X$ and a constant sheaf $A$, every constant sheaf is flasque in the Zariski topology, so $H^i(X, A) = 0$ for all $i > 0$.
Étale cohomology does not have this defect: for a smooth projective curve of genus $g$ over an algebraically closed field and $n$ prime to the characteristic, $H^1_{\text{ét}}(X, \Z/n\Z) \cong (\Z/n\Z)^{2g}$.
