---
tag: KCVJ91K4WD
kind: definition
name: Exact solutions in general relativity
msc: ["83C15", "83C20", "83C05"]
defines: H7PS83YCER
uses: [D1SYF8F8RQ, 7C2WP33E10, REDZ92MKXX, ENWD1YR20P]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_solutions_in_general_relativity
---

## Definition

Fix a matter model: a list of matter fields on a 4-manifold, together with their field equations.
The model also gives their [[stress–energy tensor|REDZ92MKXX]] $T$ in terms of the fields and the metric.
An *exact solution* of general relativity for this model is a 4-dimensional [[Lorentzian manifold|D1SYF8F8RQ]] $(M, g)$ with matter fields on $M$ such that:

1. $g$ and $T$ satisfy the [[Einstein field equations|7C2WP33E10]] $G_{ab} + \Lambda g_{ab} = 8\pi T_{ab}$, for a fixed constant $\Lambda$;
2. the matter fields satisfy their own field equations on $(M, g)$.

## Remarks

Example: the Schwarzschild metric $g = -(1 - 2M/r) dt^2 + (1 - 2M/r)^{-1} dr^2 + r^2 d\Omega^2$ on $r > 2M$ is an exact solution with no matter and $\Lambda = 0$, since its Ricci tensor is zero.
Another example is the Reissner–Nordström metric with a Coulomb electromagnetic field, which solves the Einstein–Maxwell equations.
Non-example: a gravitational plane wave of linearised gravity solves the linearised equations, but in general not the full Einstein equations, so it is an approximate solution only.
Without a matter model the notion is empty: any metric solves the equations with $T$ defined as $(G + \Lambda g)/8\pi$.
For this reason one also asks that $T$ be physically reasonable, for instance that it satisfies the [[energy conditions|ENWD1YR20P]].

## Explanations

### L1 human

An exact solution is a spacetime and its matter that satisfy Einstein's equations exactly, with the matter obeying its own laws.
