---
tag: SXFTH721QT
kind: statement
role: theorem
name: Geodesic deviation equation
msc: [83C10, 53C22, 53C50]
uses: [RNRTS8WWNM, 5FZDQQHQKM, JA29ETCM02, 9AHMM41PJ3]
about: [RNRTS8WWNM, JA29ETCM02]
sources:
  - url: https://en.wikipedia.org/wiki/Geodesic_deviation
same_as:
  wikidata: Q1206762
  wikipedia: Geodesic deviation
---

## Statement

Let $(M, g)$ be a spacetime with Levi-Civita connection $\nabla$ and [[Riemann curvature tensor|JA29ETCM02]] $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$.
Let $\gamma \colon (-\varepsilon, \varepsilon) \times I \to M$, $(s, \tau) \mapsto \gamma(s, \tau)$, be a smooth map.
Assume that for each $s$ the curve $\tau \mapsto \gamma(s, \tau)$ is a timelike [[geodesic|RNRTS8WWNM]] parametrised by proper time.
Let $u = \partial_\tau \gamma$ be the tangent field and $J = \partial_s \gamma$ the deviation vector field, and write $D/d\tau$ for the [[covariant derivative|5FZDQQHQKM]] along the curves $\tau \mapsto \gamma(s, \tau)$.
Then
$$\frac{D^2 J}{d\tau^2} = -R(J, u)u.$$
In components, $\dfrac{D^2 J^\mu}{d\tau^2} = -R^\mu{}_{\nu\alpha\beta} \, u^\nu J^\alpha u^\beta$.

## Remarks

The proof uses that $\partial_s$ and $\partial_\tau$ commute, so $\frac{D}{d\tau} J = \frac{D}{ds} u$ because the connection is torsion-free.
Then $\frac{D^2}{d\tau^2} J = \frac{D}{d\tau}\frac{D}{ds} u = \frac{D}{ds}\frac{D}{d\tau} u + R(u, J) u$, and $\frac{D}{d\tau} u = 0$ since the curves are geodesics; finally $R(u, J) = -R(J, u)$.
So $J$ restricted to each geodesic is a [[Jacobi field|9AHMM41PJ3]], and the equation is the Jacobi equation in Lorentzian signature.
Example: in Minkowski space $R = 0$, so $D^2J/d\tau^2 = 0$, and nearby free particles separate at a constant rate.
In the Newtonian limit, with gravitational potential $\Phi$ and nearly static particles, $R^i{}_{0j0} \approx \partial_i \partial_j \Phi$, and the equation becomes $d^2 J^i/dt^2 = -\partial_i \partial_j \Phi \, J^j$, the Newtonian tidal acceleration.

## Explanations

### L1 human

Two stones dropped side by side towards the Earth slowly approach each other, because both fall towards the centre of the Earth.
Two stones dropped one above the other slowly drift apart, because the lower one is pulled a bit harder.
These tidal effects are what remains of gravity in a freely falling laboratory.
The geodesic deviation equation says that they are measured exactly by the curvature of spacetime.

### L2 human

The equation is how curvature becomes observable: the equivalence principle removes gravity at one point, but the relative acceleration of nearby free particles cannot be removed.
A gravitational wave passing through a ring of free test masses deforms it by this equation, which is the principle of interferometric detectors.
The trace of the curvature term, $R_{\mu\nu} u^\mu u^\nu$, is the term that appears in the Raychaudhuri equation for the expansion of a congruence of geodesics.
