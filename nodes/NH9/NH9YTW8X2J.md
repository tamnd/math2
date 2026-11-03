---
tag: NH9YTW8X2J
kind: definition
name: Dynamo theory
msc: [76W05, 86A25, 85A30]
defines: AFVDBT0K5C
uses: [T8JWCBK9M6, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamo_theory
---

## Definition

Let $V \subset \R^3$ be a bounded region with smooth boundary, filled with a fluid of constant magnetic diffusivity $\eta > 0$.
Let the exterior $\R^3 \setminus \overline{V}$ be an electrical insulator.
Let $\mathbf{u}$ be a given smooth velocity field on $V$, tangent to $\partial V$.
The *kinematic dynamo problem* is the problem for a magnetic field $\mathbf{B}(x, t)$ on $\R^3$ such that:

1. in $V$, $\partial_t \mathbf{B} = \nabla \times (\mathbf{u} \times \mathbf{B}) + \eta \Delta \mathbf{B}$;
2. outside $V$, $\nabla \times \mathbf{B} = 0$, and $\mathbf{B}(x) = O(\abs{x}^{-3})$ as $\abs{x} \to \infty$;
3. $\nabla \cdot \mathbf{B} = 0$ everywhere, and $\mathbf{B}$ is continuous across $\partial V$.

The flow $\mathbf{u}$ is a *kinematic dynamo* if some solution has magnetic energy $\int_{\R^3} \abs{\mathbf{B}}^2 \, dx$ that does not tend to $0$ as $t \to \infty$.
*Dynamo theory* is the study of this problem and of its nonlinear version.
In the nonlinear version, $\mathbf{u}$ solves the momentum equation of [[magnetohydrodynamics|T8JWCBK9M6]] with the Lorentz force.

## Remarks

Non-example: $\mathbf{u} = 0$ is not a dynamo; then $\mathbf{B}$ solves a diffusion problem, and its energy decays exponentially.
A flow must be fast enough compared with diffusion: the magnetic Reynolds number $\mathrm{Rm} = U L / \eta$ must exceed a threshold that depends on the shape of the flow.
Examples: Herzenberg and Backus gave the first rigorous examples of kinematic dynamos in 1958.
Later simple examples include the Ponomarenko dynamo, a helical flow in a cylinder, and the G. O. Roberts dynamo, a spatially periodic flow.
For steady $\mathbf{u}$, the problem is an eigenvalue problem $\mathbf{B} = e^{\lambda t} \mathbf{B}_0(x)$, and $\mathbf{u}$ is a dynamo when some eigenvalue has $\operatorname{Re} \lambda \ge 0$.
