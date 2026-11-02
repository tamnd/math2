---
tag: JEXQ0MFJ0Q
kind: definition
name: Airy function
msc: [33C10, 34B30]
defines: 1N5D4PN92W
uses: [PNESAD6R5T, 0H5SYBSED9, 2ET068BZZH]
sources:
  - url: https://en.wikipedia.org/wiki/Airy_function
---

## Definition

For real $x$, the *Airy functions* of the first and second kind are
$$\operatorname{Ai}(x) = \frac{1}{\pi} \int_0^\infty \cos\left( \frac{t^3}{3} + x t \right) dt,$$
$$\operatorname{Bi}(x) = \frac{1}{\pi} \int_0^\infty \left( \exp\left( -\frac{t^3}{3} + x t \right) + \sin\left( \frac{t^3}{3} + x t \right) \right) dt,$$
where the oscillatory integrals are improper Riemann integrals.
Both extend to entire functions of $z \in \C$ that solve the [[Airy equation|PNESAD6R5T]] $y'' = z y$.

## Remarks

The two functions are fixed by their initial values $\operatorname{Ai}(0) = \frac{1}{3^{2/3}\,\Gamma(2/3)}$, $\operatorname{Ai}'(0) = -\frac{1}{3^{1/3}\,\Gamma(1/3)}$, $\operatorname{Bi}(0) = \frac{1}{3^{1/6}\,\Gamma(2/3)}$, $\operatorname{Bi}'(0) = \frac{3^{1/6}}{\Gamma(1/3)}$, where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
Their Wronskian is $\operatorname{Ai}(z) \operatorname{Bi}'(z) - \operatorname{Ai}'(z) \operatorname{Bi}(z) = \frac{1}{\pi}$, so they are independent.
Example: $\operatorname{Ai}$ is the solution that tends to $0$ as $x \to +\infty$, where $\operatorname{Ai}(x) \sim \frac{e^{-\zeta}}{2\sqrt{\pi}\, x^{1/4}}$ with $\zeta = \frac{2}{3} x^{3/2}$; for $x > 0$ it equals $\frac{1}{\pi} \sqrt{\frac{x}{3}}\, K_{1/3}(\zeta)$ with the [[modified Bessel function|2ET068BZZH]] $K_{1/3}$.
A non-example: $\operatorname{Ai} + \operatorname{Bi}$ solves the equation but is not $\operatorname{Ai}$, since it grows like $\operatorname{Bi}$ as $x \to +\infty$.
For $x \to -\infty$, $\operatorname{Ai}(x) \sim \frac{1}{\sqrt{\pi}\, \abs{x}^{1/4}} \sin\left( \frac{2}{3} \abs{x}^{3/2} + \frac{\pi}{4} \right)$.
