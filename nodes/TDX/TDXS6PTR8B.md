---
tag: TDXS6PTR8B
kind: example
name: Rainbow
msc: [78A05, 86A10]
illustrates: [QDV9SBK6W0, GMRYG4S3G0]
uses: [QDV9SBK6W0, JSTZ7M5VEB, 9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Rainbow
same_as:
  wikidata: Q1052
  wikipedia: Rainbow
---

## Example

Model a raindrop as a sphere of water with [[refractive index|9VGK0SP6EQ]] $n > 1$ in air.
A ray enters the drop with angle of incidence $i$ and is refracted to the angle $r$ given by [[Snell's law|QDV9SBK6W0]] $\sin i = n \sin r$.
It is [[reflected|JSTZ7M5VEB]] once inside and then leaves the drop.
Its total deviation is
$$D(i) = \pi + 2i - 4r.$$
Since $\cos i = n \cos r \, \frac{dr}{di}$, the condition $D'(i) = 0$ reads $n \cos r = 2 \cos i$.
Squaring and using $n^2 \cos^2 r = n^2 - \sin^2 i$ gives
$$\cos^2 i = \frac{n^2 - 1}{3}.$$
For $n = 4/3$ this gives $i \approx 59.4^\circ$, $r \approx 40.2^\circ$ and the minimum deviation $D \approx 138^\circ$.
Near a minimum of $D$ many rays leave in almost the same direction.
So the light is concentrated at the angle $180^\circ - 138^\circ = 42^\circ$ from the point opposite the Sun.
This concentration of rays is a [[caustic|GMRYG4S3G0]], and it is the primary rainbow.

## Remarks

The index of water is slightly larger for violet light than for red light.
So violet has a slightly smaller rainbow angle, and red is on the outside of the bow.
Rays reflected twice inside the drop give a second minimum of deviation, near $51^\circ$, which is the fainter secondary rainbow with the colours reversed.
The ray model does not explain the supernumerary bands inside the bow; they need wave optics.

## Explanations

### L1 human

Sunlight entering a raindrop bends, bounces off the back of the drop and bends again on the way out.
The amount by which the light is turned has a minimum, and many rays leave near that minimum, at about $42^\circ$ from the shadow of your head.
That is why the rainbow is a circle of that angular radius around the point opposite the Sun.
Each colour bends by a slightly different amount, so the colours separate.
