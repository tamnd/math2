---
tag: 60TDCPY4Z4
kind: concept
name: Poincaré map
msc: [37C27, 34C25, 37C10]
sources:
  - url: https://en.wikipedia.org/wiki/Poincaré_map
same_as:
  wikidata: Q339199
  wikipedia: Poincaré map
---

## Summary

The Poincaré map, or first return map, belongs to a [[periodic orbit|0AA97XA70K]] and a cross-section of it.
It follows nearby solutions once around the orbit until they hit the cross-section again.
It replaces a continuous-time flow in dimension $n$ by a discrete map in dimension $n - 1$.
The periodic orbit becomes a fixed point of the map, and the stability of the orbit is the stability of this fixed point.
The idea is due to Henri Poincaré and is a basic tool in the study of periodic orbits, bifurcations and chaos.

## Explanations

### L1 human

Put a small screen across a closed loop traced by the system.
Start a solution on the screen and wait until it crosses the screen again; the new crossing point is the image of the old one.
If the screen points come closer and closer to the loop, the loop attracts nearby motions.
For motions that spiral onto the unit circle, each crossing of the positive $x$-axis lies closer to the point $(1, 0)$ than the one before.
