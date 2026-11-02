---
tag: DJBY0QQA80
kind: definition
name: Integral operator
msc: [47G10, 45P05]
defines: H8P36XFV8K
uses: [56MJSVTHG0, CW5CEF84T2, 0RJF668P1T, XVEWR93EMV, 7KGF78FGEF]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_operator
---

## Definition

Let $(X, \mu)$ and $(Y, \nu)$ be [[measure spaces|56MJSVTHG0]] whose measures are [[sigma-finite|CW5CEF84T2]].
Let $K \colon X \times Y \to \C$ be a measurable function, the *kernel*.
The *integral operator* with kernel $K$ is the [[linear map|0RJF668P1T]] $T$ given by
$$(Tf)(x) = \int_Y K(x, y)\, f(y)\, d\nu(y).$$
Its domain is the set of measurable functions $f \colon Y \to \C$ for which the [[Lebesgue integral|XVEWR93EMV]] $\int_Y \abs{K(x, y) f(y)}\, d\nu(y)$ is finite for $\mu$-almost every $x \in X$.

## Remarks

Example: on $X = Y = [0, 1]$ with Lebesgue measure, the kernel $K(x, y) = 1$ for $y < x$ and $K(x, y) = 0$ for $y \ge x$ gives the Volterra operator $(Vf)(x) = \int_0^x f(y)\, dy$.
It is defined for every integrable $f$, because $\int_0^1 \abs{K(x, y) f(y)}\, dy \le \int_0^1 \abs{f}$.
Non-example: the identity map of $L^2([0,1])$ is linear but is not an integral operator with a function kernel.
Such a kernel would give $\int_A K(x, y)\, dy = 1$ for almost every $x \in A$ and $0$ for almost every $x \notin A$, for every interval $A$.
This would force the measure $K(x, y)\, dy$ to be a point mass at $x$, which is impossible.
If $K$ is in $L^2(X \times Y)$, the operator maps the [[Lebesgue space|7KGF78FGEF]] $L^2(Y)$ to $L^2(X)$ and is bounded with norm at most $\norm{K}_{L^2}$.
Such operators are called Hilbert–Schmidt integral operators, and they are compact.
