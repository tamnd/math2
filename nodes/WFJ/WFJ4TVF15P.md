---
tag: WFJ4TVF15P
kind: definition
name: Bateman transform
msc: [35C15, 31B05, 35L05]
defines: KR5Q7WMAVC
uses: [0NAHXR1FRH, 0DEB0JMN0W, S8RG6N1PRT, 5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Bateman_transform
---

## Definition

Let $U \subseteq \R^4$ be open and let $C$ be a piecewise smooth closed curve in $\C$.
For $x = (x_1, x_2, x_3, x_4) \in U$ and $\zeta \in \C$ put
$$A(x, \zeta) = (x_1 + i x_2) + (x_4 + i x_3)\, \zeta, \qquad B(x, \zeta) = (x_4 - i x_3) - (x_1 - i x_2)\, \zeta.$$
Let $\Omega \subseteq \C^3$ be an open set that contains the points $(A(x, \zeta), B(x, \zeta), \zeta)$ for all $x \in U$ and $\zeta \in C$.
Let $f(w_1, w_2, \zeta)$ be a [[holomorphic function|0NAHXR1FRH]] on $\Omega$.
The *Bateman transform* of $f$ is the function $u \colon U \to \C$ given by
$$u(x) = \oint_C f\big(A(x, \zeta), B(x, \zeta), \zeta\big)\, d\zeta.$$

## Remarks

The function $u$ is [[harmonic|0DEB0JMN0W]] on $U$, that is, it solves [[Laplace's equation|S8RG6N1PRT]] $\sum_{k=1}^4 \partial_k^2 u = 0$.
Indeed, by the chain rule, $\sum_k \partial_k^2$ applied to $f(A, B, \zeta)$ is a combination of second derivatives of $f$ with coefficients $\sum_k (\partial_k A)^2$, $\sum_k \partial_k A\, \partial_k B$ and $\sum_k (\partial_k B)^2$.
The gradients are $\nabla A = (1, i, i\zeta, \zeta)$ and $\nabla B = (-\zeta, i\zeta, -i, 1)$, and all three sums vanish: $1 - 1 - \zeta^2 + \zeta^2 = 0$, $-\zeta - \zeta + \zeta + \zeta = 0$ and $\zeta^2 - \zeta^2 - 1 + 1 = 0$.
Differentiation under the integral sign then gives $\Delta u = 0$.
When $\Omega$ also contains the points $(A(x, \zeta), B(x, \zeta), \zeta)$ with $x_4$ replaced by $i t$, the same integral defines $u(x_1, x_2, x_3, i t)$.
Replacing $x_4$ by $i t$ turns $\partial_{x_4}^2$ into $-\partial_t^2$, so $u(x_1, x_2, x_3, it)$ solves the [[wave equation|5EHD2XBQDG]] $\partial_t^2 u = \partial_1^2 u + \partial_2^2 u + \partial_3^2 u$.

Example: $f(w_1, w_2, \zeta) = \frac{w_1}{\zeta^2}$ and $C$ the unit circle.
Then $u(x) = \oint_C \Big( \frac{x_1 + i x_2}{\zeta^2} + \frac{x_4 + i x_3}{\zeta} \Big) d\zeta = 2\pi i\, (x_4 + i x_3)$, a linear, hence harmonic, function.

Non-example: if $f(w_1, w_2, \zeta) = \overline{w_1}$, which is not holomorphic, the function $\oint_C \overline{A(x, \zeta)}\, d\zeta$ is not covered by the definition, and the chain rule computation above fails.
