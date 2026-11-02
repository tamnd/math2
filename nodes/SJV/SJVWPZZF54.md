---
tag: SJVWPZZF54
kind: definition
name: d'Alembert's functional equation
msc: [39B22, 39B52]
defines: 6PXHVPFTAS
uses: [SRAN4EKWS0, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Definition

*d'Alembert's functional equation* is the [[functional equation|SRAN4EKWS0]]
$$f(x + y) + f(x - y) = 2 f(x) f(y) \quad \text{for all } x, y \in \R,$$
for an unknown [[function|0EPAT51DXQ]] $f \colon \R \to \R$.
A solution is a function $f$ that satisfies this identity for all real $x$ and $y$.

## Remarks

Example: $f(x) = \cos(2x)$ is a solution, by the product formula $2 \cos u \cos v = \cos(u + v) + \cos(u - v)$.
Non-example: $f(x) = 2$ is not a solution, since the left side is $4$ and the right side is $8$.
Setting $y = 0$ gives $2 f(x) = 2 f(x) f(0)$, so either $f = 0$ or $f(0) = 1$.
If $f(0) = 1$, setting $x = 0$ gives $f(-y) = f(y)$, so every nonzero solution is even.
The continuous solutions are $f = 0$, $f(x) = \cos(ax)$ and $f(x) = \cosh(ax)$ with $a \in \R$.
The same equation is studied for complex-valued functions on groups, in the form $f(xy) + f(xy^{-1}) = 2 f(x) f(y)$.
