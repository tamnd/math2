---
tag: ZRA2KCZNBP
kind: statement
role: fact
name: Yarkovsky effect
msc: [70F15, 85A04]
uses: [BXFSBB8Q46, A2RMYX8A65]
about: [BXFSBB8Q46]
sources:
  - url: https://en.wikipedia.org/wiki/Yarkovsky_effect
same_as:
  wikidata: Q139771
  wikipedia: Yarkovsky effect
---

## Statement

Let a small rotating body of diameter $D$, such as an asteroid, orbit the Sun.
Its orbit is a nearly circular [[Kepler orbit|BXFSBB8Q46]] with semi-major axis $a$.
Assume that the body absorbs sunlight and re-emits the energy as thermal radiation, close to that of a [[black body|A2RMYX8A65]].
Assume that its thermal inertia is finite and non-zero, so that its surface temperature lags behind the insolation.
Let $\gamma$ be the obliquity, the angle between its spin axis and the normal of its orbital plane.
Then the recoil of the anisotropic thermal emission gives a small force with a component along the orbit.
As a result the semi-major axis drifts secularly, with two parts.

1. The diurnal part, due to the rotation, gives $da/dt$ proportional to $\cos\gamma$.
   The orbit expands for a prograde rotator ($\gamma < 90^\circ$) and shrinks for a retrograde one ($\gamma > 90^\circ$).
2. The seasonal part, due to the motion along the orbit, always makes the orbit shrink, with $da/dt$ proportional to $-\sin^2\gamma$.

For bodies much larger than the depth of penetration of the heat wave, the drift rate $\abs{da/dt}$ scales as $1/D$.

## Remarks

Idea: a surface element is hottest some time after local noon, in the afternoon, so it radiates most in a direction rotated away from the Sun.
For a prograde spin, the net thermal emission leaves partly backwards relative to the orbital motion.
The recoil pushes the body forward, and a forward force increases the energy of the orbit and so $a$.
The force per unit mass falls with size as the area over the volume, which gives the $1/D$ law.

The hypothesis of thermal inertia is necessary.
With instantaneous re-emission the hottest point is the subsolar point, the recoil points away from the Sun, and there is no force along the orbit.

Example: the drift of the near-Earth asteroid (6489) Golevka was detected in 2003 from radar tracking.
The drift of the asteroid (101955) Bennu, which rotates retrograde, has been measured precisely, and its orbit shrinks.

The effect is named after Ivan Yarkovsky, who proposed it around 1900.
It delivers meteorites from the main asteroid belt to resonances that send them towards Earth, and it spreads asteroid families in semi-major axis.

## Explanations

### L1 human

A spinning rock warmed by the Sun gives the heat back a little later, like pavement that is still warm in the evening.
The heat leaves as infrared light, and light carries momentum, so the rock receives a gentle push from the side that radiates most.
Because of the delay, this push is not straight away from the Sun but partly along the orbit, so over millions of years the orbit grows or shrinks.

### L2 human

The force is tiny, less than a billionth of the solar gravity for a body of a kilometre, but it does not average out over an orbit.
The sign of the drift depends on the direction of the spin, through the diurnal term in $\cos\gamma$, and the seasonal term always acts inward.
The related YORP effect, due to the same thermal emission, changes the spin rate and the obliquity, and so changes the Yarkovsky drift over time.
Accurate impact predictions for near-Earth asteroids must include the Yarkovsky drift.
