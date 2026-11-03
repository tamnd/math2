---
tag: 1X8YRWYAX4
kind: definition
name: Ergosphere
msc: ["83C57", "83C15"]
defines: SWZFAXCQMT
uses: [BY4QYYS788, 5AKNNW3W4Z, D8NZ32Z3SQ, 3HTF65XMF7]
sources:
  - url: https://en.wikipedia.org/wiki/Ergosphere
---

## Definition

Let $(M, g)$ be a stationary, [[asymptotically flat|3HTF65XMF7]] spacetime, a [[Lorentzian manifold|BY4QYYS788]] of signature $(-, +, +, +)$ that contains a black hole.
Let $\xi$ be the stationary [[Killing vector field|5AKNNW3W4Z]], normalised so that it is timelike near infinity with $g(\xi, \xi) \to -1$.
The *ergoregion* is the set of points outside the black hole region, that is outside the [[event horizon|D8NZ32Z3SQ]], at which $g(\xi, \xi) > 0$.
Its boundary away from the horizon, where $g(\xi, \xi) = 0$, is the *ergosurface*.
The word *ergosphere* is used for the ergoregion, and sometimes for the ergosurface.

## Remarks

At a point of the ergoregion, $\xi$ is spacelike, so no observer, whose world line is timelike, can follow an orbit of $\xi$.
Every observer there must rotate relative to infinity.

Example: in the [[Kerr metric|X3FZC85THY]] of mass $M$ and spin $a$ with $0 < \abs{a} < M$, in [[Boyer–Lindquist coordinates|2NJH36SR8A]],
$$g(\partial_t, \partial_t) = -\left(1 - \frac{2Mr}{r^2 + a^2 \cos^2\theta}\right).$$
This is positive exactly when $r^2 - 2Mr + a^2\cos^2\theta < 0$, that is when $r < M + \sqrt{M^2 - a^2 \cos^2\theta}$.
The horizon is at $r_+ = M + \sqrt{M^2 - a^2}$.
So the ergoregion is $r_+ < r < M + \sqrt{M^2 - a^2\cos^2\theta}$, which is nonempty for $\theta \ne 0, \pi$ and reaches $r = 2M$ at the equator.

Non-example: for the Schwarzschild metric ($a = 0$), $g(\partial_t, \partial_t) = -(1 - 2M/r) < 0$ for all $r > 2M$.
The set where $\xi$ is spacelike lies inside the horizon, so the ergoregion is empty.
