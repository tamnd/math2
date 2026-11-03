---
tag: FXG9ZQBDVB
kind: example
name: Kelvin wake pattern
msc: [76B20, 76B15]
illustrates: [JT5EGBG2ZV]
uses: [R9WC0Z7Z69, JT5EGBG2ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Kelvin_wake_pattern
same_as:
  wikidata: Q53111159
  wikipedia: Kelvin wake pattern
---

## Example

A small body, such as a ship or a duck, moves with constant speed $U$ along a straight line on the surface of deep water.
In the linear theory of gravity [[water waves|R9WC0Z7Z69]], the steady wave pattern it leaves behind is confined to a wedge behind the body.
The half-angle $\alpha$ of the wedge satisfies
$$\sin\alpha = \frac{1}{3}, \qquad \alpha \approx 19.47^\circ,$$
whatever the speed $U$.
Inside the wedge one sees transverse waves, with crests across the track, and divergent waves, with crests at an angle to it.
The two systems meet on the edge of the wedge in a line of cusps.

## Remarks

Check: work in the frame of the water, and let $P$ be the point that the body passed a time $T$ ago.
Take a wave component sent out from $P$ in a direction at angle $\theta$ to the track.
It is steady in the frame of the body only if its phase speed is $c = U\cos\theta$.
Its energy moves at the group velocity, which by the [[deep-water dispersion relation|JT5EGBG2ZV]] is $c_g = c/2 = \tfrac{1}{2}U\cos\theta$.
So after the time $T$ this energy sits at $P + \tfrac{1}{2}UT\cos\theta\,(\cos\theta, \sin\theta)$, and these points fill the circle of diameter $\tfrac{1}{2}UT$ through $P$, centred at distance $\tfrac{1}{4}UT$ from $P$ towards the body.
The body is at distance $UT$ from $P$, hence at distance $\tfrac{3}{4}UT$ from the centre of a circle of radius $\tfrac{1}{4}UT$.
The tangent lines from the body to all these circles make the angle $\arcsin\left(\tfrac{1}{4} / \tfrac{3}{4}\right) = \arcsin(1/3)$ with the track.
Observations of fast ships show wakes narrower than this angle; the point-source model ignores the finite size of the hull, which matters at high speed.

## Explanations

### L1 human

Look at the wake of a boat from above and you see a V-shaped pattern of waves behind it.
Lord Kelvin showed that, on deep water, the arms of the V always make an angle of about $19.5$ degrees with the path.
So the whole V spans about $39$ degrees.
The surprise is that this angle does not depend on how fast the boat goes.
It comes from the fact that in deep water wave energy travels at half the speed of the wave crests.
