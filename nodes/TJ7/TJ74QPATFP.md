---
tag: TJ74QPATFP
kind: statement
role: proposition
name: Gravitational redshift
msc: [83C10, 83B05]
uses: [6Y50T68WKY, 5AKNNW3W4Z, RNRTS8WWNM, QS7YCQK8K7]
about: [6Y50T68WKY]
sources:
  - url: https://en.wikipedia.org/wiki/Gravitational_redshift
same_as:
  wikidata: Q656181
  wikipedia: Gravitational redshift
---

## Statement

Let $M$ be a mass, $G$ the gravitational constant, $c$ the speed of light and $r_s = 2GM/c^2$.
Consider the exterior [[Schwarzschild metric|6Y50T68WKY]] of mass $M$.
Let a static emitter at radius $r_e > r_s$ send light to a static observer at radius $r_o > r_s$.
Let $\nu_e$ be its frequency measured by the emitter.
Then the frequency $\nu_o$ measured by the observer satisfies
$$\frac{\nu_o}{\nu_e} = \sqrt{\frac{1 - r_s/r_e}{1 - r_s/r_o}}.$$
In particular light climbing out of the field ($r_o > r_e$) arrives with lower frequency, and in the weak-field limit
$$\frac{\nu_e - \nu_o}{\nu_e} \approx \frac{\Phi(r_o) - \Phi(r_e)}{c^2}, \qquad \Phi(r) = -\frac{GM}{r}.$$

## Remarks

The vector field $\xi = \partial_t$ is a [[Killing vector field|5AKNNW3W4Z]], so $g(k, \xi)$ is constant along the null [[geodesic|RNRTS8WWNM]] with tangent $k$ followed by the light.
A static observer has four-velocity $u = \xi / \sqrt{-g(\xi, \xi)}$, and the frequency it measures is proportional to $-g(k, u)$.
Since $-g(\xi, \xi) = c^2 (1 - r_s/r)$, $\nu_o/\nu_e$ is the value of $\sqrt{-g(\xi,\xi)}$ at the emitter divided by its value at the observer, which is the formula above.
The same argument works in any static spacetime, with $\sqrt{-g(\xi, \xi)}$ in place of $c\sqrt{1 - r_s/r}$.
The Pound–Rebka experiment, published in 1960, measured the shift of gamma rays over a height of about $22.5$ metres at the surface of the Earth.
The Global Positioning System must correct its clocks for this effect.

## Explanations

### L1 human

Clocks deep in a gravitational field run slow compared with clocks higher up.
So light sent upwards arrives with a lower frequency than it had when it left, shifted towards the red.
Near the Earth the effect is tiny, about one part in $10^{16}$ per metre of height, but atomic clocks can measure it.

### L2 human

The redshift follows already from the [[equivalence principle|QS7YCQK8K7]]: in an accelerated laboratory, light sent from floor to ceiling is Doppler shifted by the motion of the receiver.
So it tests the equivalence principle more than the full field equations of general relativity.
Near a black hole the redshift becomes unbounded as the emitter approaches the horizon $r = r_s$.
