---
tag: 0NDV5R6Z6X
kind: definition
name: Principal part
aliases: [principal-part-of-a-laurent-series, singular-part]
msc: [30B10]
defines: 0TZ2DPT0JV
uses: [0X3XD2ATB0, 06WHRARZKY]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_part
    locator: Laurent series definition
  - url: https://en.wikipedia.org/wiki/Laurent_series
    locator: Principal part
---

## Definition

Let $c \in \mathbb{C}$, let $R \in (0, \infty]$, and let $f$ be [[holomorphic|0DG0Z72CQD]] on the punctured disc $0 < |z - c| < R$.
Let $f(z) = \sum_{n \in \mathbb{Z}} a_n (z - c)^n$ be the [[Laurent expansion|06WHRARZKY]] of $f$ on this punctured disc.
The principal part of $f$ at $c$ is the series
$$\sum_{n = 1}^{\infty} a_{-n} (z - c)^{-n},$$
the part of the [[Laurent series|0X3XD2ATB0]] with the negative powers of $z - c$.

## Remarks

The principal part converges for each $z \neq c$. The difference $f(z) - \sum_{n \ge 1} a_{-n} (z - c)^{-n}$ extends to a holomorphic function on $|z - c| < R$.
The principal part is $0$ at a [[removable singularity|0P18JC72RE]], it has finitely many nonzero terms at a [[pole|0WPQYW8MTE]], and it has infinitely many at an [[essential singularity|0YKDJBV26S]].
For example, the principal part of $\frac{e^z}{z^2}$ at $0$ is $\frac{1}{z^2} + \frac{1}{z}$.

## Explanations

### L1 human

The principal part is the piece of the function that is responsible for its bad behavior at $c$.
If you subtract it, what is left is holomorphic at $c$.
