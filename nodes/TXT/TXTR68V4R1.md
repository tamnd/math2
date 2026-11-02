---
tag: TXTR68V4R1
kind: definition
name: Forward difference operator
msc: [39A70, 39A12]
defines: 8E0EBA8X07
uses: [CYW8E2HTWN, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Definition

Let $M$ be an additive commutative monoid, let $G$ be an additive abelian group, and let $h \in M$.
The *forward difference operator* with step $h$ sends a function $f \colon M \to G$ to the function $\Delta_h f \colon M \to G$ given by
$$\Delta_h f(x) = f(x + h) - f(x) \qquad (x \in M).$$
When $h = 1$, one writes $\Delta$ for $\Delta_1$.
For a sequence $u \colon \N \to G$, this gives $(\Delta u)_n = u_{n+1} - u_n$.

## Remarks

It is a [[finite difference|7JSQZ126BP]] in the forward direction.
The operator $\Delta_h$ is additive: $\Delta_h(f + g) = \Delta_h f + \Delta_h g$.
Example: for $f(x) = 2^x$ on $\Z$ with $h = 1$, $\Delta f(x) = 2^{x+1} - 2^x = 2^x$, so $f$ is a fixed point of $\Delta$, like $e^x$ for the derivative.
Non-example: $g(x) = f(x+1) - f(x-1)$ is not $\Delta_h f$ for any $h$; it is a central difference with step $2$.
With the [[shift operator|MBK6AE6734]] $E_h f(x) = f(x + h)$ and the identity $I$, one has $\Delta_h = E_h - I$.
