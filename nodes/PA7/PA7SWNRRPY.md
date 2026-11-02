---
tag: PA7SWNRRPY
kind: definition
name: Inverse Mellin transform
msc: [44A15]
defines: CHESR1W1CY
uses: [0RNGDMHT7M, X7GTF3D98F, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_inversion_theorem
---

## Definition

Let $c \in \R$ and let $\varphi$ be a complex function defined on the line $\operatorname{Re} s = c$.
Assume that $y \mapsto \varphi(c + iy)$ is [[integrable|X7GTF3D98F]] on $\R$.
For $x > 0$ and $s \in \C$, let $x^{-s} = e^{-s \log x}$ be the [[complex power|0RNGDMHT7M]].
The *inverse Mellin transform* of $\varphi$ along the line $\operatorname{Re} s = c$ is the function on $(0, \infty)$ given by
$$\mathcal{M}^{-1}_c \varphi(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} x^{-s} \varphi(s) \, ds = \frac{1}{2\pi} \int_{-\infty}^{\infty} x^{-c - iy} \varphi(c + iy) \, dy.$$

## Remarks

The [[Lebesgue integral|DWJF7ABPR1]] converges absolutely for every $x > 0$, because $\abs{x^{-c - iy}} = x^{-c}$.
The result usually depends on $c$.
When $\varphi$ is holomorphic on a vertical strip and decays fast enough, Cauchy's theorem shows that it does not change as $c$ moves inside the strip.
Example: $\varphi = \Gamma$ and $c > 0$.
Stirling's formula gives $\abs{\Gamma(c + iy)} = O(\abs{y}^{c - 1/2} e^{-\pi \abs{y}/2})$, so $\varphi$ is integrable on the line, and $\mathcal{M}^{-1}_c \Gamma(x) = e^{-x}$.
Non-example: $\varphi(s) = 1/s$ and $c > 0$.
Then $\abs{\varphi(c + iy)} = (c^2 + y^2)^{-1/2}$ is not integrable on $\R$, so the definition does not apply; the integral exists only as a limit of integrals over $[c - iT, c + iT]$.
It is common to drop the index $c$ and write $\mathcal{M}^{-1} \varphi$.
