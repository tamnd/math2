---
tag: 14CGGHA85T
kind: object
name: Sphere spectrum
msc: [55P42, 55Q45]
instance_of: [1GHF4EKBXS]
uses: [1GHF4EKBXS, HGZAYPQBXW, 26GTNMAF7B]
sources:
  - url: https://en.wikipedia.org/wiki/Sphere_spectrum
same_as:
  wikidata: Q7576683
  wikipedia: Sphere spectrum
---

## Description

The sphere spectrum $S$ is the [[spectrum|1GHF4EKBXS]] with $S_n = S^n$, the $n$-sphere, for $n \ge 0$, and with structure maps the canonical homeomorphisms $\Sigma S^n \cong S^{n+1}$.
It is the suspension spectrum $\Sigma^\infty S^0$ of the two-point space.
Its homotopy groups are the [[stable homotopy groups of spheres|HGZAYPQBXW]]:
$$\pi_k(S) = \operatorname{colim}_n \pi_{k+n}(S^n) = \pi_k^s.$$

## Remarks

One has $\pi_k(S) = 0$ for $k < 0$, $\pi_0(S) = \Z$, $\pi_1(S) = \Z/2$, $\pi_2(S) = \Z/2$ and $\pi_3(S) = \Z/24$.
For $k > 0$ every group $\pi_k(S)$ is finite, by Serre's finiteness theorem.
In the [[stable homotopy category|26GTNMAF7B]], $S$ is the unit for the smash product, and maps $S \to E$ of degree $k$ compute $\pi_k(E)$ for every spectrum $E$.
The multiplication $S^n \wedge S^m \cong S^{n+m}$ makes $S$ a commutative ring spectrum, and $\pi_*(S)$ is a graded commutative ring.

## Explanations

### L1 human

The sphere spectrum is the stable version of the two-point space $S^0$, or of the circle, the 2-sphere and all higher spheres at once.
It plays the role in stable homotopy theory that the integers play in algebra.
Its homotopy groups, the stable stems, are among the most studied and least understood objects in topology.
