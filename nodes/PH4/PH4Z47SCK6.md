---
tag: PH4Z47SCK6
kind: statement
role: theorem
name: Christodoulou–Klainerman stability of Minkowski space
msc: [83C05, 35Q75, 35L70]
uses: [3MCZ97SW6V, BY4QYYS788, 92C3S03AQZ]
about: [3MCZ97SW6V]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_space
---

## Statement

Consider the Einstein vacuum equations $\operatorname{Ric}(g) = 0$ for a [[Lorentzian metric|BY4QYYS788]] $g$ on a $4$-dimensional manifold, the vacuum case of the [[Einstein field equations|3MCZ97SW6V]].
Let $(\Sigma, \bar g, k)$ be an initial data set for these equations, with $\Sigma$ diffeomorphic to $\R^3$.
Here $\bar g$ is a Riemannian metric on $\Sigma$, $k$ is a symmetric $2$-tensor on $\Sigma$, and the constraint equations hold.
Assume that the data are strongly asymptotically flat and maximal ($\operatorname{tr}_{\bar g} k = 0$).
Assume also that they are close enough to the data $(\R^3, \delta, 0)$ of Minkowski space in a suitable weighted Sobolev norm.
Then the maximal globally hyperbolic development of the data is a geodesically complete solution of the vacuum equations.
Moreover, it approaches Minkowski space in every direction as one goes to infinity, with precise decay rates for the curvature.

## Remarks

The result was proved by Demetrios Christodoulou and Sergiu Klainerman, and published as a monograph in 1993.
In a suitable gauge the vacuum equations form a system of nonlinear wave equations, so the theorem is a global existence result for small data of a [[hyperbolic|92C3S03AQZ]] system.
The nonlinearity is critical in three space dimensions.
For general quadratic nonlinearities small data can blow up in finite time, so global existence uses a special structure of the Einstein equations.
The proof uses a foliation of spacetime by maximal hypersurfaces and by null cones, and energy estimates for the Bel–Robinson tensor contracted with approximate symmetries of the solution.
Lindblad and Rodnianski later gave a different proof in harmonic (wave) gauge, under somewhat different assumptions on the data.

## Explanations

### L1 human

In general relativity, empty flat spacetime is the simplest solution of Einstein's equations.
The theorem says that this solution is stable: if one disturbs it a little, for instance by weak gravitational waves, the disturbance spreads out and dies away.
The spacetime does not collapse into a black hole or develop other singularities.
Far away and late in time it looks again like flat spacetime.

### L2 human

Proving stability means proving global existence and decay for a quasilinear hyperbolic system with small data.
Linear waves in three space dimensions decay like $t^{-1}$.
This is just barely too slow to control a general quadratic nonlinearity, as examples of John show for some nonlinear wave equations.
In harmonic gauge the Einstein equations do not satisfy the classical null condition of Klainerman, but their nonlinear terms still have enough structure to prevent blow-up.
The techniques of the proof, the vector field method and geometric energy estimates, became standard tools for nonlinear wave equations.
They are also used in later stability problems, such as the stability of black holes.
