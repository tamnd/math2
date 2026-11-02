---
tag: ZNC09JXRC5
kind: definition
name: Kontorovich–Lebedev transform
msc: [44A20, 33C10]
defines: XFJDYMB91J
uses: [2ET068BZZH, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Kontorovich%E2%80%93Lebedev_transform
---

## Definition

For $y \in \R$ and $x > 0$ let $K_{iy}(x) = \int_0^\infty e^{-x\cosh t} \cos(yt)\, dt$ be the [[modified Bessel function of the second kind|2ET068BZZH]] of order $iy$.
Let $f \colon (0, \infty) \to \C$ be measurable with $\int_0^\infty \abs{f(x)}\, K_0(x)\, dx < \infty$.
The *Kontorovich–Lebedev transform* of $f$ is the function $g \colon \R \to \C$ given by the [[Lebesgue integral|DWJF7ABPR1]]
$$g(y) = \int_0^\infty f(x)\, K_{iy}(x)\, dx.$$

## Remarks

The integral converges absolutely because $\abs{K_{iy}(x)} \le \int_0^\infty e^{-x\cosh t}\, dt = K_0(x)$.
The function $K_{iy}(x)$ is real and even in $y$, so $g$ is even and is usually considered on $(0, \infty)$.
Under suitable conditions on $f$, the inversion formula is
$$f(x) = \frac{2}{\pi^2 x} \int_0^\infty g(y)\, K_{iy}(x)\, \sinh(\pi y)\, y\, dy.$$

Example: $f(x) = 1$.
Since $K_0(x)$ behaves like $-\log x$ near $0$ and like $\sqrt{\pi/(2x)}\, e^{-x}$ at infinity, $K_0$ is integrable and the condition holds.
The formula $\int_0^\infty K_\mu(x)\, dx = \frac{\pi}{2\cos(\pi\mu/2)}$ for $\abs{\operatorname{Re} \mu} < 1$, with $\mu = iy$, gives $g(y) = \frac{\pi}{2\cosh(\pi y / 2)}$.

Non-example: $f(x) = e^x$.
For fixed $y$, $K_{iy}(x) \sim \sqrt{\pi/(2x)}\, e^{-x}$ as $x \to \infty$, so $f(x) K_{iy}(x) \sim \sqrt{\pi/(2x)}$ and the integral diverges at infinity.
