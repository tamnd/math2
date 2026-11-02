---
tag: TYXD1T6FRX
kind: example
name: Kepler problem
msc: [70F05, 70H05]
instance_of: [0EDKGA2FAK]
uses: [0262JP0NV9, 00HJCMC2CD, 0RBKKNH4GV, 0VKCCEXBJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Kepler_problem
---

## Example

Let $k > 0$.
The Kepler problem is the system
$$r'' = -\frac{k\, r}{\norm{r}^3}$$
for a position $r(t) \in \R^3 \setminus \set{0}$, with velocity $v = r'$.
It describes a body attracted to a fixed centre by an inverse-square force, such as a planet around the Sun.
It is the [[Hamiltonian system|0EDKGA2FAK]] with $H(r, v) = \frac{1}{2} \norm{v}^2 - \frac{k}{\norm{r}}$.

Three quantities are [[first integrals|0262JP0NV9]]:

1. the energy $E = \frac{1}{2} \norm{v}^2 - k / \norm{r}$;
2. the angular momentum $L = r \times v$;
3. the Laplace–Runge–Lenz vector $A = v \times L - k\, r / \norm{r}$.

Check for $L$: $L' = v \times v + r \times r'' = 0 - \frac{k}{\norm{r}^3}\, r \times r = 0$.

## Remarks

Since $L$ is constant, a motion with $L \ne 0$ stays in the plane through the origin orthogonal to $L$.
In polar coordinates in that plane, with $\theta$ measured from the direction of $A$, the orbit is
$$\norm{r} = \frac{\norm{L}^2 / k}{1 + e \cos \theta}, \qquad e = \norm{A} / k.$$
So the orbit is a [[conic section|00HJCMC2CD]] with a [[focus|0RBKKNH4GV]] at the origin and eccentricity $e$.
It is an [[ellipse|0VKCCEXBJ1]] when $E < 0$, a parabola when $E = 0$, and a branch of a hyperbola when $E > 0$.
For an ellipse with semi-major axis $a$, the period $T$ satisfies $T^2 = 4 \pi^2 a^3 / k$, which is Kepler's third law.

## Explanations

### L1 human

The Kepler problem asks how a body moves when it is pulled toward a fixed point with a force that falls off like the square of the distance.
The answer is that it moves on an ellipse, a parabola or a hyperbola, with the centre of force at a focus.
This explains Kepler's laws of planetary motion from Newton's law of gravitation.
