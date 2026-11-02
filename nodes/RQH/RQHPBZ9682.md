---
tag: RQHPBZ9682
kind: definition
name: Mean-periodic function
msc: [42A75, 42A85]
defines: N470GNCK2Y
uses: [0X3WGX95FE, HZNEQQBCW4, FQTXV6BQZG, 2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Mean-periodic_function
---

## Definition

Let $f \colon \R \to \C$ be a [[continuous function|0X3WGX95FE]].
Let $\mu$ range over the nonzero complex [[Radon measures|HZNEQQBCW4]] on $\R$ with compact [[support|FQTXV6BQZG]].
The function $f$ is *mean-periodic* if the [[convolution|2Z29JN3VES]] of $f$ with some such $\mu$ vanishes:
$$(f * \mu)(x) = \int_{\R} f(x - y) \, d\mu(y) = 0 \quad \text{for all } x \in \R.$$

## Remarks

Give $C(\R)$ the topology of uniform convergence on compact sets.
Its dual space is the space of compactly supported complex Radon measures.
By the Hahn–Banach theorem, $f$ is mean-periodic if and only if the closed linear span of the translates $x \mapsto f(x - a)$, $a \in \R$, is not all of $C(\R)$.
Some authors allow $\mu$ to be a compactly supported distribution instead of a measure.

Example: if $f$ is continuous with period $p > 0$, take $\mu = \delta_0 - \delta_p$.
Then $(f * \mu)(x) = f(x) - f(x - p) = 0$, so $f$ is mean-periodic.
Similarly $f(x) = e^{\lambda x}$ with $\lambda \in \C$ satisfies $f * (\delta_0 - e^{\lambda} \delta_1) = 0$.

Non-example: $f(x) = e^{x^2}$ is not mean-periodic.
Suppose $f * \mu = 0$ with $\mu$ compactly supported, and let $\nu$ be the measure $e^{y^2} d\mu(y)$.
Then $(f * \mu)(x) = e^{x^2} \int e^{-2xy} \, d\nu(y)$, so $F(z) = \int e^{-2zy} \, d\nu(y)$ vanishes for real $z$.
Since $\nu$ has compact support, $F$ is an entire function, so $F = 0$ on $\C$.
On the imaginary axis $F$ is the Fourier transform of $\nu$, so $\nu = 0$ and $\mu = 0$.
