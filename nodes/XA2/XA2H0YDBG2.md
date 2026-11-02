---
tag: XA2H0YDBG2
kind: definition
name: Logarithmic potential
msc: [31A15]
defines: 46NHWJHW44
uses: [JHKSF3XFY2, VDZ5FKYC2T, DYR1QFNGNJ, FQTXV6BQZG, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
---

## Definition

Identify $\R^2$ with $\C$.
Let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\C$ with finite total mass and compact [[support|FQTXV6BQZG]].
The *logarithmic potential* of $\mu$ is the function $p_\mu \colon \C \to (-\infty, +\infty]$,
$$p_\mu(z) = \int \log \frac{1}{\abs{z - w}} \, d\mu(w).$$
It is the [[potential|JHKSF3XFY2]] of $\mu$ with respect to the [[logarithmic kernel|VDZ5FKYC2T]].

## Remarks

Example: let $\mu$ be the uniform probability measure on the unit circle.
Then $p_\mu(z) = 0$ for $\abs{z} \le 1$ and $p_\mu(z) = -\log\abs{z}$ for $\abs{z} \ge 1$, by the mean value property.
For $\abs{z} > 1$ apply it to the harmonic function $w \mapsto \log\abs{z - w}$ on the disc $\abs{w} < \abs{z}$.
For $\abs{z} < 1$ write $\abs{z - e^{it}} = \abs{1 - z e^{-it}}$ and apply it to the harmonic function $\zeta \mapsto \log\abs{1 - z\zeta}$ on the disc $\abs{\zeta} < 1/\abs{z}$; the case $\abs{z} = 1$ follows from $\int_0^{2\pi} \log\abs{1 - e^{it}} \, dt = 0$.
Example: for $\mu = \sum_{j=1}^d \delta_{z_j}$ one gets $p_\mu(z) = -\log\abs{(z - z_1)\cdots(z - z_d)}$.
Non-example: for Lebesgue measure on all of $\C$ the integral diverges at every point, which is why the definition asks for a finite measure with compact support.
The function $p_\mu$ is [[harmonic|0DEB0JMN0W]] on $\C \setminus \operatorname{supp}\mu$, and $p_\mu(z) = -\mu(\C) \log\abs{z} + o(1)$ as $\abs{z} \to \infty$.
In the sense of distributions, $\Delta p_\mu = -2\pi\mu$.
Some authors use the opposite sign, $\int \log\abs{z - w} \, d\mu(w)$, which is subharmonic.
