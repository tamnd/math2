---
tag: Q134D9EMAZ
kind: statement
role: theorem
name: Shilnikov theorem
msc: [37G20, 34C37, 37C29]
uses: [6DBSQKZK4W, 01TPMXM6NM, 0BQAA2BK3Q, 0AA97XA70K, N63Z6EA6YS, JQYCTY3Q8V]
about: [6DBSQKZK4W, JQYCTY3Q8V]
sources:
  - url: https://en.wikipedia.org/wiki/Homoclinic_orbit
---

## Statement

Let $\dot x = F(x)$ be a smooth vector field on $\R^3$.
Let $x_0$ be a [[hyperbolic equilibrium|01TPMXM6NM]] whose Jacobian matrix $DF(x_0)$ has [[eigenvalues|0BQAA2BK3Q]] $\lambda > 0$ and $-\rho \pm i \omega$ with $\rho > 0$ and $\omega \ne 0$.
Let $\Gamma$ be a [[homoclinic orbit|6DBSQKZK4W]] to $x_0$.
Assume the Shilnikov condition $\rho < \lambda$.
Then every neighbourhood of $\Gamma \cup \set{x_0}$ contains infinitely many [[periodic orbits|0AA97XA70K]] of saddle type.

## Remarks

Such an equilibrium is called a saddle-focus: orbits near it spiral in along a plane and leave along a line.
The proof studies the return map to a small section transverse to $\Gamma$.
Near $x_0$ the flow is close to linear, and the passage time near the equilibrium makes the returning image a spiral that winds infinitely often.
When $\rho < \lambda$ this spiral is stretched rather than contracted, and it crosses the section so as to form infinitely many [[Smale horseshoes|N63Z6EA6YS]].
Each horseshoe carries infinitely many periodic orbits, which gives the conclusion.
The condition $\rho < \lambda$ is needed: if $\rho > \lambda$, a sufficiently small neighbourhood of $\Gamma$ contains at most one periodic orbit.
The theorem is due to Leonid Shilnikov.

## Explanations

### L1 human

Imagine a flow in space with a point that pulls nearby orbits inward along a spiralling disc and pushes them out along a line.
If an orbit leaves along the line and comes back spiralling into the point, the theorem says that complicated behaviour is forced near this loop.
When the push outwards is stronger than the pull inwards, infinitely many closed orbits appear near the loop.
This is a simple test for chaos that can be checked from the eigenvalues at one point.

### L2 human

The theorem is a main source of chaos in three-dimensional flows, because it reduces chaos to the existence of a single homoclinic orbit plus an inequality on eigenvalues.
A [[homoclinic bifurcation|JQYCTY3Q8V]] to a saddle-focus that satisfies the Shilnikov condition is therefore a route to chaos in families of flows.
In the plane, by contrast, the breaking of a homoclinic loop creates at most one limit cycle.
