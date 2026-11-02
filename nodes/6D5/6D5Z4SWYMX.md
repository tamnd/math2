---
tag: 6D5Z4SWYMX
kind: definition
name: Zak transform
msc: [42A38, 42C15]
defines: S026HQSGY9
uses: [SASP14MA1Z, G12KXDHPPS, CG9JEATW3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Zak_transform
---

## Definition

Let $f$ be a function in the [[Schwartz space|CG9JEATW3Q]] $\mathcal{S}(\R)$.
The *Zak transform* of $f$ is the function $Zf \colon \R^2 \to \C$,
$$Zf(x, \omega) = \sum_{k \in \Z} f(x + k) \, e^{-2\pi i k \omega}.$$
For general $f \in L^2(\R)$ (see [[Lp space|SASP14MA1Z]]), $Zf$ is defined by continuous extension, with the series converging in $L^2([0, 1)^2)$.

## Remarks

For fixed $x$, $Zf(x, \cdot)$ is a [[Fourier series|G12KXDHPPS]] with coefficients $f(x + k)$.
The map $Z$ extends to a unitary operator from $L^2(\R)$ onto $L^2([0, 1)^2)$.
The values are quasi-periodic: $Zf(x, \omega + 1) = Zf(x, \omega)$ and $Zf(x + 1, \omega) = e^{2\pi i \omega} Zf(x, \omega)$.
The second rule follows by putting $j = k + 1$ in the series.
Some authors include a lattice parameter $a > 0$ and use $f(x + ak)$.

Example: let $f = 1_{[0, 1)}$.
For $x \in [0, 1)$ only the term $k = 0$ is nonzero, so $Zf(x, \omega) = 1$ on $[0, 1)^2$.
Then $\norm{Zf}^2_{L^2([0,1)^2)} = 1 = \norm{f}_2^2$, as unitarity requires.

Non-example: the map $f \mapsto \sum_{k \in \Z} f(x + k)$ without phase factors is the periodization of $f$.
It loses information, for instance it sends $1_{[0, 1/2)} - 1_{[1, 3/2)}$ to $0$.
