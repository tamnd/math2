---
tag: 4HMBNA4RMN
kind: definition
name: Function having a given Mellin transform
msc: [44A15]
defines: 1D5VDZYJ20
uses: [SGZZ4Y0D36, N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Definition

Let $f \colon (0, \infty) \to \C$ be measurable, let $s \in \C$ and let $m \in \C$.
The function $f$ *has Mellin transform $m$ at $s$* if both conditions hold:

1. $f$ is [[Mellin convergent|SGZZ4Y0D36]] at $s$, that is, $x \mapsto x^{s-1} f(x)$ is integrable on $(0, \infty)$.
2. The [[Mellin transform|N5PVGRJE1T]] of $f$ at $s$ equals $m$: $\int_0^\infty x^{s-1} f(x) \, dx = m$.

## Remarks

Example: $f = \mathbf{1}_{(0, 1]}$, the indicator function of $(0, 1]$, has Mellin transform $1/s$ at every $s$ with $\operatorname{Re} s > 0$.
Indeed $\int_0^1 x^{\operatorname{Re} s - 1} \, dx = 1/\operatorname{Re} s < \infty$, and $\int_0^1 x^{s-1} \, dx = 1/s$.
Non-example: the same $f$ at $s = 0$ fails clause 1, because $\int_0^1 x^{-1} \, dx$ diverges.
So $f$ does not have Mellin transform $m$ at $0$ for any $m$, although the function $1/s$ has a pole there and no value.
In Mathlib this predicate is `HasMellin f s m`.
