---
tag: STJAXZG1K1
kind: definition
name: Cauchy's power equation
msc: [39B22]
defines: MDWN6E58AW
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation
---

## Definition

*Cauchy's power equation* is the [[functional equation|SRAN4EKWS0]]
$$f(xy) = f(x)\, f(y) \quad \text{for all } x, y > 0,$$
for an unknown [[function|0EPAT51DXQ]] $f \colon (0, \infty) \to \R$.
A solution is a function $f$ that satisfies this identity for all positive $x$ and $y$.

## Remarks

Example: $f(x) = \sqrt{x}$ is a solution, since $\sqrt{xy} = \sqrt{x} \sqrt{y}$.
Non-example: $f(x) = 2x$ is not a solution, since $f(1 \cdot 1) = 2$ while $f(1) f(1) = 4$.
The substitution $x = e^s$, $y = e^t$ turns the equation into [[Cauchy's exponential equation|CEGF8W64VQ]] for $g(s) = f(e^s)$.
So the continuous solutions are $f = 0$ and $f(x) = x^c$ with $c \in \R$.
