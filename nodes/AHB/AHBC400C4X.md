---
tag: AHBC400C4X
kind: statement
role: proposition
name: Ekman spiral
msc: [86A05, 76U05]
uses: [H5GNFWEW80, 6HZRX3WSQD, NM5Q4845Z4]
about: [H5GNFWEW80]
sources:
  - url: https://en.wikipedia.org/wiki/Ekman_transport
---

## Statement

Consider sea water of constant density $\rho$ filling the half-space $z \le 0$, in a frame rotating with Coriolis parameter $f > 0$ (the northern hemisphere).
Let $\nu > 0$ be a constant vertical eddy [[viscosity|NM5Q4845Z4]].
Let a constant wind stress of magnitude $\tau > 0$ act on the surface $z = 0$ in the $x$-direction.
Assume the horizontal velocity $(u(z), v(z))$ is steady and horizontally uniform, that there is no horizontal pressure gradient, and that it solves
$$-f v = \nu u'', \qquad f u = \nu v'', \qquad \rho \nu u'(0) = \tau, \quad v'(0) = 0, \qquad (u, v) \to 0 \text{ as } z \to -\infty.$$
Set $\delta = \sqrt{2 \nu / f}$ and $V_0 = \tau / (\rho \sqrt{f \nu})$.
Then the unique solution is
$$u = V_0 \, e^{z/\delta} \cos\!\Big( \frac{z}{\delta} - \frac{\pi}{4} \Big), \qquad v = V_0 \, e^{z/\delta} \sin\!\Big( \frac{z}{\delta} - \frac{\pi}{4} \Big).$$
In particular:

1. the surface current has speed $V_0$ and points $45^\circ$ to the right of the wind;
2. with increasing depth the current turns clockwise and its speed decays like $e^{z/\delta}$;
3. the total transport is $\int_{-\infty}^{0} (u, v) \, dz = \big( 0, -\tau / (\rho f) \big)$, at right angles to the right of the wind.

## Remarks

Set $w = u + i v$.
The two equations combine into $w'' = (i f / \nu) w = \big( (1 + i)/\delta \big)^2 w$, whose only solutions that vanish as $z \to -\infty$ are $w = W e^{(1 + i) z / \delta}$.
The stress condition $\rho \nu w'(0) = \tau$ gives $W = V_0 e^{-i \pi / 4}$, which is the formula above.
Integrating $w$ over $z \le 0$ gives $W \delta / (1 + i) = -i \tau / (\rho f)$, which is clause 3.

At the depth $z = -\pi \delta$ the current points opposite to the surface current and is weaker by the factor $e^{-\pi} \approx 0.04$.
This depth is often taken as the thickness of the [[Ekman layer|H5GNFWEW80]].
In the southern hemisphere, $f < 0$, and the same computation gives a spiral turning to the left.
The hypothesis $f \ne 0$ is needed: without rotation the equations reduce to $u'' = v'' = 0$, and no solution decays at depth.

## Explanations

### L1 human

Wind blowing over the sea drags the top layer of water, and the [[Coriolis force|6HZRX3WSQD]] of the rotating Earth turns that water to the right in the northern hemisphere.
Each layer drags the one below, which turns a little further and moves a little slower.
Drawn as arrows at increasing depth, the currents form a spiral that shrinks as it goes down.
Added up, the water moves at a right angle to the wind, not along it.

### L2 human

The spiral was computed by Vagn Walfrid Ekman from a balance between the Coriolis force and vertical friction.
Real ocean spirals are flatter than the model predicts, because the eddy viscosity is not constant and the wind is not steady.
The robust prediction is clause 3: the Ekman transport $\tau / (\rho f)$ does not depend on $\nu$.
Its convergence and divergence pump water down or up out of the [[Ekman layer|H5GNFWEW80]], and this pumping drives the wind-driven circulation of the ocean interior and coastal upwelling.
