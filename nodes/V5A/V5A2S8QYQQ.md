---
tag: V5A2S8QYQQ
kind: object
name: Lemniscate constant
msc: ["33E05", 11Y60]
instance_of: [0VTQXTCR2G]
uses: [0VTQXTCR2G, 0H5SYBSED9, RM54CPPE12]
sources:
  - url: https://en.wikipedia.org/wiki/Lemniscate_constant
same_as:
  wikidata: Q1248689
  wikipedia: Lemniscate constant
---

## Description

The *lemniscate constant* is $\varpi = 2.62205755429\ldots$, defined by
$$\varpi = 2\int_0^1 \frac{dt}{\sqrt{1 - t^4}}.$$
It plays for the lemniscate of Bernoulli $(x^2 + y^2)^2 = x^2 - y^2$ the role that $\pi$ plays for the unit circle.
The lemniscate has total arc length $2\varpi$, as the circle has length $2\pi$.

1. With the [[gamma function|0H5SYBSED9]], $\varpi = \dfrac{\Gamma(1/4)^2}{2\sqrt{2\pi}}$.
2. With the [[complete elliptic integral of the first kind|RM54CPPE12]], $\varpi = \sqrt2\,K(1/\sqrt2)$.
3. With the arithmetic–geometric mean $M$, $\varpi = \pi / M(1, \sqrt2)$; the number $\varpi/\pi = 1/M(1, \sqrt 2) = 0.8346\ldots$ is Gauss's constant.
4. $\varpi$ is a [[transcendental number|0VTQXTCR2G]].

## Remarks

Check of point 1: the substitution $s = t^4$ gives $\int_0^1 (1 - t^4)^{-1/2}\,dt = \frac14 B(1/4, 1/2) = \frac14\,\Gamma(1/4)\Gamma(1/2)/\Gamma(3/4)$.
The reflection formula $\Gamma(1/4)\Gamma(3/4) = \pi/\sin(\pi/4) = \pi\sqrt2$ and $\Gamma(1/2) = \sqrt\pi$ turn this into $\Gamma(1/4)^2/(4\sqrt{2\pi})$, which is $\varpi/2$.
Check of point 2: with $t = \cos\theta$ and $1 - \cos^4\theta = \sin^2\theta\,(1 + \cos^2\theta)$, one gets $\int_0^1 dt/\sqrt{1 - t^4} = \int_0^{\pi/2} d\theta/\sqrt{1 + \cos^2\theta} = \int_0^{\pi/2} d\theta/\sqrt{2 - \sin^2\theta} = K(1/\sqrt2)/\sqrt2$.
The [[lemniscate sine|TQDZQ964AZ]] first reaches $1$ at $\varpi/2$, as the sine first reaches $1$ at $\pi/2$.

## Explanations

### L1 human

Everyone knows $\pi$, the half-length of the unit circle.
The lemniscate constant is the analogous number for the figure-eight lemniscate: half its length is $\varpi \approx 2.622$.
It turns up in elliptic integrals, in the arithmetic–geometric mean of $1$ and $\sqrt 2$, and in values of the gamma function at $1/4$.
