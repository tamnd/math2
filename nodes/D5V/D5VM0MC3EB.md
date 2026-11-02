---
tag: D5VM0MC3EB
kind: statement
role: theorem
name: De Giorgi's structure theorem
msc: [49Q15, 28A75, 26B30]
uses: [W6R7QNEAF1, Y68BHXZJBV, HZNEQQBCW4, Q1TGZK8RN6, 7N0GFMW05R]
about: [W6R7QNEAF1]
sources:
  - url: https://en.wikipedia.org/wiki/Caccioppoli_set
---

## Statement

Let $n \ge 2$ and let $E \subseteq \R^n$ be a set of locally finite [[perimeter|Y68BHXZJBV]], that is, a local [[Caccioppoli set|W6R7QNEAF1]].
Let $\mu = \abs{D\chi_E}$ be the total variation measure of the distributional gradient of its indicator function $\chi_E$, a [[Radon measure|HZNEQQBCW4]].
Write $D\chi_E = -\nu_E \, \mu$ with a Borel map $\nu_E \colon \R^n \to \R^n$ such that $\abs{\nu_E} = 1$ $\mu$-almost everywhere.
For $x \in \R^n$ and $r > 0$ let $B_r(x)$ be the open ball of radius $r$ about $x$.
Consider the limit
$$\lim_{r \to 0} \frac{D\chi_E(B_r(x))}{\mu(B_r(x))}.$$
The *reduced boundary* $\partial^* E$ is the set of points $x$ in the support of $\mu$ at which this limit exists and has norm $1$.
Let $\mathcal{H}^{n-1}$ be the $(n-1)$-dimensional [[Hausdorff measure|Q1TGZK8RN6]].
Then:

1. The set $\partial^* E$ is countably $(n-1)$-[[rectifiable|7N0GFMW05R]]: up to an $\mathcal{H}^{n-1}$-null set, it is contained in a countable union of $C^1$ hypersurfaces.
2. $\mu = \mathcal{H}^{n-1} \llcorner \partial^* E$, that is, $\mu(A) = \mathcal{H}^{n-1}(A \cap \partial^* E)$ for every Borel set $A$.
3. For every $x \in \partial^* E$, the rescaled sets $(E - x)/r$ converge in $L^1_{\mathrm{loc}}(\R^n)$, as $r \to 0$, to the half-space $\set{y : y \cdot \nu_E(x) < 0}$.
4. For every $\varphi \in C^1_c(\R^n; \R^n)$, the generalized Gauss–Green formula holds:
$$\int_E \operatorname{div} \varphi \, dx = \int_{\partial^* E} \varphi \cdot \nu_E \, d\mathcal{H}^{n-1}.$$

## Remarks

The proof starts from the Besicovitch differentiation theorem, which shows that $\mu$-almost every point lies in $\partial^* E$.
At a point of $\partial^* E$, the isoperimetric inequality gives density estimates comparing $\mu(B_r(x))$ with $r^{n-1}$.
With the compactness of sets of finite perimeter, a blow-up argument then shows that the rescaled sets converge to a half-space.
The half-space limit identifies $\mu$ with $\mathcal{H}^{n-1}$ on $\partial^* E$.
Rectifiability then follows from the existence of approximate tangent planes at all points of $\partial^* E$.
For a bounded open set with $C^1$ boundary, $\partial^* E = \partial E$, $\nu_E$ is the outer unit normal, and item 4 is the classical divergence theorem.
For the square $[0, 1]^2$, the reduced boundary is the boundary minus the four corners; the corners form an $\mathcal{H}^1$-null set.
The topological boundary can be much larger than $\partial^* E$, even of positive Lebesgue measure, so the reduced boundary is the right notion of boundary here.

## Explanations

### L1 human

A set of finite perimeter can have a very rough boundary.
The theorem says that the part of the boundary that matters is still made of pieces of smooth surfaces, with a well-defined outward direction at almost every point.
Zooming in at such a point, the set looks more and more like half of space.
With this boundary, the usual formula relating the flux through the boundary to the integral of the divergence still holds.

### L2 human

The theorem is due to Ennio De Giorgi, and it is the foundation of the theory of sets of finite perimeter.
It turns a set known only through the measure $D\chi_E$ into a geometric object with a measure-theoretic normal.
Federer later showed that $\partial^* E$ coincides, up to an $\mathcal{H}^{n-1}$-null set, with the essential boundary, the set of points where $E$ has density neither $0$ nor $1$.
These results are the starting point of the regularity theory of perimeter minimizers and of the study of free discontinuity problems.
