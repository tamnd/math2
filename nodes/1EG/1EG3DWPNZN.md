---
tag: 1EG3DWPNZN
kind: definition
name: Error function
msc: ["33B20", "60E05"]
defines: 7Y56QCZSZJ
uses: [0J0FCWV32D, 04TMP0XGMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Error_function
---

## Definition

The *error function* is the function $\operatorname{erf} \colon \R \to \R$ given by the [[definite integral|04TMP0XGMJ]]
$$\operatorname{erf} x = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2}\, dt,$$
where $e^{-t^2}$ uses the [[exponential function|0J0FCWV32D]].

## Remarks

Example: $\operatorname{erf} 0 = 0$, and the [[Gaussian integral|0DFT1GP1JP]] $\int_0^\infty e^{-t^2}\, dt = \frac{\sqrt{\pi}}{2}$ gives $\lim_{x \to \infty} \operatorname{erf} x = 1$.
The integrand is even, so $\operatorname{erf}(-x) = -\operatorname{erf} x$.
Its derivative is $\operatorname{erf}' x = \frac{2}{\sqrt{\pi}} e^{-x^2} > 0$, so $\operatorname{erf}$ increases strictly from $-1$ to $1$.

Non-example: $x \mapsto \int_0^x e^{-t^2}\, dt$ is not the error function; without the factor $\frac{2}{\sqrt{\pi}}$ its limit at $\infty$ is $\frac{\sqrt{\pi}}{2}$, not $1$.

The distribution function of the standard [[normal distribution|05AQE0QR0D]] is $\Phi(x) = \frac12\left(1 + \operatorname{erf}\frac{x}{\sqrt{2}}\right)$.
The same integral, along any path from $0$ to $z$, defines $\operatorname{erf} z$ as an entire function of $z \in \C$, with power series $\operatorname{erf} z = \frac{2}{\sqrt{\pi}} \sum_{n \ge 0} \frac{(-1)^n z^{2n+1}}{n!\,(2n+1)}$.
