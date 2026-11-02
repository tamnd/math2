---
tag: TFB4BYRZ1W
kind: definition
name: Uniform approximation
msc: [41A65, 41A50, 41A10]
defines: XAARVNKXF1
uses: [VNWH2KADN7, 08FPABDQ4C, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_norm
---

## Definition

Let $S$ be a set, let $f \colon S \to \R$ be a [[function|0EPAT51DXQ]], and let $A$ be a set of functions $S \to \R$.
For $\varepsilon > 0$, a function $g \in A$ *approximates $f$ uniformly within $\varepsilon$* if
$$\sup_{x \in S} \abs{f(x) - g(x)} \le \varepsilon.$$
The function $f$ *can be uniformly approximated by $A$* if such a $g \in A$ exists for every $\varepsilon > 0$.
Equivalently, there is a sequence $g_n \in A$ that [[converges uniformly|08FPABDQ4C]] to $f$ on $S$.

## Remarks

Example: on $S = [0, 1]$, the function $e^x$ can be uniformly approximated by polynomials.
By Taylor's theorem, $\abs{e^x - \sum_{k=0}^{n} x^k / k!} \le e / (n + 1)!$ for $x \in [0, 1]$, and the bound tends to $0$.

Non-example: on $S = \R$, the function $e^x$ cannot be uniformly approximated by polynomials.
For each polynomial $p$, the difference $e^x - p(x)$ tends to $\infty$ as $x \to \infty$, so the supremum is infinite.

For bounded functions, the quantity $\sup_S \abs{f - g}$ is the distance in the supremum norm, and uniform approximation is [[function approximation|VNWH2KADN7]] in that norm.
Complex-valued functions are treated in the same way.
