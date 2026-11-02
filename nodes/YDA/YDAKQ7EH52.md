---
tag: YDAKQ7EH52
kind: definition
name: Barnes G-function
msc: ["33B15"]
defines: 7E2JJWFF00
uses: [0H5SYBSED9, 0G4F0XB9X2, 00C5P9JZBK]
sources:
  - url: https://en.wikipedia.org/wiki/Barnes_G-function
---

## Definition

Let $\gamma$ be the [[Euler–Mascheroni constant|00C5P9JZBK]].
The *Barnes G-function* is the [[entire function|0G4F0XB9X2]] $G$ given for $z \in \C$ by
$$G(1 + z) = (2\pi)^{z/2} \exp\left(-\frac{z + (1+\gamma) z^2}{2}\right) \prod_{k=1}^\infty \left(1 + \frac{z}{k}\right)^k \exp\left(\frac{z^2}{2k} - z\right).$$

## Remarks

The product converges uniformly on compact sets.
The function $G$ satisfies $G(1) = 1$ and
$$G(z + 1) = \Gamma(z)\, G(z)$$
for all $z$, where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
At a pole of $\Gamma$ the right side is read as a limit, since $G$ has a zero there.

Example: the recurrence gives $G(2) = \Gamma(1) G(1) = 1$, $G(3) = \Gamma(2) G(2) = 1$, $G(4) = \Gamma(3) G(3) = 2$ and $G(5) = \Gamma(4) G(4) = 12$.
In general $G(n) = \prod_{k=0}^{n-2} k!$ for integers $n \ge 2$.

Non-example: the function $F(z) = G(z) \cdot (1 + \sin^2 \pi z)$ also satisfies $F(1) = 1$ and $F(z+1) = \Gamma(z) F(z)$, but it is not $G$.
So the recurrence alone does not determine $G$; one needs an extra condition, for example that $\frac{d^3}{dx^3} \log G(x) \ge 0$ for $x > 0$.

From the product, $G$ has zeros exactly at $z = -n$ for integers $n \ge 0$, of order $n + 1$.
