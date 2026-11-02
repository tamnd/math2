---
tag: VF43FTDA1H
kind: example
name: Geodesic flow
msc: [37D40, 53D25]
instance_of: [116TPXR5FS]
uses: [NSYMQMHPDN, 5HDG31YEPW, DQB1BVQJWD, 1X42JAA349]
sources:
  - url: https://en.wikipedia.org/wiki/Geodesic
---

## Example

Let $M$ be a complete [[Riemannian manifold|5HDG31YEPW]] with [[tangent bundle|DQB1BVQJWD]] $TM$.
Let $SM$ be its unit tangent bundle, the set of tangent vectors of length $1$.
For $v \in SM$ let $\gamma_v$ be the [[geodesic|NSYMQMHPDN]] with $\gamma_v(0)$ the base point of $v$ and $\gamma_v'(0) = v$.
The geodesic flow is $\varphi_t(v) = \gamma_v'(t)$ for $t \in \R$.
It is defined for all $t$ because $M$ is complete, and $\varphi_{s+t} = \varphi_s \circ \varphi_t$ because $t \mapsto \gamma_v(s + t)$ is the geodesic with initial vector $\gamma_v'(s)$.
So it is a [[smooth dynamical system|116TPXR5FS]] in continuous time on $SM$.

Check on the flat torus $M = \R^2/\Z^2$: geodesics are straight lines, so $SM = M \times S^1$ and $\varphi_t(x, v) = (x + t v, v)$.
For a direction $v$ of irrational slope, the orbit of $(x, v)$ is dense in the torus $M \times \set{v}$.
For a direction of rational slope, every orbit is periodic.

## Remarks

The geodesic flow preserves the Liouville measure on $SM$, the product of the Riemannian volume and the uniform measure on each unit sphere.
If $M$ is compact and its [[sectional curvature|1X42JAA349]] is negative everywhere, the geodesic flow is an [[Anosov flow|8FQJXSA4DT]], as Anosov proved, and it is ergodic for the Liouville measure.
For a surface of constant curvature $-1$ it can be written as a homogeneous flow, see [[geodesic flow on a locally symmetric space|5TKBSHY6VC]].
Identify $TM$ with the cotangent bundle $T^*M$ by the metric.
Then the geodesic flow is the Hamiltonian flow of the kinetic energy $H(v) = \frac12\norm{v}^2$, restricted to an energy level.

## Explanations

### L1 human

Put a frictionless marble on a curved surface and push it in some direction.
It rolls along the straightest possible path, a geodesic, at constant speed.
The geodesic flow records where the marble is and which way it moves after time $t$.
On a flat torus the motion is simple, but on a surface curved like a saddle everywhere, nearby paths diverge exponentially and the motion is chaotic.
