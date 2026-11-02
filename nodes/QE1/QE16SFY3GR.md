---
tag: QE16SFY3GR
kind: definition
name: Finite difference coefficients
msc: [65D25, 65N06]
defines: 752Z7DRT7P
uses: [NVH3F8FTYS, Q3JWBZ7EFY, 03QHBVW4TT]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference_coefficient
---

## Definition

Let $m \ge 0$ and $N \ge m + 1$ be integers, and let $s_1, \ldots, s_N$ be distinct real numbers, the *stencil*.
The *finite difference coefficients* for the $m$-th derivative on this stencil are the real numbers $a_1, \ldots, a_N$ that solve
$$\sum_{j=1}^{N} a_j \, s_j^{\,i} = \begin{cases} m! & \text{if } i = m, \\ 0 & \text{if } i \ne m, \end{cases} \qquad i = 0, 1, \ldots, N - 1.$$
The associated formula is $f^{(m)}(x) \approx h^{-m} \sum_{j=1}^{N} a_j f(x + s_j h)$ for a step $h > 0$.

## Remarks

The matrix of the system is a [[Vandermonde matrix|Q3JWBZ7EFY]] in the distinct numbers $s_j$, so the coefficients exist and are unique.
Expanding $f(x + s_j h)$ by [[Taylor's theorem|03QHBVW4TT]] up to order $N - 1$ shows that for $f \in C^N$ the formula has error $O(h^{N - m})$; for symmetric stencils the order is often one higher.
Example: $m = 1$ and the forward stencil $0, 1, 2$ give $a = (-\tfrac32, 2, -\tfrac12)$.
Check: $\sum a_j = 0$, $\sum a_j s_j = 2 - 1 = 1 = 1!$, and $\sum a_j s_j^2 = 2 - 2 = 0$.
So $f'(x) \approx \frac{-3 f(x) + 4 f(x+h) - f(x+2h)}{2h}$, with error $O(h^2)$.
Non-example: for $m = 2$ the weights $(1, -2, 1)$ on the stencil $0, 1, 3$ are not the coefficients, since $\sum a_j s_j = -2 + 3 = 1 \ne 0$; the correct ones there are $(\tfrac23, -1, \tfrac13)$.

## Explanations

### L1 human

The weighted sum of the samples cancels every term of the Taylor expansion except the wanted derivative.
It does so up to the degree that the number of points allows.
More points give more cancellations and a more accurate formula.
