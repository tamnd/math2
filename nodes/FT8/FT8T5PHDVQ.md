---
tag: FT8T5PHDVQ
kind: statement
role: proposition
name: Shapiro time delay
msc: [83C10, 83B05]
uses: [6Y50T68WKY, RNRTS8WWNM, 2TAW8GAMM1]
about: [RNRTS8WWNM]
sources:
  - url: https://en.wikipedia.org/wiki/Shapiro_time_delay
same_as:
  wikidata: Q1848968
  wikipedia: Shapiro time delay
---

## Statement

Let $M$ be a mass, $G$ the gravitational constant and $c$ the speed of light.
Consider the weak field of the [[Schwarzschild metric|6Y50T68WKY]] of mass $M$.
Let a light signal travel along a null [[geodesic|RNRTS8WWNM]] between two points at distances $r_1$ and $r_2$ from the mass.
Let $d$ be the Euclidean distance between the two points.
Then, to first order in $GM/c^2$, the coordinate travel time exceeds the flat-space value $d/c$ by
$$\Delta t = \frac{2 G M}{c^3} \ln\left( \frac{r_1 + r_2 + d}{r_1 + r_2 - d} \right).$$
If the ray passes the mass at closest distance $b \ll r_1, r_2$, this becomes $\Delta t \approx \frac{2GM}{c^3} \ln \frac{4 r_1 r_2}{b^2}$, and a radar echo that goes and returns has twice this delay.

## Remarks

In the weak field the metric is $ds^2 \approx -(1 - 2GM/(c^2 r)) c^2 dt^2 + (1 + 2GM/(c^2 r)) \abs{d\mathbf{x}}^2$ in isotropic coordinates.
Along a null ray, $c \, dt \approx (1 + 2GM/(c^2 r)) \abs{d\mathbf{x}}$, so the delay is $(2GM/c^3) \int dl / r$ along the straight line, and this integral is the logarithm above.
Shapiro proposed the effect in 1964 as a new test of general relativity, using radar echoes from Venus and Mercury.
In the [[parameterized post-Newtonian formalism|2TAW8GAMM1]] the delay is multiplied by $(1 + \gamma)/2$; tracking of the Cassini spacecraft in 2002 found $\gamma$ equal to $1$ within about $2 \times 10^{-5}$.

## Explanations

### L1 human

A radar pulse that passes close to the Sun takes a little longer to come back than it would if the Sun were not there.
The extra time is about two hundred microseconds for a signal that grazes the Sun on its way to a planet behind it and back.
In general relativity this happens because clocks run slow and distances stretch near the Sun.

### L2 human

The Shapiro delay is the time-domain partner of the deflection of light: both come from the same weak-field metric and both measure the parameter $\gamma$.
It is also seen in binary pulsars, where the pulses from a pulsar are delayed as they pass its companion, and this gives a way to measure the companion's mass.
The delay depends on the path through its logarithm, so it is largest for rays that pass close to the mass.
