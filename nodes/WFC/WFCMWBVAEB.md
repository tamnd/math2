---
tag: WFCMWBVAEB
kind: statement
role: proposition
name: Frame-dragging
msc: [83C10, 83C15]
uses: [X3FZC85THY, 5AKNNW3W4Z, 7M7M55TKXA]
about: [X3FZC85THY]
sources:
  - url: https://en.wikipedia.org/wiki/Frame-dragging
same_as:
  wikidata: Q15149343
  wikipedia: Frame-dragging
---

## Statement

Work in units with $G = c = 1$.
Let $M > 0$ and $0 < a \le M$, and consider the [[Kerr metric|X3FZC85THY]] of mass $M$ and angular momentum $J = aM$ in Boyer–Lindquist coordinates $(t, r, \theta, \varphi)$, outside the event horizon.
Let a *zero angular momentum observer* be an observer whose four-velocity $u$ satisfies $g(u, \partial_\varphi) = 0$.
Then such an observer at $(r, \theta)$ moves with coordinate angular velocity
$$\omega = \frac{d\varphi}{dt} = -\frac{g_{t\varphi}}{g_{\varphi\varphi}} = \frac{2 M a r}{(r^2 + a^2)^2 - a^2 \Delta \sin^2\theta}, \qquad \Delta = r^2 - 2Mr + a^2,$$
which is positive, so it rotates in the same sense as the body.
At large $r$, $\omega \approx 2J/r^3$.

## Remarks

The vector fields $\partial_t$ and $\partial_\varphi$ are [[Killing vector fields|5AKNNW3W4Z]], and $g(u, \partial_\varphi) = 0$ means $u$ is proportional to $\partial_t + \omega \, \partial_\varphi$ with $g_{t\varphi} + \omega g_{\varphi\varphi} = 0$.
Inserting the Kerr components $g_{t\varphi} = -2Mar\sin^2\theta/\Sigma$ and $g_{\varphi\varphi} = ((r^2 + a^2)^2 - a^2\Delta\sin^2\theta)\sin^2\theta/\Sigma$, with $\Sigma = r^2 + a^2\cos^2\theta$, gives the formula.
Inside the ergosphere, where $g_{tt} > 0$, no observer can stay at fixed $\varphi$: all observers are dragged around with the rotation.
The same effect makes the planes of orbits precess (Lense–Thirring precession) and makes gyroscopes near a rotating body precess relative to the distant stars.
For $a = 0$ the metric is the Schwarzschild metric and $\omega = 0$: a body that does not rotate drags nothing.

## Explanations

### L1 human

In [[general relativity|7M7M55TKXA]] a rotating mass pulls spacetime around with it, a little like a spinning ball in honey drags the honey.
An observer who tries not to rotate, in the sense of having zero angular momentum, is still carried around the body as seen from far away.
Near the Earth the effect is extremely small, but near a fast-spinning black hole it is so strong that nothing can stay still.

### L2 human

In the weak field, frame-dragging is the gravitomagnetic part of the metric, the off-diagonal terms $g_{ti}$ produced by mass currents.
Its effects on satellites were measured by laser ranging of the LAGEOS satellites and by the gyroscopes of the Gravity Probe B mission.
In astrophysics it shapes accretion disks around spinning black holes and powers the extraction of rotational energy from them.
