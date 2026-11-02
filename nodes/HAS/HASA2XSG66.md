---
tag: HASA2XSG66
kind: statement
role: theorem
name: Interpolation error formula
msc: [41A05, 65D05, 41A80]
uses: [SS1YMS2NPC, 0V1EJCT8G6, 0194DY35BG]
about: [SS1YMS2NPC]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_interpolation
---

## Statement

Let $n \ge 0$, let $a < b$, and let $f \colon [a, b] \to \R$ be $n + 1$ times continuously differentiable.
Let $x_0, \dots, x_n \in [a, b]$ be pairwise distinct, and let $p$ be the [[interpolation polynomial|SS1YMS2NPC]] of degree at most $n$ with $p(x_i) = f(x_i)$ for all $i$.
Then for every $x \in [a, b]$ there is $\xi$ in the smallest closed interval that contains $x, x_0, \dots, x_n$ such that
$$f(x) - p(x) = \frac{f^{(n+1)}(\xi)}{(n + 1)!} \prod_{i=0}^{n} (x - x_i).$$

## Remarks

If $x$ is a node, both sides are $0$.
Otherwise set $\omega(t) = \prod_i (t - x_i)$ and choose the constant $c$ so that $g(t) = f(t) - p(t) - c \, \omega(t)$ vanishes at $t = x$.
Then $g$ has $n + 2$ distinct zeros, and $n + 1$ applications of [[Rolle's theorem|0194DY35BG]] give a zero $\xi$ of the [[derivative|0V1EJCT8G6]] $g^{(n+1)} = f^{(n+1)} - c \, (n + 1)!$.
This gives $c = f^{(n+1)}(\xi)/(n + 1)!$.

Example: take $f = \exp$ on $[0, 1]$ with the nodes $0$ and $1$.
At $x = 1/2$ the error of the linear interpolant is $\frac{e^{\xi}}{2} \cdot \frac{1}{2} \cdot \left(-\frac{1}{2}\right)$ for some $\xi \in [0, 1]$.
So its absolute value is at most $e/8$.

For $n = 0$ the formula is the mean value theorem.
It is the analogue of [[Taylor's theorem|03QHBVW4TT]] with the Lagrange remainder, with $n + 1$ separate points in place of one point of high contact.

## Explanations

### L1 human

When a polynomial is fitted through some points of a smooth curve, it matches the curve exactly at those points and is off somewhere else.
The formula says how far off it is.
The error is small when the curve does not bend too much, measured by a high derivative, and when the point is close to the nodes.

### L2 human

Taking the maximum over $[a, b]$ gives $\norm{f - p}_\infty \le \frac{\norm{f^{(n+1)}}_\infty}{(n + 1)!} \max_{x \in [a, b]} \abs{\omega(x)}$.
The first factor depends only on $f$, the second only on the nodes.
[[Chebyshev nodes|HYK8J56PSH]] make the second factor as small as possible on an interval.
When the derivatives of $f$ grow fast, the bound can fail to tend to $0$, which is what happens in [[Runge's phenomenon|ZMT8JF21R6]].
In terms of [[divided differences|N5ZHV4HWDC]], for $x$ not a node the error equals $f[x_0, \dots, x_n, x] \, \omega(x)$.
