---
tag: 94TR0F5TPX
kind: definition
name: Sidereal time
msc: [85A04]
defines: DRQ3VSN27H
uses: [20B8CQHH1S, QBEJJPMWV1]
sources:
  - url: https://en.wikipedia.org/wiki/Sidereal_time
---

## Definition

Fix an observer on the Earth.
The *local sidereal time* $\mathrm{LST}$ is the [[hour angle|20B8CQHH1S]] of the March equinox for that observer, in hours from $0^{\mathrm h}$ to $24^{\mathrm h}$.
The *Greenwich sidereal time* $\mathrm{GST}$ is the local sidereal time on the meridian of Greenwich.
A *sidereal day* is the interval between two successive meridian passages of the March equinox.

## Remarks

The hour angle of an object of right ascension $\alpha$ is $H = \mathrm{LST} - \alpha$.
So $\mathrm{LST} = \alpha$ exactly for the objects on the local meridian.
For an observer at east longitude $\lambda$, in hours, $\mathrm{LST} = \mathrm{GST} + \lambda$.
Example: if $\mathrm{LST} = 6^{\mathrm h} 45^{\mathrm m}$, then Sirius, with $\alpha \approx 6^{\mathrm h} 45^{\mathrm m}$, is near the meridian.
Non-example: the hour angle of the Sun plus $12^{\mathrm h}$ is apparent solar time, not sidereal time.
The sidereal day is about $23^{\mathrm h} 56^{\mathrm m} 4^{\mathrm s}$ of mean solar time.
"Mean" sidereal time uses the mean equinox, and "apparent" sidereal time uses the true equinox, which includes nutation.
