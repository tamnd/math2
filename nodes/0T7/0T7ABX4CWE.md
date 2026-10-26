---
tag: 0T7ABX4CWE
kind: definition
name: Circle integral
msc: ["30E20"]
defines: 0AP750DHVP
uses: [00FWNP9TXY, 054VXHMCA3]
sources:
  - url: https://en.wikipedia.org/wiki/Contour_integration
    locator: Example
---

## Definition

Let $c \in \mathbb{C}$ and let $R > 0$ be a real number.
Let $f$ be a complex function that is continuous on the circle $\{z : |z - c| = R\}$.
The circle integral of $f$ over this circle is the [[contour integral|00FWNP9TXY]] along the path $\gamma(\theta) = c + R e^{i\theta}$, $\theta \in [0, 2\pi]$:
$$\oint_{|z - c| = R} f(z) \, dz = \int_0^{2\pi} f(c + R e^{i\theta}) \, i R e^{i\theta} \, d\theta.$$

## Remarks

The path goes once around the circle, in the positive (counterclockwise) direction.
The length of the path is $2 \pi R$.
The basic example is the [[integral of 1/z|0SXZ68HV6F]]: $\oint_{|z| = 1} \frac{dz}{z} = 2 \pi i$.

## Explanations

### L1 human

A circle integral is a contour integral where the path is a circle, traveled once counterclockwise.
Circles are the paths that appear most in complex analysis, for example in [[Cauchy's integral formula|0DG10TVYPN]].
