---
tag: 9PV9CN8X0Y
kind: example
name: Harmonic function on a ball
msc: [31B05, 31B10]
instance_of: [EYMQ82Z8XJ]
uses: [TCYSWCTYYM, 0E0B6RA8K0, 0YE5868HZB]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_kernel
---

## Example

Let $n \ge 2$, let $B = \set{x \in \R^n : \abs{x} < 1}$ be the unit [[open ball|0YE5868HZB]], and fix a point $\zeta$ with $\abs{\zeta} = 1$.
Consider the function
$$u(x) = \frac{1 - \abs{x}^2}{\abs{x - \zeta}^n}, \qquad x \in B,$$
which is the [[Poisson kernel|TCYSWCTYYM]] of the ball with pole $\zeta$, up to a constant factor.
It is positive on $B$, because $\abs{x} < 1$ and $x \ne \zeta$.
To check that it is harmonic, write $f(x) = 1 - \abs{x}^2$, $g(x) = \abs{x - \zeta}^{-n}$ and $r = \abs{x - \zeta}$.
Then $\Delta f = -2n$, $\nabla f = -2x$, $\nabla g = -n r^{-n-2} (x - \zeta)$ and $\Delta g = 2n r^{-n-2}$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
The product rule $\Delta(fg) = f \Delta g + 2 \nabla f \cdot \nabla g + g \Delta f$ gives
$$\Delta u = 2n r^{-n-2} \left( 1 - \abs{x}^2 + 2 x \cdot (x - \zeta) - r^2 \right).$$
Since $r^2 = \abs{x}^2 - 2 x \cdot \zeta + 1$, the bracket equals $0$, so $\Delta u = 0$.

## Remarks

As $x$ tends to a boundary point $\eta \ne \zeta$, the numerator tends to $0$ and the denominator stays away from $0$, so $u(x) \to 0$.
As $x \to \zeta$ along the radius, $u(t\zeta) = (1 + t)/(1 - t)^{n-1}$ tends to $+\infty$.
So $u$ is a positive harmonic function on the ball that vanishes on the whole boundary sphere except at one point.

## Explanations

### L1 human

This function is the steady temperature in a ball when all the heat enters through one point $\zeta$ of the surface.
It is zero near the rest of the surface and blows up at $\zeta$.
Every positive harmonic function on the ball is an average of such functions with different poles.
