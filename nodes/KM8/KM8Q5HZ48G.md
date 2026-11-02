---
tag: KM8Q5HZ48G
kind: statement
role: theorem
name: Douglas–Radó solution of Plateau's problem
msc: [49Q05, 53A10, "58E12"]
uses: [DVYA6GD8RN, 0DEB0JMN0W, 0YYT36R4YD, 41X0YW2R9N, M4CEZ5K9HP, 0HATW2VWAZ]
about: [DVYA6GD8RN]
sources:
  - url: https://en.wikipedia.org/wiki/Plateau%27s_problem
---

## Statement

Let $n \ge 2$ and let $\Gamma \subseteq \R^n$ be a [[rectifiable|0HATW2VWAZ]] Jordan curve, that is, a curve of finite length homeomorphic to a circle.
Let $D$ be the open unit disc in $\R^2$, with coordinates $(u, v)$, and let $\overline{D}$ be its closure.
Let $\mathcal{C}(\Gamma)$ be the set of continuous maps $Y \colon \overline{D} \to \R^n$ in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,2}(D; \R^n)$.
The restriction of each such $Y$ to $\partial D$ must be a monotone parametrization of $\Gamma$.
Then there is a map $X \in \mathcal{C}(\Gamma)$ such that:

1. $X$ restricted to $\partial D$ is a homeomorphism onto $\Gamma$;
2. $X$ is [[harmonic|0DEB0JMN0W]] in $D$;
3. $X$ is weakly [[conformal|0YYT36R4YD]] in $D$: $\abs{X_u}^2 = \abs{X_v}^2$ and $X_u \cdot X_v = 0$;
4. the area $\int_D \abs{X_u \wedge X_v} \, du \, dv$ of $X$ is the least area of all maps in $\mathcal{C}(\Gamma)$.

## Remarks

Jesse Douglas and Tibor Radó found the theorem independently, around 1930.
The idea is to minimize the Dirichlet energy $\frac12 \int_D (\abs{Y_u}^2 + \abs{Y_v}^2)$ instead of the area.
The energy is easier to control, and it is at least the area, with equality for conformal maps.
The energy is invariant under the conformal maps of the disc, so one fixes the images of three boundary points.
Then the Courant–Lebesgue lemma makes a minimizing sequence equicontinuous on the boundary, and a minimizer exists.
A minimizer of the energy is harmonic, and varying the parametrization of the disc shows that it is weakly conformal, so it also minimizes area.
Points where $X_u = 0$ are isolated branch points, and away from them the image is a [[minimal surface|41X0YW2R9N]].
For example, if $\Gamma$ is a planar circle, the solution parametrizes the flat disc that it bounds.
The theorem controls only disc-type surfaces: a curve may bound a surface of another topological type with smaller area.

## Explanations

### L1 human

A wire loop dipped in soapy water holds a film of least area.
Douglas and Radó proved that for every loop of finite length a least-area surface shaped like a disc exists.
Their surface is given by a parametrization that is both harmonic and angle-preserving.

### L2 human

The theorem answers [[Plateau's problem|DVYA6GD8RN]] for disc-type surfaces, and it is a model of the direct method of the calculus of variations.
The trick of replacing area by the Dirichlet energy reappears in the theory of harmonic maps and of minimal surfaces in Riemannian manifolds.
Later work studied the branch points: for area-minimizing solutions in $\R^3$ there are no interior branch points.
Geometric measure theory treats the problem in other dimensions and without fixing the topology, with currents and varifolds.
