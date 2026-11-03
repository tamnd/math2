---
tag: CE8MVD4BF1
kind: object
name: Cornu spiral
msc: [53A04, 33B20, 78A45]
uses: [D0TQ9F2ZDW, EWS4WFTA7W, 0TH78S7GBZ, 7JQS6VKFEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_spiral
same_as:
  wikidata: Q755003
  wikipedia: Euler spiral
---

## Description

The *Cornu spiral*, also called the Euler spiral or clothoid, is the [[plane curve|EWS4WFTA7W]] $t \mapsto (C(t), S(t))$, $t \in \R$, given by the normalised [[Fresnel integrals|D0TQ9F2ZDW]]
$$C(t) = \int_0^t \cos\left(\frac{\pi s^2}{2}\right) ds, \qquad S(t) = \int_0^t \sin\left(\frac{\pi s^2}{2}\right) ds.$$
Its velocity is $(\cos(\pi t^2/2), \sin(\pi t^2/2))$, a unit vector, so $t$ is the [[arc length|0TH78S7GBZ]] measured from the origin.
The angle of the tangent is $\pi t^2/2$, so the [[curvature|7JQS6VKFEZ]] is $\kappa(t) = \pi t$: it grows linearly with arc length.
The curve is symmetric under $t \mapsto -t$, which maps $(C, S)$ to $(-C, -S)$.
As $t \to +\infty$ it winds around the point $(1/2, 1/2)$ and converges to it, and as $t \to -\infty$ it converges to $(-1/2, -1/2)$.

## Remarks

The Cornu spiral is a graphical tool for [[Fresnel diffraction|M8669NXXJS]] by a slit or a straight edge.
The complex amplitude at a point is proportional to a chord joining two points of the spiral.
These two points depend on the positions of the edges relative to the observation point.
For a straight edge, a point deep in the light corresponds to the full chord from $(-1/2, -1/2)$ to $(1/2, 1/2)$.
Moving into the shadow shortens the chord, so the intensity falls off smoothly in the shadow.
On the bright side the chord length oscillates, which gives the fringes.
Because its curvature changes linearly, the same curve is used as a transition curve between a straight line and a circular arc on roads and railways.

## Explanations

### L1 human

The Cornu spiral starts straight at the origin and bends more and more sharply as you move along it, at a steady rate.
So it curls into two tight spirals, one at each end.
Driving along it at constant speed while turning the steering wheel at a steady rate is exactly how a car traces this curve.
