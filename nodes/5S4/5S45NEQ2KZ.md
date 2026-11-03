---
tag: 5S45NEQ2KZ
kind: example
name: Stokes' first and second problems
msc: [76D05, 76D10]
illustrates: [18KXZHVF4M]
uses: [18KXZHVF4M, DF0M8YNQ3D, YCFPD0GE5G]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes_problem
---

## Example

Let a viscous fluid of kinematic viscosity $\nu > 0$ fill the half-space $y > 0$ above a flat plate $y = 0$.
Look for flows $u = (w(y, t), 0, 0)$ with constant pressure.
Such a field is divergence-free, and $(u \cdot \nabla) u = w \, \partial_x u = 0$.
So the [[Navier–Stokes equations|18KXZHVF4M]] reduce to the heat equation $\partial_t w = \nu \, \partial_y^2 w$.

1. *First problem* (impulsively started plate): the fluid is at rest for $t < 0$, and for $t > 0$ the plate moves with constant speed $U$.
The solution is
$$w(y, t) = U \operatorname{erfc}\Big( \frac{y}{2 \sqrt{\nu t}} \Big),$$
where $\operatorname{erfc}(s) = \frac{2}{\sqrt{\pi}} \int_s^\infty e^{-\sigma^2} d\sigma$.
2. *Second problem* (oscillating plate): the plate moves with velocity $U \cos(\omega t)$, with $\omega > 0$.
The time-periodic solution that stays bounded as $y \to \infty$ is
$$w(y, t) = U e^{-k y} \cos(\omega t - k y), \qquad k = \sqrt{\frac{\omega}{2 \nu}}.$$

Check of 2: $w$ is the real part of $W = U e^{i \omega t - (1 + i) k y}$.
Then $\partial_t W = i \omega W$ and $\nu \, \partial_y^2 W = \nu (1 + i)^2 k^2 W = 2 i \nu k^2 W = i \omega W$.
At $y = 0$, $w = U \cos(\omega t)$, so the [[no-slip condition|DF0M8YNQ3D]] holds.
Check of 1: $\operatorname{erfc}(y / (2 \sqrt{\nu t}))$ is the standard similarity solution of the heat equation.
It equals $1$ at $y = 0$ and tends to $0$ as $y \to \infty$ or $t \to 0^+$.

## Remarks

In the first problem the plate's motion spreads into the fluid over a distance of order $\sqrt{\nu t}$.
In the second problem the motion is confined to a layer of thickness of order $\sqrt{2 \nu / \omega}$, the Stokes layer, and the phase lags behind the plate as $y$ grows.
Both are exact solutions of the full Navier–Stokes equations, and both are basic models of a [[boundary layer|YCFPD0GE5G]].
The first problem is also called the Rayleigh problem.

## Explanations

### L1 human

Jerk a plate under a still liquid into motion and the liquid near it is dragged along.
The disturbance spreads upward slowly, like heat from a warm wall, reaching a height that grows with the square root of time.
If the plate shakes back and forth instead, only a thin layer moves, and the waves of motion die out quickly with height.
