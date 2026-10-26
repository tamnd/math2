---
tag: 0J8T4K4YTE
kind: statement
role: theorem
name: Taylor's theorem in several variables
aliases: [multivariate-taylor-theorem]
msc: [26B12]
uses: [0TCBZMEYGN, 02RSXVM1ZN, 0PJXBR6QA3]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Taylor's theorem for multivariate functions
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Derivation for the remainder of multivariate Taylor polynomials
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $k \ge 1$ be an integer, and let $f \colon U \to \mathbb{R}$ be of [[class C^k|0TCBZMEYGN]] on $U$.
Let $a \in U$.
For a [[multi-index|0PJXBR6QA3]] $\alpha = (\alpha_1, \dots, \alpha_n)$, write $|\alpha| = \alpha_1 + \dots + \alpha_n$, $\alpha! = \alpha_1! \cdots \alpha_n!$, $h^\alpha = h_1^{\alpha_1} \cdots h_n^{\alpha_n}$, and $D^\alpha f = \partial^{|\alpha|} f / \partial x_1^{\alpha_1} \cdots \partial x_n^{\alpha_n}$.
Then
$$f(a + h) = \sum_{|\alpha| \le k} \frac{D^\alpha f(a)}{\alpha!} \, h^\alpha + R_k(h), \qquad \lim_{h \to 0} \frac{R_k(h)}{\|h\|^k} = 0.$$
If $f$ is of class $C^{k+1}$ and the segment from $a$ to $a + h$ lies in $U$, then
$$R_k(h) = \sum_{|\beta| = k + 1} \frac{k + 1}{\beta!} \, h^\beta \int_0^1 (1 - t)^k \, D^\beta f(a + t h) \, dt.$$

## Remarks

The sum over $|\alpha| \le k$ is the Taylor polynomial of order $k$ of $f$ at $a$.
For $k = 1$ the statement says that $f$ is differentiable at $a$, with $f(a + h) = f(a) + \nabla f(a) \cdot h + o(\|h\|)$.
One proof applies the one-variable Taylor theorem to $g(t) = f(a + t h)$ on $[0, 1]$, together with the chain rule.
The case $k = 2$ is the [[second-order Taylor expansion|0P30YYZN85]].

## Explanations

### L1 human

Near a point, a smooth function of several variables looks like a polynomial in the displacement $h$.
The coefficients of that polynomial are the partial derivatives at the point, divided by factorials.
The error is smaller than $\|h\|^k$, so the approximation gets better quickly as $h$ shrinks.
