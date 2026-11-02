---
tag: VSTM4MZJXZ
kind: definition
name: Numerical differentiation
msc: [65D25]
defines: NVH3F8FTYS
uses: [0V1EJCT8G6, 04TKTF8KDK, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_differentiation
---

## Definition

Let $k \ge 1$ be an integer, let $f$ be a real function defined near a point $x \in \R$, and let $s_1, \ldots, s_N$ be distinct real numbers.
A *numerical differentiation formula* for the [[$k$-th derivative|04TKTF8KDK]] $f^{(k)}(x)$ is an expression
$$D_h f(x) = \frac{1}{h^k} \sum_{j=1}^{N} a_j \, f(x + s_j h), \qquad h > 0,$$
with real coefficients $a_1, \ldots, a_N$ that do not depend on $h$ or $f$.
It has *order* $p \ge 1$ if $D_h f(x) - f^{(k)}(x) = O(h^p)$ as $h \to 0$ for every $f$ of class $C^{k+p}$ near $x$, in [[big O notation|0TGV80E6A4]].
*Numerical differentiation* is the approximation of $f^{(k)}(x)$ by such formulas, or more generally by derivatives of functions fitted to finitely many values of $f$.

## Remarks

Example: the central difference $D_h f(x) = \frac{f(x + h) - f(x - h)}{2h}$ for $k = 1$, with stencil $-1, 1$ and $a = (-\tfrac12, \tfrac12)$, has order $2$.
Check with Taylor's theorem for $f \in C^3$: $f(x \pm h) = f(x) \pm h f'(x) + \frac{h^2}{2} f''(x) \pm \frac{h^3}{6} f'''(\xi_\pm)$, so $D_h f(x) - f'(x) = O(h^2)$.
The forward difference $\frac{f(x + h) - f(x)}{h}$ has only order $1$, with error $\frac{h}{2} f''(\xi)$.
Non-example: $\frac{f(x+h) + f(x)}{h}$ approximates no derivative; for $f = 1$ it equals $\frac{2}{h}$, which does not tend to $f'(x) = 0$.
In floating-point arithmetic with unit round-off $u$, the forward difference has total error about $\frac{h}{2}\abs{f''} + \frac{2u\abs{f}}{h}$, which is smallest for $h$ of the order of $\sqrt{u}$.

## Explanations

### L1 human

A numerical differentiation formula combines a few nearby values of a function to estimate one of its derivatives.
The order says how fast the error shrinks when the spacing $h$ shrinks: order $2$ means that halving $h$ divides the error by about $4$.
