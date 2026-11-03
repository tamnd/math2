---
tag: PJ4V6A4XX8
kind: definition
name: Hydrodynamic stability
msc: ["76E99", "76E05"]
defines: H028A17Z55
uses: [18KXZHVF4M, 0F2SYCKDT2, DF0M8YNQ3D]
sources:
  - url: https://en.wikipedia.org/wiki/Hydrodynamic_stability
---

## Definition

Let $\Omega \subseteq \R^3$ be a bounded open set with smooth boundary, and let $\nu > 0$.
Let $U \colon \Omega \to \R^3$ be a steady solution, the *basic flow*, of the [[Navier–Stokes equations|18KXZHVF4M]] with given steady boundary values and forcing.
Let $u_0$ be a smooth divergence-free initial velocity with the same boundary values as $U$.
Let $u(t)$ be the smooth solution with these boundary values, the same forcing and $u(0) = u_0$, as long as it exists.
The basic flow $U$ is *stable* (in the energy norm) if for every $\varepsilon > 0$ there is $\delta > 0$ such that

1. every such $u_0$ with $\norm{u_0 - U}_{L^2} < \delta$ gives a solution $u(t)$ that exists for all $t \ge 0$, and
2. $\norm{u(t) - U}_{L^2} < \varepsilon$ for all $t \ge 0$.

It is *asymptotically stable* if, in addition, $\norm{u(t) - U}_{L^2} \to 0$ as $t \to \infty$ for all such $u_0$, and *unstable* if it is not stable.

## Remarks

This is [[Lyapunov stability|0F2SYCKDT2]] of the equilibrium $U$ of the Navier–Stokes evolution.

Example: the rest state $U = 0$ with zero forcing and the [[no-slip condition|DF0M8YNQ3D]] is asymptotically stable.
For a smooth solution, $\frac{d}{dt} \norm{u}_{L^2}^2 = -2 \nu \norm{\nabla u}_{L^2}^2 \le -2 \nu \lambda_1 \norm{u}_{L^2}^2$ by the Poincaré inequality with its constant $\lambda_1 > 0$, so $\norm{u(t)}_{L^2} \le e^{-\nu \lambda_1 t} \norm{u_0}_{L^2}$.

Non-example: take circular Couette flow with the outer cylinder at rest and the inner one rotating fast enough.
Here the cylinders are infinitely long and disturbances are taken periodic in the axial direction, so the domain is a periodic gap rather than a bounded set.
It is unstable: a small disturbance grows into Taylor vortices, so clause 2 fails for small $\varepsilon$.

*Linear stability* replaces the equations by their linearisation at $U$ and asks that no eigenvalue of the linearised operator has positive real part.
The energy method gives sufficient conditions for nonlinear stability, and linear analysis gives sufficient conditions for instability.
Both depend on the norm and on the class of disturbances, which must be stated.
