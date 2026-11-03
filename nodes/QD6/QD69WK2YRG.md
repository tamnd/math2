---
tag: QD69WK2YRG
kind: definition
name: Orbital elements
msc: [70F15, 70M20, 70F05]
defines: K6KNWEVRY4
uses: [BXFSBB8Q46, 0HVX863SAJ]
sources:
  - url: https://en.wikipedia.org/wiki/Orbital_elements
---

## Definition

Fix a reference plane through the central body, a reference direction in it, and a reference time $t_0$.
Let a body move on an elliptic [[Kepler orbit|BXFSBB8Q46]] whose plane is not the reference plane.
Its *Keplerian orbital elements* are the six numbers:

1. the semi-major axis $a > 0$ of the ellipse;
2. the [[eccentricity|0HVX863SAJ]] $e \in [0, 1)$;
3. the inclination $i \in [0, \pi]$, the angle between the orbital plane and the reference plane;
4. the longitude of the ascending node $\Omega \in [0, 2\pi)$, the angle in the reference plane from the reference direction to the ascending node;
5. the argument of periapsis $\omega \in [0, 2\pi)$, the angle in the orbital plane from the ascending node to the periapsis;
6. the mean anomaly $M_0 \in [0, 2\pi)$ at time $t_0$.

The ascending node is the point where the body crosses the reference plane going upwards.
The mean anomaly at time $t$ is $n (t - \tau)$, where $n = 2\pi / T$ is the mean motion, $T$ the period and $\tau$ a time of periapsis passage.

## Remarks

The map from orbital elements to position and velocity at $t_0$ is a bijection onto the elliptic states, away from the cases $e = 0$ and $i \in \set{0, \pi}$.
For $e = 0$ the periapsis is not defined, and for $i = 0$ or $i = \pi$ the node is not defined; equinoctial elements avoid these problems.
Example: the International Space Station, with the Earth's equator as reference plane, has roughly $a \approx 6780$ km, $e < 0.001$ and $i \approx 51.6^\circ$; all six elements are defined because $0 < e < 1$ and $0 < i < \pi$.
Non-example: a geostationary orbit has $i = 0$, so its plane is the reference plane, the ascending node does not exist and clause 4 cannot be applied.
The true anomaly or the time of periapsis passage can replace the mean anomaly as the sixth element.
