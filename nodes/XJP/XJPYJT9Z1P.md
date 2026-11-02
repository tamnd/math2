---
tag: XJPYJT9Z1P
kind: object
name: Eilenberg–MacLane spectrum
msc: [55P42, 55P20]
instance_of: [1GHF4EKBXS]
uses: [1GHF4EKBXS, AJHEYJE5XY, 071DDFVG4J, 6N7BC70CX0, 26GTNMAF7B]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg%E2%80%93MacLane_spectrum
same_as:
  wikidata: Q134310487
  wikipedia: Eilenberg–MacLane spectrum
---

## Description

Let $G$ be an [[abelian group|071DDFVG4J]].
The Eilenberg–MacLane spectrum $HG$ is the [[spectrum|1GHF4EKBXS]] with $(HG)_n = K(G, n)$, an [[Eilenberg–MacLane space|AJHEYJE5XY]], for $n \ge 0$.
Its structure maps $\Sigma K(G, n) \to K(G, n+1)$ are adjoint to weak homotopy equivalences $K(G, n) \to \Omega K(G, n+1)$, so $HG$ is an $\Omega$-spectrum.
Its homotopy groups are $\pi_0(HG) = G$ and $\pi_k(HG) = 0$ for $k \neq 0$, and these properties determine $HG$ up to isomorphism in the [[stable homotopy category|26GTNMAF7B]].

## Remarks

The spectrum $HG$ represents ordinary [[singular cohomology|6N7BC70CX0]] with coefficients in $G$: for a CW complex $X$ and $n \ge 0$, $\tilde H^n(X; G) \cong [\Sigma^\infty X, \Sigma^n HG]$.
It also represents homology: $\tilde H_n(X; G) \cong \pi_n(HG \wedge X)$.
For $p$ prime, the graded ring $[H\F_p, \Sigma^* H\F_p]$ of stable self-maps is the mod $p$ Steenrod algebra.
If $R$ is a commutative ring, the product of $R$ makes $HR$ a commutative ring spectrum.

## Explanations

### L1 human

The Eilenberg–MacLane spectrum of a group $G$ is the simplest spectrum with homotopy $G$: it has $G$ in degree zero and nothing else.
It is the stable object behind ordinary cohomology with coefficients in $G$.
Comparing other spectra with it is how one connects generalized cohomology theories with ordinary cohomology.
