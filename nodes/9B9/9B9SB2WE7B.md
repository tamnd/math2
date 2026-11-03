---
tag: 9B9SB2WE7B
kind: statement
role: proposition
name: Sunrise equation
msc: [85A04]
uses: [20B8CQHH1S, 5HD86E1TEH, DMAYYCRMJD]
about: [20B8CQHH1S]
sources:
  - url: https://en.wikipedia.org/wiki/Sunrise_equation
same_as:
  wikidata: Q492486
  wikipedia: Sunrise equation
---

## Statement

Let an observer be at geographic latitude $\varphi$ with $\abs{\varphi} < 90^\circ$.
Treat the Sun as a point of fixed [[declination|5HD86E1TEH]] $\delta$ during the day, with $\abs{\delta} < 90^\circ$.
Ignore atmospheric refraction, and call sunrise and sunset the moments when the Sun's altitude in the [[horizontal coordinate system|DMAYYCRMJD]] is $0$.
If $\abs{\tan\varphi\tan\delta} \le 1$, then the Sun sets at the [[hour angle|20B8CQHH1S]] $\omega_0 \in [0^\circ, 180^\circ]$ given by
$$\cos\omega_0 = -\tan\varphi\tan\delta,$$
and rises at the hour angle $-\omega_0$.
If $\tan\varphi\tan\delta > 1$, the Sun does not set that day; if $\tan\varphi\tan\delta < -1$, it does not rise.

## Remarks

The altitude $a$ of the Sun at hour angle $H$ satisfies $\sin a = \sin\varphi\sin\delta + \cos\varphi\cos\delta\cos H$.
Setting $a = 0$ and dividing by $\cos\varphi\cos\delta > 0$ gives the equation.
The altitude is largest at $H = 0$ and decreases in $\abs{H}$, so the solution is unique in $[0^\circ, 180^\circ]$.
The length of the day is $2\omega_0 / 15^\circ$ hours.
Example: at an equinox $\delta = 0$, so $\omega_0 = 90^\circ$ and the day lasts $12$ hours at every latitude.
Example: at $\varphi = 60^\circ$ and $\delta = 23.44^\circ$, $\cos\omega_0 \approx -0.751$, so $\omega_0 \approx 138.7^\circ$ and the day lasts about $18.5$ hours.
For the visible upper limb of the Sun with standard refraction, one replaces $0$ by an altitude of about $-0.83^\circ$.
This gives $\cos\omega_0 = (\sin(-0.83^\circ) - \sin\varphi\sin\delta) / (\cos\varphi\cos\delta)$.

## Explanations

### L1 human

The sunrise equation tells how long the Sun stays up on a given day at a given place.
It needs only the latitude of the place and how far north or south the Sun is that day.
At the equator, or on the day of an equinox, day and night are equal.
Far north in summer the right side of the equation passes $-1$, and the Sun does not set at all.

### L2 human

The equation is the special case $a = 0$ of the formula for the altitude, which is the spherical law of cosines in the triangle pole, zenith, Sun.
It gives the hour angle, and the clock time then follows from the longitude and the equation of time.
The declination of the Sun changes during the day, and refraction lifts the Sun by about half a degree near the horizon.
For precise times one therefore iterates the computation with the corrected altitude $-0.83^\circ$.
The conditions $\abs{\tan\varphi\tan\delta} > 1$ give exactly the polar day and polar night inside the polar circles.
