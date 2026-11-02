---
tag: WP4YAHJ6V4
kind: statement
role: theorem
name: Penrose–Hawking singularity theorems
msc: ["83C75", "53C50"]
uses: [BY4QYYS788, NSYMQMHPDN, 4GTNM0WHDH]
about: [BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Penrose%E2%80%93Hawking_singularity_theorems
same_as:
  wikidata: Q1452678
  wikipedia: Penrose–Hawking singularity theorems
---

## Statement

A spacetime here is a connected, time-oriented, four-dimensional [[Lorentzian manifold|BY4QYYS788]] $(M, g)$ of signature $(-, +, +, +)$.
It is timelike (resp. null) geodesically complete if every inextendible timelike (resp. null) [[geodesic|NSYMQMHPDN]] is defined for all values of its affine parameter.
A closed trapped surface is a compact spacelike surface without boundary in $M$.
On it, both families of future-directed null geodesics orthogonal to it must have negative expansion.
Let $\operatorname{Ric}$ be the [[Ricci curvature|4GTNM0WHDH]] of $g$.

1. (Hawking) Assume that $(M, g)$ is globally hyperbolic and that $\operatorname{Ric}(V, V) \ge 0$ for all timelike vectors $V$.
Let $\Sigma$ be a smooth spacelike Cauchy surface in $M$.
Let $\theta$ be the expansion on $\Sigma$ of the past-directed normal geodesics, that is, the mean curvature for the past-directed unit normal.
Assume that $\theta \le C$ on $\Sigma$ for a constant $C < 0$.
Then every past-directed timelike curve starting on $\Sigma$ has length at most $3/\abs{C}$.
In particular, $(M, g)$ is not timelike geodesically complete.
2. (Penrose) Assume that $(M, g)$ is globally hyperbolic with a noncompact Cauchy surface.
Assume that $\operatorname{Ric}(K, K) \ge 0$ for all null vectors $K$, and that $M$ contains a closed trapped surface.
Then $(M, g)$ is not null geodesically complete.
3. (Hawking and Penrose) Assume that $\operatorname{Ric}(V, V) \ge 0$ for all timelike and null vectors $V$.
Assume that $M$ has no closed timelike curves, and that every timelike or null geodesic satisfies the generic condition.
Assume also that at least one of the conditions (a), (b), (c) below holds.
(a) $M$ contains a compact achronal set without edge.
(b) $M$ contains a closed trapped surface.
(c) There is a point $p$ such that the null geodesics from $p$ all start to reconverge.
This means that the expansion of the future-directed null geodesics from $p$ becomes negative along each of them.
The same with past-directed geodesics also suffices.
Then $(M, g)$ contains an incomplete timelike or null geodesic.

## Remarks

The common core of the proofs is the Raychaudhuri equation.
By it, the curvature conditions force the expansion of a congruence of geodesics to become $-\infty$ in finite affine parameter, which creates conjugate or focal points.
Such points prevent geodesics from maximizing length beyond them.
On the other hand, global causal assumptions, such as global hyperbolicity, guarantee the existence of maximizing geodesics.
The two facts together show that some geodesic cannot be extended.
The Schwarzschild black hole contains closed trapped surfaces inside its horizon, and the theorem of Penrose shows that the singularity there persists under perturbations that keep a trapped surface.
The theorems prove incompleteness of geodesics; they do not say that the curvature becomes infinite.

## Explanations

### L1 human

These theorems say that, under reasonable physical conditions, general relativity predicts singularities.
Gravity attracts, so light rays and free-falling particles that start to converge keep converging.
Once matter collapses far enough to form a trapped surface, or the whole universe is expanding uniformly, some paths of particles or light must end after a finite time.
This is how the theory predicts black holes and a Big Bang.

### L2 human

The curvature conditions are energy conditions on matter, translated through the Einstein equations into inequalities on the Ricci curvature.
The proofs use the comparison theory of geodesics, much like the proof of Myers's theorem in Riemannian geometry, where positive Ricci curvature bounds the length of minimizing geodesics.
Penrose's theorem dates from 1965, and the joint theorem of Hawking and Penrose from 1970.
The third theorem trades global hyperbolicity for the weaker chronology condition, at the cost of the generic condition.
