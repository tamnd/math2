---
tag: F6ZWKD5W15
kind: definition
name: Cauchy's exponential equation
msc: [39B22]
defines: CEGF8W64VQ
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
---

## Definition

*Cauchy's exponential equation* is the [[functional equation|SRAN4EKWS0]]
$$f(x + y) = f(x)\, f(y) \quad \text{for all } x, y \in \R,$$
for an unknown [[function|0EPAT51DXQ]] $f \colon \R \to \R$.
A solution is a function $f$ that satisfies this identity for all real $x$ and $y$.

## Remarks

Example: $f(x) = e^{3x}$ is a solution, since $e^{3(x + y)} = e^{3x} e^{3y}$.
Non-example: $f(x) = 1 + x$ is not a solution, since $f(1 + 1) = 3$ while $f(1) f(1) = 4$.
Every solution satisfies $f(x) = f(x/2)^2 \ge 0$.
If $f(x_0) = 0$ for one $x_0$, then $f(x) = f(x - x_0) f(x_0) = 0$ for all $x$.
Otherwise $f > 0$ and $\ln f$ is an [[additive function|KF719SZD5T]], so the solutions are $f = 0$ and $f = e^{A}$ with $A$ additive.
The continuous solutions are $f = 0$ and $f(x) = a^x$ with $a > 0$.
