---
tag: J6X53EPYR5
kind: example
name: Stefan problem as a variational inequality
msc: [35R35, "80A22", 35K86]
illustrates: [3B0HB3DHW1, 6QS7X5GVMY]
uses: [3B0HB3DHW1, 6QS7X5GVMY, GXN2NEHC8X]
sources:
  - url: https://en.wikipedia.org/wiki/Stefan_problem
---

## Example

Take the one-dimensional one-phase [[Stefan problem|3B0HB3DHW1]] in units with thermal diffusivity and conductivity equal to $1$ and latent heat $L > 0$.
The liquid occupies $0 < x < s(t)$, with $s(0) = 0$ and $s$ increasing.
The end $x = 0$ is heated, with a given temperature $u(0, t) > 0$, and the temperature $u$ satisfies:
$$\partial_t u = \partial_x^2 u \ \text{ for } 0 < x < s(t), \qquad u(s(t), t) = 0, \qquad L s'(t) = -\partial_x u(s(t), t).$$
Extend $u$ by $0$ to the solid region $x > s(t)$, and define the integrated temperature
$$w(x, t) = \int_0^t u(x, \tau) \, d\tau.$$
Then $w$ solves the obstacle-type system
$$w \ge 0, \qquad \partial_t w - \partial_x^2 w + L \ge 0, \qquad w \, \big(\partial_t w - \partial_x^2 w + L\big) = 0.$$

Check in the liquid: fix $x > 0$ and let $\theta(x)$ be the time with $s(\theta(x)) = x$, so $u(x, \tau) = 0$ for $\tau \le \theta(x)$.
Then $w(x, t) = \int_{\theta(x)}^t u(x, \tau) \, d\tau$ for $t > \theta(x)$.
Differentiating twice in $x$ and using $u(x, \theta(x)) = 0$ gives $\partial_x^2 w = \int_{\theta(x)}^t \partial_x^2 u \, d\tau - \partial_x u(x, \theta(x)) \, \theta'(x)$.
The Stefan condition and $s'(\theta(x)) \, \theta'(x) = 1$ give $-\partial_x u(x, \theta(x)) \, \theta'(x) = L$.
The heat equation turns the integral into $u(x, t) = \partial_t w$, so $\partial_t w - \partial_x^2 w = -L$ where $w > 0$.
In the solid, $w = 0$, so $\partial_t w - \partial_x^2 w + L = L > 0$.

## Remarks

For each time $t$, the system is equivalent to a [[variational inequality|6QS7X5GVMY]] over the convex set $K = \set{v \ge 0}$:
$$\int \big(\partial_t w - \partial_x^2 w + L\big) (v - w) \, dx \ge 0 \quad \text{for all } v \in K.$$
Indeed, where $w > 0$ the first factor vanishes, and where $w = 0$ both factors are nonnegative.
So the free boundary $x = s(t)$ becomes the boundary of the set $\set{w > 0}$, as in the [[obstacle problem|GXN2NEHC8X]], and it no longer appears explicitly among the unknowns.
This change of unknown is due to Georges Duvaut, and it allows existence and regularity results for the Stefan problem through the theory of variational inequalities.

## Explanations

### L1 human

In a melting problem, the moving boundary between ice and water is unknown, which makes the equations hard to handle.
The trick is to add up the temperature over time at each place.
The new function is zero where the ice has not melted yet and positive in the water.
It solves a problem of the same type as a membrane pressed against an obstacle, where the contact set is found as part of the solution.
