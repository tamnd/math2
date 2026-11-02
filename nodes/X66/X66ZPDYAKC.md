---
tag: X66ZPDYAKC
kind: definition
name: Differentiable curve
msc: [53A04]
defines: C57T562NKB
uses: [0JF1XXGWB4, WK5HPW5Y24, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_curve
---

## Definition

Let $n \ge 1$ be an integer, let $k \ge 1$ be an integer or $k = \infty$, and let $I \subseteq \R$ be an [[interval|0TK8Y3J5RW]] with more than one point.
Let $\gamma \colon I \to \R^n$, $\gamma(t) = (\gamma_1(t), \dots, \gamma_n(t))$, be a [[parametrised curve|0JF1XXGWB4]].
The curve $\gamma$ is a *differentiable curve of class $C^k$* if each coordinate function $\gamma_i$ is of class $C^k$ (see [[smoothness classes|WK5HPW5Y24]]) on $I$.
This means that $\gamma_i$ is $k$ times differentiable and its derivatives up to order $k$ are continuous.
At an end point of $I$ that belongs to $I$, the derivatives are one-sided.
A *smooth curve* is a differentiable curve of class $C^\infty$.

## Remarks

Example: $\gamma(t) = (t, t^2)$, $t \in \R$, is a smooth curve, since both coordinates are polynomials.
Non-example: $\gamma(t) = (t, \abs{t})$, $t \in \R$, is a continuous curve but not of class $C^1$, because the second coordinate has no derivative at $t = 0$.
A differentiable curve can still have a cusp in its image: $t \mapsto (t^2, t^3)$ is smooth, but its velocity vanishes at $t = 0$.
Curves whose velocity never vanishes are the [[regular curves|06JMR2XWXW]].
