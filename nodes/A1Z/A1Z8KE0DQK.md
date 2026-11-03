---
tag: A1Z8KE0DQK
kind: example
name: Bi-elliptic transfer
msc: [70M20, 70F05]
illustrates: [S95BKBMH2Z]
uses: [7EXMA8J1WT, S95BKBMH2Z, BXFSBB8Q46]
sources:
  - url: https://en.wikipedia.org/wiki/Bi-elliptic_transfer
same_as:
  wikidata: Q3997712
  wikipedia: Bi-elliptic transfer
---

## Example

Let $\mu > 0$, let $0 < r_1 < r_2$ be the radii of two coplanar circular orbits about the same centre, and choose $r_b \ge r_2$.
The *bi-elliptic transfer* uses two half-ellipses, both [[Kepler orbits|BXFSBB8Q46]].
A first tangential burn at $r_1$ puts the craft on an ellipse with periapsis $r_1$ and apoapsis $r_b$, of semi-major axis $a_1 = (r_1 + r_b)/2$.
At $r_b$ a second burn raises the periapsis to $r_2$, giving an ellipse of semi-major axis $a_2 = (r_2 + r_b)/2$.
At $r_2$ a third, braking, burn puts the craft on the outer circle.
By the [[vis-viva equation|S95BKBMH2Z]] the three changes of speed are
$$\Delta v_1 = \sqrt{\frac{2\mu}{r_1} - \frac{\mu}{a_1}} - \sqrt{\frac{\mu}{r_1}}, \quad \Delta v_2 = \sqrt{\frac{2\mu}{r_b} - \frac{\mu}{a_2}} - \sqrt{\frac{2\mu}{r_b} - \frac{\mu}{a_1}}, \quad \Delta v_3 = \sqrt{\frac{2\mu}{r_2} - \frac{\mu}{a_2}} - \sqrt{\frac{\mu}{r_2}}.$$

Check with numbers: take $\mu = 1$, $r_1 = 1$, $r_2 = 20$ and let $r_b \to \infty$.
Then $\Delta v_1 \to \sqrt{2} - 1$, $\Delta v_2 \to 0$ and $\Delta v_3 \to (\sqrt{2} - 1)/\sqrt{20}$, a total of about $0.507$.
The [[Hohmann transfer|7EXMA8J1WT]] between the same circles needs $\Delta v_1 + \Delta v_2 \approx 0.380 + 0.155 = 0.535$.
So here the bi-elliptic transfer is cheaper.

## Remarks

If $r_2 / r_1 < 11.94$ approximately, the Hohmann transfer is cheaper for every choice of $r_b$.
If $r_2 / r_1 > 15.58$ approximately, the bi-elliptic transfer is cheaper for every $r_b > r_2$.
In between, it depends on $r_b$.
The saving is small and the bi-elliptic transfer takes much longer.

## Explanations

### L1 human

To climb from a low orbit to a very high one, it can pay to overshoot first.
The craft goes far out, where a small push is enough to change the low point of its orbit, and then falls back to the target circle.
For very large climbs this three-burn path uses less fuel than the direct two-burn Hohmann path.
