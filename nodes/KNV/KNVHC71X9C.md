---
tag: KNVHC71X9C
kind: example
name: Alcubierre metric
msc: [83C15, 83C99]
instance_of: [BY4QYYS788]
illustrates: [ENWD1YR20P]
uses: [3MCZ97SW6V, G49G4R1K04]
sources:
  - url: https://en.wikipedia.org/wiki/Alcubierre_drive
same_as:
  wikidata: Q169890
  wikipedia: Alcubierre drive
---

## Example

Use units where the gravitational constant and the speed of light equal $1$.
Let $x_s \colon \R \to \R$ be a smooth function, the path of the bubble centre, with velocity $v_s = x_s'$.
Let $f \colon [0, \infty) \to [0, 1]$ be a smooth function with $f(s) = 1$ for small $s$ and $f(s) = 0$ for large $s$.
Set $r_s = \sqrt{(x - x_s(t))^2 + y^2 + z^2}$.
On $\R^4$ with coordinates $(t, x, y, z)$, the *Alcubierre metric* is
$$g = -dt^2 + \left(dx - v_s(t) f(r_s)\, dt\right)^2 + dy^2 + dz^2.$$

Check of the main features:
where $f(r_s) = 0$, far from the bubble, $g$ is the flat [[Minkowski|G49G4R1K04]] metric.
Where $f(r_s) = 1$, inside the bubble, $g = -dt^2 + (dx - v_s\, dt)^2 + dy^2 + dz^2$, which is flat Minkowski space in coordinates moving with velocity $v_s$.
The world line $x = x_s(t)$, $y = z = 0$ of the bubble centre has tangent $\partial_t + v_s\partial_x$, and $g(\partial_t + v_s\partial_x, \partial_t + v_s\partial_x) = -1$.
So it is a timelike curve parametrized by proper time, and one checks that it is a geodesic.
No condition limits $v_s$, so the bubble may move faster than light relative to the distant flat region.
Yet the observer inside never moves faster than light locally.

The metric is defined first, and the matter is read off from the [[Einstein field equations|3MCZ97SW6V]].
Consider the observers with $4$-velocity $n = \partial_t + v_s f\, \partial_x$, normal to the slices $t = \text{const}$.
The energy density they measure is
$$T_{ab} n^a n^b = -\frac{1}{8\pi}\, \frac{v_s^2\left(y^2 + z^2\right)}{4 r_s^2} \left(f'(r_s)\right)^2 \le 0,$$
and it is strictly negative where $f' \ne 0$ off the axis.
So the weak [[energy condition|ENWD1YR20P]] fails in the wall of the bubble.

## Explanations

### L1 human

Miguel Alcubierre proposed this spacetime in 1994 as a model of a warp drive.
A bubble of flat spacetime is carried along by contracting space in front of it and expanding space behind it.
A ship inside the bubble floats freely and feels no acceleration, yet the bubble can travel faster than light as seen from far away.
The catch is that the wall of the bubble needs negative energy density, which ordinary matter does not have.
