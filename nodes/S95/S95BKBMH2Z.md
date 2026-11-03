---
tag: S95BKBMH2Z
kind: statement
role: proposition
name: Vis-viva equation
msc: [70F05, 70M20]
uses: [BXFSBB8Q46, AV2WRWW1TN, DJGG5SN382]
about: [BXFSBB8Q46]
sources:
  - url: https://en.wikipedia.org/wiki/Vis-viva_equation
same_as:
  wikidata: Q1142411
  wikipedia: Vis-viva equation
---

## Statement

Let $\mu > 0$ and let $r(t)$ move on an elliptic [[Kepler orbit|BXFSBB8Q46]] with gravitational parameter $\mu$ and semi-major axis $a > 0$.
Let $v = \norm{r'}$ be the speed and $\rho = \norm{r}$ the distance to the attracting centre.
Then at every time
$$v^2 = \mu \left( \frac{2}{\rho} - \frac{1}{a} \right).$$

## Remarks

The specific energy $E = \frac{1}{2} v^2 - \mu / \rho$ is constant along the orbit, by [[conservation of energy|AV2WRWW1TN]].
At periapsis and apoapsis the velocity is orthogonal to $r$, and the distances are $a(1 - e)$ and $a(1 + e)$.
Using the conservation of $\norm{r \times r'}$ at these two points and solving gives $E = -\mu / (2a)$, which is the equation.
For a hyperbolic orbit the same formula holds with $a < 0$, and for a parabolic orbit with $1/a = 0$.
Example: on a circular orbit, $\rho = a$, so $v = \sqrt{\mu / a}$.
Letting $a \to \infty$ gives $v = \sqrt{2 \mu / \rho}$, the [[escape velocity|DJGG5SN382]].

## Explanations

### L1 human

The speed of a body on an orbit depends only on how far it is from the centre and on the size of the orbit.
Closer in, it moves faster; on a bigger orbit, it moves faster at the same distance.
This lets one compute speeds on orbits without solving any differential equation.

### L2 human

The vis-viva equation is the working tool for manoeuvre planning.
For a tangential burn, the change of speed needed to go from one orbit to another at a given point is the difference of two vis-viva speeds.
The Hohmann and bi-elliptic transfers are computed this way.
It also shows that the energy of a Kepler orbit depends only on $a$, which, together with Kepler's third law, gives the period $2\pi \sqrt{a^3 / \mu}$ from the energy.
