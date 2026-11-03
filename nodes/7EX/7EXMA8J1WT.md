---
tag: 7EXMA8J1WT
kind: example
name: Hohmann transfer orbit
msc: [70M20, 70F05]
instance_of: [BXFSBB8Q46]
uses: [S95BKBMH2Z, 20XK96APWK, 0VKCCEXBJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Hohmann_transfer_orbit
same_as:
  wikidata: Q723861
  wikipedia: Hohmann transfer orbit
---

## Example

Let $\mu > 0$ and let $0 < r_1 < r_2$ be the radii of two coplanar circular orbits about the same centre.
The *Hohmann transfer orbit* is the [[ellipse|0VKCCEXBJ1]] with a focus at the centre, periapsis distance $r_1$ and apoapsis distance $r_2$.
Its semi-major axis is $a = (r_1 + r_2)/2$.
It is a [[Kepler orbit|BXFSBB8Q46]], used as follows.
A tangential burn at radius $r_1$ moves the craft from the inner circle onto the ellipse.
Half an orbit later, at radius $r_2$, a second tangential burn moves it onto the outer circle.

By the [[vis-viva equation|S95BKBMH2Z]] the two changes of speed are
$$\Delta v_1 = \sqrt{\frac{\mu}{r_1}} \left( \sqrt{\frac{2 r_2}{r_1 + r_2}} - 1 \right), \qquad \Delta v_2 = \sqrt{\frac{\mu}{r_2}} \left( 1 - \sqrt{\frac{2 r_1}{r_1 + r_2}} \right).$$
Check of $\Delta v_1$: on the circle the speed is $\sqrt{\mu / r_1}$, and on the ellipse at $r_1$ it is $\sqrt{\mu (2/r_1 - 2/(r_1 + r_2))} = \sqrt{\mu / r_1} \sqrt{2 r_2 / (r_1 + r_2)}$.
The transfer takes half a period, $\pi \sqrt{(r_1 + r_2)^3 / (8 \mu)}$.

Numbers: go from a low Earth orbit with $r_1 = 6678$ km to the geostationary radius $r_2 = 42164$ km, with $\mu = 398600\ \mathrm{km^3/s^2}$.
Then $\Delta v_1 \approx 2.43$ km/s, $\Delta v_2 \approx 1.47$ km/s, and the transfer takes about $5.3$ hours.

## Remarks

Among transfers with two impulses between coplanar circular orbits, the Hohmann transfer needs the least total change of speed.
With three impulses one can sometimes do better, as the bi-elliptic transfer shows when $r_2 / r_1$ is large.
It is the basic manoeuvre of [[orbital mechanics|20XK96APWK]], named after Walter Hohmann, who described it in 1925.

## Explanations

### L1 human

To move a satellite from a low circle to a high circle, speed it up once so that it coasts up along half an ellipse.
At the top, speed it up again so that it stays on the high circle.
This two-step plan uses very little fuel, though it is slow.
