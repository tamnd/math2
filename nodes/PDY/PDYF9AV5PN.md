---
tag: PDYF9AV5PN
kind: example
name: Particular values of the gamma function
msc: [33B15]
illustrates: [0H5SYBSED9]
uses: [0V3FZMVB4K]
sources:
  - url: https://en.wikipedia.org/wiki/Particular_values_of_the_gamma_function
same_as:
  wikidata: Q7140511
  wikipedia: Particular values of the gamma function
---

## Example

Here are some values of the [[gamma function|0V3FZMVB4K]].

| $z$ | $\Gamma(z)$ |
|---|---|
| $n \in \set{1, 2, 3, \ldots}$ | $(n - 1)!$ |
| $\tfrac12$ | $\sqrt{\pi}$ |
| $\tfrac32$ | $\tfrac12\sqrt{\pi}$ |
| $\tfrac52$ | $\tfrac34\sqrt{\pi}$ |
| $n + \tfrac12$, $n \ge 0$ | $\dfrac{(2n)!}{4^n \, n!}\sqrt{\pi}$ |
| $-\tfrac12$ | $-2\sqrt{\pi}$ |
| $-\tfrac32$ | $\tfrac43\sqrt{\pi}$ |

Checks.
The first row is [[the gamma function extends the factorial|0FDCW77H44]].
The value at $\tfrac12$ is [[Gamma of one half|WM5FNBB7K0]].
The [[functional equation|ZCB806EV8A]] $\Gamma(z + 1) = z\Gamma(z)$ gives the others: $\Gamma(\tfrac52) = \tfrac32 \cdot \tfrac12 \sqrt{\pi} = \tfrac34\sqrt\pi$, and $\Gamma(-\tfrac12) = \Gamma(\tfrac12)/(-\tfrac12) = -2\sqrt\pi$, and $\Gamma(-\tfrac32) = \Gamma(-\tfrac12)/(-\tfrac32) = \tfrac43\sqrt\pi$.
For $n = 2$ the general half-integer formula gives $\frac{24}{16 \cdot 2}\sqrt{\pi} = \tfrac34\sqrt{\pi}$, in agreement.

Values at other rational points are less explicit, but the [[reflection formula|WF7KQAQTS2]] gives products:
$$\Gamma\!\left(\tfrac13\right)\Gamma\!\left(\tfrac23\right) = \frac{\pi}{\sin(\pi/3)} = \frac{2\pi}{\sqrt3}, \qquad \Gamma\!\left(\tfrac14\right)\Gamma\!\left(\tfrac34\right) = \frac{\pi}{\sin(\pi/4)} = \pi\sqrt2.$$

## Remarks

The values $\Gamma(\tfrac13)$ and $\Gamma(\tfrac14)$ are known to be [[transcendental numbers|0VTQXTCR2G]].
The value $\Gamma(\tfrac14)$ appears in the arc length of the lemniscate and in elliptic integrals.

## Explanations

### L1 human

At whole numbers the gamma function gives factorials, shifted by one.
At halves it gives rational multiples of $\sqrt{\pi}$, and the sign alternates for negative halves.
At thirds and quarters the single values are new constants, but some of their products are simple.
