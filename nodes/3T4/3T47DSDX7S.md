---
tag: 3T47DSDX7S
kind: statement
role: fact
name: Hack's law
msc: [86A05]
uses: [2XGF4FECN5, W5X8VSTM8P]
about: [2XGF4FECN5]
sources:
  - url: https://en.wikipedia.org/wiki/Hack%27s_law
same_as:
  wikidata: Q1032350
  wikipedia: Hack's law
---

## Statement

For a drainage basin, let $A$ be its area.
Let $L$ be the length of its longest stream, measured from the outlet to the drainage divide.
Over many basins of different sizes, $L$ and $A$ follow approximately a power law
$$L = C A^h.$$
Here $C > 0$ is a constant, and the exponent $h$ is close to $0.6$.

## Remarks

It is an empirical law, named after the geologist John Hack, found by fitting measured basins, and the values of $C$ and $h$ vary from region to region.
If basins were geometrically similar, length would scale like the square root of area, so $h = 1/2$.
An exponent above $1/2$ means that large basins are relatively longer and thinner than small ones.
For example, with $h = 0.6$, a basin with four times the area of another has a main stream about $4^{0.6} \approx 2.3$ times as long, not $2$ times.
Since the main stream meanders, its length also grows faster than straight-line distance, and both effects contribute to the exponent.

## Explanations

### L1 human

Bigger river basins have longer rivers, and Hack's law says how much longer.
The river length grows like the area raised to about the power $0.6$.
This is a bit faster than one would guess from simply scaling up a map, so large basins are stretched out compared with small ones.

### L2 human

Hack's law is one of the scaling laws of river networks in [[hydrology|2XGF4FECN5]], together with [[Horton's laws|W5X8VSTM8P]].
On a log-log plot of $L$ against $A$, measured basins lie near a line of slope $h$.
The departure of $h$ from $1/2$ is often read as a sign that river networks are self-similar fractals rather than scaled copies of one shape.
