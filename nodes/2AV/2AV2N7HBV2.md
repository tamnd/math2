---
tag: 2AV2N7HBV2
kind: statement
role: theorem
name: Blasius theorem
msc: [76G25, "30E20"]
uses: [Q4DVPTBHEE, 84K7TEWZ2Z, 7XFWQVWPG1, 06ZGPYTWK8]
about: [Q4DVPTBHEE]
sources:
  - url: https://en.wikipedia.org/wiki/Blasius_theorem
same_as:
  wikidata: Q881920
  wikipedia: Blasius theorem
---

## Statement

Consider a steady, two-dimensional, incompressible and irrotational flow of an inviscid fluid of constant density $\rho$ around a rigid body, with no body forces.
Identify the plane with $\C$ and let $C$ be the boundary curve of the body, oriented counterclockwise.
Let $w(z)$ be the [[complex potential|Q4DVPTBHEE]] of the flow.
Let $(F_x, F_y)$ be the force per unit length that the pressure of the fluid exerts on the body.
Let $M$ be the counterclockwise moment of this force about the origin.
Then
$$F_x - i F_y = \frac{i \rho}{2} \oint_C \left(\frac{dw}{dz}\right)^2 dz, \qquad M = \operatorname{Re}\left[-\frac{\rho}{2} \oint_C z \left(\frac{dw}{dz}\right)^2 dz\right].$$

## Remarks

The proof writes the force as the integral of $-p\,n$ over $C$ and replaces $p$ by $p_0 - \tfrac{1}{2}\rho\abs{w'}^2$ using [[Bernoulli's principle|7XFWQVWPG1]].
Since $C$ is a streamline, $dw = w'(z)\,dz$ is real along $C$, so $\overline{w'}\,d\bar z = w'\,dz$ there, and this turns $\abs{w'}^2 d\bar z$ into $(w')^2 dz$.
Because $(w')^2$ is holomorphic in the fluid, the [[contour integral|06ZGPYTWK8]] over $C$ can be replaced by one over any larger closed curve in the fluid, and then computed by residues.
For a uniform stream $U$ past a body with circulation $\Gamma$, the residue at infinity gives $F_x - iF_y = i\rho U \Gamma$, which is the Kutta–Joukowski theorem.

## Explanations

### L1 human

The force of a flowing fluid on an object comes from the pressure all around its surface.
The Blasius theorem turns this force into a single complex integral of the squared complex velocity.
That integral is often easy to compute with the tools of complex analysis.

### L2 human

The theorem is the bridge between [[potential flow|84K7TEWZ2Z]] in the plane and the forces on bodies.
Once the complex potential of a flow is known, for instance from a conformal map or the circle theorem, the lift and moment follow from a residue computation.
It gives a short proof of the Kutta–Joukowski lift formula and of d'Alembert's result that the drag vanishes in steady potential flow.
