---
tag: KRJAF5K1YA
kind: statement
role: proposition
name: Time dilation
msc: [83A05]
uses: [WEVGN4C7PQ, 2E9AJVZS6E, YG74WHC3S9]
about: [YG74WHC3S9, 2E9AJVZS6E]
sources:
  - url: https://en.wikipedia.org/wiki/Time_dilation
same_as:
  wikidata: Q185918
  wikipedia: Time dilation
---

## Statement

Let $S$ be an inertial frame and let a clock move with constant velocity $\mathbf{v}$ relative to $S$, where $v = \abs{\mathbf{v}} < c$.
Let two events on the clock's world line be separated by the [[proper time|YG74WHC3S9]] $\Delta\tau$, the time shown by the clock between them.
Then the time between the same two events measured in $S$ is
$$\Delta t = \gamma \, \Delta\tau, \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}},$$
where $\gamma$ is the [[Lorentz factor|2E9AJVZS6E]].
In particular $\Delta t > \Delta\tau$ whenever $v \ne 0$ and $\Delta\tau > 0$.

## Remarks

Proof idea: in the rest frame $S'$ of the clock, the two events are $(t', x') = (0, 0)$ and $(\Delta\tau, 0)$.
The inverse [[Lorentz transformation|WEVGN4C7PQ]] gives $t = \gamma (t' + v x' / c^2)$, so $\Delta t = \gamma \Delta\tau$.
Equivalently, the spacetime interval gives $c^2 \Delta\tau^2 = c^2 \Delta t^2 - v^2 \Delta t^2$.
Example: muons made in the upper atmosphere have a mean lifetime of about $2.2$ microseconds at rest.
At $\gamma = 10$ they live about $22$ microseconds in the Earth frame, long enough for many to reach the ground.
The effect is symmetric: each of two inertial observers finds the other's clock slow, which is consistent because they compare different pairs of events.
The constant-velocity hypothesis can be dropped by integrating: for any timelike world line, $\Delta\tau = \int \sqrt{1 - v(t)^2/c^2} \, dt \le \Delta t$.

## Explanations

### L1 human

A moving clock ticks more slowly than the clocks it passes.
At everyday speeds the effect is far too small to notice, but at speeds near $c$ it is large.
At $60\%$ of the speed of light, the moving clock shows $8$ seconds while $10$ seconds pass for the observer.

### L2 human

Time dilation is the simplest consequence of the Lorentz transformation and is usually derived together with length contraction.
It is the same statement as the fact that the proper time along a straight world line is the length of that world line in the Minkowski metric.
Its integrated form underlies the twin paradox: among timelike world lines between two events, the straight one has the largest proper time.
Satellite navigation systems must correct for it, together with the gravitational effect of general relativity.
