---
tag: 9HGAVQ8BRR
kind: definition
name: Shadow zone
msc: [86A15, 74J05]
defines: ABCFGTGWE6
uses: [AZFGJKMKTP, JAFNCJNF6E, EEPJJHC5JZ, GZ7E9GHQYB]
sources:
  - url: https://en.wikipedia.org/wiki/Shadow_zone
---

## Definition

Let a spherically symmetric Earth model have wave speed $v(r)$ for a given wave type, and fix a point source at the surface.
For each [[ray parameter|JAFNCJNF6E]] $p$, let $\Delta(p)$ be the angular distance at which the direct [[seismic ray|AZFGJKMKTP]] with parameter $p$ returns to the surface.
The *shadow zone* of that wave type is the set of epicentral distances $\Delta \in [0°, 180°]$ that are not of the form $\Delta(p)$ for any direct ray.

## Remarks

A ray with parameter $p$ turns at a radius $r$ where $r / v(r) = p$.
If $r/v(r)$ jumps at some radius because the speed drops sharply with depth, a range of values of $p$ has no turning point above that radius.
Those rays enter the low-speed region, bend strongly, and emerge much farther away, which leaves a gap in the distances $\Delta(p)$.
Example: at the core–mantle boundary the [[P-wave|EEPJJHC5JZ]] speed falls from about $13.7$ km/s to about $8$ km/s.
The direct P-waves that just miss the core emerge near $104°$, and those that enter it emerge beyond about $140°$, so the P shadow zone is roughly $104°$ to $140°$.
For [[S-waves|GZ7E9GHQYB]] the outer core is liquid and has $v = 0$, so no direct S-ray crosses it, and the shadow is everything beyond about $104°$.
Non-example: a station at $60°$ receives direct P-waves that turn in the lower mantle, so $60°$ is not in the P shadow zone.
The definition is in terms of rays; waves diffracted along the core and waves reflected from the inner core still bring weak energy into the shadow.
