---
tag: EBA1CNBYJY
kind: definition
name: Polar motion
msc: [86A30, "70E15"]
defines: QTRK8GS2Y1
uses: [EF1Q2JF8QH]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_motion
---

## Definition

Let $\mathcal{T}$ be a right-handed terrestrial reference frame with third axis near the mean rotation axis.
Its first axis points towards the Greenwich meridian, and its second axis towards $90^\circ$ east longitude.
Let $p(t)$ be the unit vector of the rotation pole in $\mathcal{T}$ at time $t$.
Here the pole is the one used to describe [[the rotation of the Earth|EF1Q2JF8QH]]; in current conventions it is the Celestial Intermediate Pole.
The *polar motion* is the curve $t \mapsto (x_p(t), y_p(t))$, where $x_p$ and $y_p$ are the small angles such that
$$p(t) \approx (x_p(t),\, -y_p(t),\, 1)$$
to first order.
Thus $x_p$ is measured towards the Greenwich meridian and $y_p$ towards $90^\circ$ west longitude.
This is the convention of the International Earth Rotation and Reference Systems Service.

## Remarks

Example: $x_p = 0.1''$ and $y_p = 0.3''$ put the pole about $3$ m from the reference pole towards Greenwich and about $9$ m towards $90^\circ$ west.
Here $1''$ corresponds to about $31$ m on the Earth's surface.
Non-example: the motion of the rotation axis relative to the stars, precession and nutation, is not polar motion, since it is measured in a celestial frame.
Polar motion is reported by the International Earth Rotation and Reference Systems Service in seconds of arc.
