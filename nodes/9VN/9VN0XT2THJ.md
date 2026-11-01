---
tag: 9VN0XT2THJ
kind: definition
name: Symmetric derivative
msc: [26A24]
defines: B40P5MJYYJ
uses: [0XHDTE5YMZ, 0TXTSEMHR5, 0F1WR9C83K, AZBDB5F4M4]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_derivative
    locator: Definition
---

## Definition

Let $I \subseteq \R$ be an open interval, let $f \colon I \to \R$ be a [[function|0XHDTE5YMZ]], and let $x \in I$.
The function $f$ is *symmetrically differentiable* at $x$ if the [[limit|0TXTSEMHR5]]
$$f_s(x) = \lim_{h \to 0} \frac{f(x + h) - f(x - h)}{2h}$$
exists and is a real number.
The number $f_s(x)$ is the *symmetric derivative* of $f$ at $x$.

## Remarks

If $f$ is differentiable at $x$, then $\frac{f(x + h) - f(x - h)}{2h}$ is the average of two [[difference quotients|AZBDB5F4M4]] with increments $h$ and $-h$.
Both tend to $f'(x)$, so $f_s(x) = f'(x)$.
The symmetric derivative does not use the value $f(x)$.
For example, the indicator function of $\set{0}$ has symmetric derivative $0$ at $0$, although it is not continuous there.

Example: $f(x) = \abs{x}$ at $x = 0$.
For $h \ne 0$, the quotient is $\frac{\abs{h} - \abs{-h}}{2h} = 0$, so $f_s(0) = 0$, while $f'(0)$ does not exist.

Non-example: $f(x) = \sqrt[3]{x}$ at $x = 0$.
The quotient is $\frac{h^{1/3} + h^{1/3}}{2h} = h^{-2/3}$, which tends to $+\infty$, so the limit is not a real number.
