---
tag: WE89NFZ84Q
kind: example
name: Van der Pol oscillator
msc: [34C15, 34C26, 34C07]
illustrates: [0AAQ73WRFB]
uses: [D2KC8NEAPS, 178GG6TXKQ, 0YG0ZJPTWG, 09ZWYRQ41J]
sources:
  - url: https://en.wikipedia.org/wiki/Van_der_Pol_oscillator
---

## Example

Let $\mu > 0$.
The van der Pol oscillator is the equation
$$x'' - \mu (1 - x^2)\, x' + x = 0.$$
It is a [[Liénard equation|D2KC8NEAPS]] with $f(x) = -\mu (1 - x^2)$ and $g(x) = x$, so $F(x) = \mu (x^3/3 - x)$.
The function $F$ has the single positive zero $\sqrt{3}$, is negative on $(0, \sqrt{3})$, and is increasing on $(1, \infty)$.
By [[Liénard's theorem|178GG6TXKQ]], the equation has exactly one [[limit cycle|0AAQ73WRFB]], and it is stable.

## Remarks

The only equilibrium is the origin.
The [[linearisation|09ZWYRQ41J]] there is $x'' - \mu x' + x = 0$, whose characteristic roots $\frac{1}{2}\left(\mu \pm \sqrt{\mu^2 - 4}\right)$ have positive real part.
So the origin is unstable, and every other solution tends to the limit cycle.
For $\mu = 0$ the equation is the [[harmonic oscillator|0YG0ZJPTWG]].
For small $\mu > 0$, the limit cycle is close to the circle of radius $2$ in the $(x, x')$-plane.
For large $\mu$, the oscillation is a [[relaxation oscillation|2NHWCM0DK8]]: slow drifts alternate with fast jumps.

## Explanations

### L1 human

The van der Pol oscillator is an oscillator with negative friction for small swings and positive friction for large swings.
Small motions grow and large motions shrink, so all motions settle on one oscillation of a definite size.
It was first studied as a model of electrical circuits with vacuum tubes.
