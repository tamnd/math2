---
tag: TZ37HTS1AT
kind: concept
name: GNSS positioning
msc: [86A30, 65H10]
sources:
  - url: https://en.wikipedia.org/wiki/Satellite_navigation_solution
same_as:
  wikidata: Q5514013
  wikipedia: Satellite navigation solution
---

## Summary

GNSS positioning is the computation of a receiver's position from signals of navigation satellites such as GPS.
The receiver measures pseudoranges: signal travel times multiplied by the speed of light, which contain an unknown receiver clock error.
The unknowns are three coordinates and the clock bias, so at least four satellites are needed.
The equations are solved by linearisation and [[least squares|0BYTQ4X1HC]], a version of [[trilateration|7WSH8Z6F7T]] with an extra unknown.

## Explanations

### L1 human

Each satellite broadcasts where it is and what time it sent its signal.
The receiver notes when the signal arrives, and the delay gives the distance to the satellite.
The receiver's own clock is cheap and slightly wrong, so all these distances are off by the same unknown amount.
With four satellites there are four equations for four unknowns: three for position and one for the clock error.
More satellites give extra equations, which average out measurement noise.
