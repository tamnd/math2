---
tag: TYE6885WXJ
kind: definition
name: Hour angle
msc: [85A04]
defines: 20B8CQHH1S
uses: [QBEJJPMWV1, W7GD4WR497]
sources:
  - url: https://en.wikipedia.org/wiki/Hour_angle
---

## Definition

Fix an observer on the Earth and a direction $u$ on the [[celestial sphere|W7GD4WR497]], not at a celestial pole.
The *local meridian* is the half great circle from the north celestial pole through the zenith to the south celestial pole.
The *hour circle* of $u$ is the half great circle from the north celestial pole through $u$ to the south celestial pole.
The *hour angle* $H$ of $u$ is the angle along the celestial equator from the local meridian to the hour circle of $u$, measured westward.
It is given in hours, with $1^{\mathrm h} = 15^\circ$, either in $[0^{\mathrm h}, 24^{\mathrm h})$ or in $(-12^{\mathrm h}, 12^{\mathrm h}]$.

## Remarks

The hour angle uses the celestial equator of the [[equatorial coordinate system|QBEJJPMWV1]], but counts from a meridian that turns with the Earth.
So it equals the local sidereal time minus the right ascension: $H = \mathrm{LST} - \alpha$.
Example: a star on the meridian has $H = 0$; six sidereal hours later it has $H = 6^{\mathrm h}$.
Non-example: right ascension is counted eastward from the March equinox; it is fixed for a star, while $H$ grows with time.
A negative hour angle means the object has not yet reached the meridian.
