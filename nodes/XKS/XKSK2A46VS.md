---
tag: XKSK2A46VS
kind: example
name: Potential flow around a circular cylinder
msc: [76G25, 76B99]
instance_of: [84K7TEWZ2Z]
uses: [Q4DVPTBHEE, E66111XRRA, 7XFWQVWPG1, BTHH4Y71QR, TY2JZPPKVB]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_flow_around_a_circular_cylinder
same_as:
  wikidata: Q7234818
  wikipedia: Potential flow around a circular cylinder
---

## Example

Consider a two-dimensional, steady, incompressible and irrotational flow of an inviscid fluid of density $\rho$ outside the disc $\abs{z} \le a$ in the plane $z = x + iy$.
Far from the disc the flow tends to the uniform stream of speed $U > 0$ in the $x$-direction.
The [[complex potential|Q4DVPTBHEE]] of this [[potential flow|84K7TEWZ2Z]] is
$$w(z) = U\left(z + \frac{a^2}{z}\right), \qquad \abs{z} \ge a.$$
In polar coordinates $z = r e^{i\theta}$ the [[stream function|E66111XRRA]] is $\psi = \operatorname{Im} w = U\left(r - \frac{a^2}{r}\right)\sin\theta$.
It vanishes on $r = a$, so the circle is a streamline and no fluid crosses it.
The complex velocity is $w'(z) = U(1 - a^2/z^2)$, which tends to $U$ as $\abs{z} \to \infty$.
On the circle the speed is $\abs{w'(a e^{i\theta})} = 2U\abs{\sin\theta}$.
So there are stagnation points at $\theta = 0$ and $\theta = \pi$, and the speed reaches its maximum $2U$ at the top and bottom.

## Remarks

The potential is the result of the [[Milne-Thomson circle theorem|TY2JZPPKVB]] applied to the uniform stream $f(z) = Uz$.
By [[Bernoulli's principle|7XFWQVWPG1]], the pressure on the circle is $p = p_\infty + \tfrac{1}{2}\rho U^2 (1 - 4\sin^2\theta)$, where $p_\infty$ is the pressure far away.
This pressure is symmetric under $\theta \mapsto \pi - \theta$, so the front and the back of the cylinder feel the same push and the drag is zero.
It is also symmetric under $\theta \mapsto -\theta$, so the lift is zero.
Adding a point vortex gives the family $w(z) = U(z + a^2/z) - \frac{i\Gamma}{2\pi}\log z$, where $\Gamma$ is the counterclockwise [[circulation|BTHH4Y71QR]] around the cylinder.
For this flow the force per unit length on the cylinder is $(0, -\rho U \Gamma)$, as the Kutta–Joukowski theorem predicts.

## Explanations

### L1 human

This is the simplest model of a stream flowing past a round post.
The fluid splits at the front, speeds up to twice the stream speed at the sides, and joins again at the back.
The picture is perfectly symmetric front to back, so the model predicts no drag, which is not what happens in a real fluid.
Spinning the cylinder adds a swirl and makes the flow faster on one side than the other, and this produces a sideways force.
