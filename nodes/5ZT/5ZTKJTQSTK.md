---
tag: 5ZTKJTQSTK
kind: problem
name: Stability of the Solar System
msc: [70F15, 70F10, 37N05]
uses: [62SNWC5E45, 3ZZSXKM16Z, DBKXCGDKTD]
about: [62SNWC5E45]
sources:
  - url: https://en.wikipedia.org/wiki/Stability_of_the_Solar_System
  - url: https://en.wikipedia.org/wiki/Opticks
same_as:
  wikidata: Q2497813
  wikipedia: Stability of the Solar System
history:
  posed_by: "Isaac Newton"
  first_stated: "1706"
---

## Problem

Model the Sun and the planets as point masses that move by Newton's law of gravitation.
Their motion is then a solution of the [[n-body problem|62SNWC5E45]].
Does the present Solar System stay bounded for all future time, with no collisions and no escape of a planet?
Do the orbits of the planets stay close to their present shapes?

## Remarks

In the queries of the Opticks Newton suggested that the mutual perturbations of the planets might grow until the system needs a reformation.
Laplace and Lagrange showed that, to first order in the masses, the semi-major axes of the planets have no secular drift.
The [[Kolmogorov–Arnold–Moser theorem|3ZZSXKM16Z]] shows that, for small enough masses, many initial conditions lead to quasi-periodic motions that last forever.
But the real masses are far too large for the known estimates.
Laskar showed in 1989, by integrating averaged equations over 200 million years, that the motion of the inner planets is chaotic in the sense of [[chaos theory|DBKXCGDKTD]].
So the positions of the planets cannot be predicted more than some tens of millions of years ahead.
Laskar and Gastineau computed 2501 orbits with very close initial conditions over 5 billion years.
In about one percent of them the eccentricity of Mercury grew enough to allow a collision with Venus or the Sun.
The question in its mathematical form is open.

## Explanations

### L1 human

Will the planets keep going round the Sun as they do now, forever?
Each planet pulls on the others a little, and over billions of years these small pulls might add up.
Computer studies show that the system is chaotic, so the far future cannot be predicted exactly.
They also suggest that a serious change, such as Mercury hitting Venus, has only a small chance in the lifetime of the Sun.
