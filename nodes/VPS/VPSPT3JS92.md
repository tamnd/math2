---
tag: VPSPT3JS92
kind: statement
role: theorem
name: Birkhoff's theorem (relativity)
msc: ["83C15", "83C20"]
uses: [3MCZ97SW6V, 6Y50T68WKY, BY4QYYS788, 5AKNNW3W4Z]
about: [6Y50T68WKY, 3MCZ97SW6V]
sources:
  - url: https://en.wikipedia.org/wiki/Birkhoff%27s_theorem_(relativity)
same_as:
  wikidata: Q865665
  wikipedia: Birkhoff's theorem (relativity)
---

## Statement

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]] that solves the vacuum [[Einstein field equations|3MCZ97SW6V]] $R_{ab} = 0$.
Assume $g$ is spherically symmetric: the rotation group $SO(3)$ acts on $M$ by isometries with orbits that are spacelike two-spheres.
Then every point of $M$ has a neighbourhood isometric to an open subset of the [[Schwarzschild metric|6Y50T68WKY]] with some mass parameter $M_0 \in \R$.
Here $M_0 = 0$ gives Minkowski space, and $M_0 < 0$ the negative-mass Schwarzschild metric.
In particular, the metric has, in addition to the rotations, a fourth [[Killing vector field|5AKNNW3W4Z]], which is timelike outside the horizon.

## Remarks

Write the metric as $-e^{2\alpha(t, r)} dt^2 + e^{2\beta(t, r)} dr^2 + r^2 d\Omega^2$, where $r$ is the area radius of the orbit spheres.
The $tr$ component of $R_{ab} = 0$ gives $\partial_t \beta = 0$.
The other components then give $e^{-2\beta} = 1 - 2M_0/r$ and $\alpha = -\beta + f(t)$, and $f$ is removed by a change of the time coordinate.
Regions where $dr$ is null or zero need a separate argument with the same conclusion.

Consequences: the gravitational field outside any spherically symmetric body is the Schwarzschild field, even if the body pulsates or collapses.
So a spherically symmetric source emits no gravitational radiation.

The theorem uses that the vacuum field equations hold; inside matter, spherical symmetry does not force staticity.
With a cosmological constant the same argument gives the Schwarzschild–de Sitter metrics, and for the Einstein–Maxwell equations it gives the Reissner–Nordström metrics.

## Explanations

### L1 human

Birkhoff's theorem says that empty space around a round object always looks the same: it is described by the Schwarzschild solution, fixed by one number, the mass.
Even if a round star swells and shrinks, nothing changes outside it.
This is the gravity version of the fact that a round charged ball looks from outside like a point charge.

### L2 human

The theorem explains why the Schwarzschild metric is the right exterior for every spherical star and every spherical collapse model.
It shows that spherical motions of matter radiate no gravitational waves, so wave emission needs at least a quadrupole deviation from symmetry.
It is the simplest of the uniqueness results for black holes, and it is often proved as a first exercise with the Einstein equations.
