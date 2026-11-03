---
tag: NZKHXG3YQ0
kind: example
name: Kármán vortex street
msc: [76D25, 76B47]
illustrates: [B7PKESV4CV]
uses: [B3SXT9TWFA, JH9EJ0HA0R, B7PKESV4CV, BTHH4Y71QR]
sources:
  - url: https://en.wikipedia.org/wiki/K%C3%A1rm%C3%A1n_vortex_street
same_as:
  wikidata: Q1044416
  wikipedia: Kármán vortex street
---

## Example

A *Kármán vortex street* is the double row of vortices in the wake of a bluff body, such as a cylinder, in a steady stream.
Vortices are shed alternately from the two sides of the body.
The vortices of the two rows turn in opposite senses, so the [[vorticity|B3SXT9TWFA]] of the wake alternates in sign.
For a circular cylinder the street appears once the [[Reynolds number|JH9EJ0HA0R]] based on the diameter exceeds a critical value of about $47$.
Let $D$ be the diameter and $U$ the speed of the stream.
Over a wide range of Reynolds numbers above this value, the shedding frequency $f$ satisfies $f D / U \approx 0.2$.
So the [[Strouhal number|B7PKESV4CV]] of the flow stays nearly constant.

## Remarks

Von Kármán studied an idealised model: two infinite rows of point vortices in an ideal fluid.
One row has vortices of [[circulation|BTHH4Y71QR]] $\Gamma$ at the points $(na, h/2)$, and the other has vortices of circulation $-\Gamma$ at the points $((n + \tfrac{1}{2})a, -h/2)$, for all integers $n$.
This staggered array moves as a whole, parallel to the rows, with speed $\frac{\Gamma}{2a} \tanh\left(\frac{\pi h}{a}\right)$.
A linear stability analysis shows that the staggered array is neutrally stable only when $\sinh(\pi h / a) = 1$, that is $h / a \approx 0.281$, and unstable otherwise.
The symmetric arrangement, with the two rows facing each other, is always unstable.

## Explanations

### L1 human

When wind or water flows past a pole, the wake does not stay calm.
Swirls peel off the pole, first from one side and then from the other, and they drift downstream in two staggered rows.
The regular shedding makes the pole feel a periodic sideways push, which is why wires sing in the wind.
The rate of shedding is proportional to the flow speed and inversely proportional to the size of the body.
