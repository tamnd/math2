---
tag: 0SXZ68HV6F
kind: example
name: Integral of 1/z around the unit circle
aliases: [contour-integral-of-1-over-z]
msc: ["30E20"]
instance_of: [0AP750DHVP]
uses: [0T7ABX4CWE, 054VXHMCA3]
sources:
  - url: https://en.wikipedia.org/wiki/Contour_integration
    locator: Example
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem
    locator: Discussion
---

## Example

The [[circle integral|0T7ABX4CWE]] of $f(z) = 1/z$ over the unit circle $|z| = 1$ is
$$\oint_{|z| = 1} \frac{dz}{z} = 2 \pi i.$$
Computation: the path is $\gamma(\theta) = e^{i\theta}$ with $\theta \in [0, 2\pi]$, so $\gamma'(\theta) = i e^{i\theta}$. Then
$$\oint_{|z| = 1} \frac{dz}{z} = \int_0^{2\pi} \frac{i e^{i\theta}}{e^{i\theta}} \, d\theta = \int_0^{2\pi} i \, d\theta = 2 \pi i.$$
More generally, let $c, w \in \mathbb{C}$ and $R > 0$. If $|w - c| < R$, then $\oint_{|z - c| = R} \frac{dz}{z - w} = 2 \pi i$. If $|w - c| > R$, the integral is $0$.

## Remarks

For each integer $n \neq -1$, $\oint_{|z| = 1} z^n \, dz = 0$, because $z^n$ has a primitive on $\mathbb{C} \setminus \{0\}$.
The value is not $0$, so $1/z$ has no primitive on $\mathbb{C} \setminus \{0\}$, and [[Cauchy's integral theorem|01MPZXYVYF]] does not apply on $\mathbb{C} \setminus \{0\}$.
This integral is the base of [[Cauchy's integral formula|0DG10TVYPN]], of the [[residue|0JFGKKWWFK]] and of the [[winding number|0X7SBS8E0F]].

## Explanations

### L1 human

On the unit circle, $dz$ is $i z \, d\theta$, so $dz / z$ is just $i \, d\theta$.
Going once around adds up $i \, d\theta$ over a full turn of $2\pi$, which gives $2 \pi i$.
