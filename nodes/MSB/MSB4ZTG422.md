---
tag: MSB4ZTG422
kind: concept
name: Kepler's equation
msc: [70F05, 70F15, 65H05]
uses: [M1A7XV292M, 0VKCCEXBJ1, 0HVX863SAJ]
sources:
  - url: https://en.wikipedia.org/wiki/Kepler%27s_equation
same_as:
  wikidata: Q932001
  wikipedia: Kepler's equation
---

## Summary

Kepler's equation is $M = E - e \sin E$, which links the time along an elliptic Kepler orbit to the position on it.
Here $e$ is the [[eccentricity|0HVX863SAJ]] of the [[ellipse|0VKCCEXBJ1]], the mean anomaly $M$ grows linearly with time, and the eccentric anomaly $E$ fixes the position.
Solving it for $E$ is the step that turns [[Kepler's laws|M1A7XV292M]] into a prediction of where a planet is at a given time.
It has no solution in elementary functions, and it has been a classical test case for numerical methods and series expansions.

## Explanations

### L1 human

Kepler's laws say which ellipse a planet follows and how fast it sweeps area, but not directly where it is on a given date.
Kepler's equation answers this question.
The clock time gives the number $M$, and solving the equation gives the angle $E$, from which the position follows.
For a circular orbit, $e = 0$ and simply $E = M$: the planet moves around at a constant rate.
