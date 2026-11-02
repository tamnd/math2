---
tag: HZ5J8GGS16
kind: statement
role: proposition
name: Associativity of convolution
msc: [44A35, 42A85]
uses: [2Z29JN3VES, SASP14MA1Z, 0R0T1VWH5X, 067SYD2J4B]
about: [2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Statement

Let $n \ge 1$, and let $f, g, h \in L^1(\R^n)$.
Then the [[convolutions|2Z29JN3VES]] $(f * g) * h$ and $f * (g * h)$ are both defined almost everywhere, they lie in [[$L^1(\R^n)$|SASP14MA1Z]], and
$$(f * g) * h = f * (g * h)$$
almost everywhere.

## Remarks

Both sides are formally the double integral $\iint f(y) g(z - y) h(x - z) \, dy \, dz$.
[[Tonelli's theorem|067SYD2J4B]] shows that $\iiint \abs{f(y) g(z - y) h(x - z)} \, dy \, dz \, dx = \norm{f}_1 \norm{g}_1 \norm{h}_1 < \infty$, so the double integral converges absolutely for almost every $x$.
[[Fubini's theorem|0R0T1VWH5X]] then allows the order of integration to be swapped, and the substitution $z = y + w$ turns one side into the other.

Example: on $\R$ with $f = g = h = \mathbf{1}_{[0, 1]}$, both sides equal the convolution of the tent function $\mathbf{1}_{[0,1]} * \mathbf{1}_{[0,1]}$ with $\mathbf{1}_{[0, 1]}$, a piecewise quadratic spline supported on $[0, 3]$.

Integrability matters.
Take $f = 1$, $g = \mathbf{1}_{[0,1]} - \mathbf{1}_{[1,2]}$ and $h = \mathbf{1}_{[0,\infty)}$ on $\R$; only $g$ is integrable.
Then $f * g = \int_\R g = 0$, so $(f * g) * h = 0$.
But $g * h$ is the tent function equal to $x$ on $[0, 1]$, to $2 - x$ on $[1, 2]$ and to $0$ elsewhere, so $f * (g * h) = 1$.

## Explanations

### L1 human

When you convolve three functions, you may first combine the first two or the last two.
The result is the same.
So an expression like $f * g * h$ needs no brackets.

### L2 human

Associativity makes $L^1(\R^n)$ an associative algebra under convolution, in fact a commutative Banach algebra.
It lets one define [[convolution powers|JGR1E7Q9KQ]] $f^{*k}$ without brackets.
In probability it says that the distribution of $X + Y + Z$ for independent $X, Y, Z$ does not depend on how the sum is grouped.
