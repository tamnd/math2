---
tag: BQJ9C1CD5X
kind: statement
role: theorem
name: Mean value theorem for divided differences
msc: [65D05, 41A05, 26A24]
uses: [N5ZHV4HWDC, 0194DY35BG, 0V1EJCT8G6, SS1YMS2NPC]
about: [N5ZHV4HWDC]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem_(divided_differences)
same_as:
  wikidata: Q17098096
  wikipedia: Mean value theorem (divided differences)
---

## Statement

Let $n \ge 1$, let $I \subseteq \R$ be an open interval, and let $f \colon I \to \R$ be $n$ times differentiable.
Let $x_0, \dots, x_n \in I$ be pairwise distinct, and let $m$ and $M$ be the smallest and largest of them.
Then there is $\xi \in (m, M)$ such that
$$f[x_0, \dots, x_n] = \frac{f^{(n)}(\xi)}{n!},$$
where $f[x_0, \dots, x_n]$ is the [[divided difference|N5ZHV4HWDC]].

## Remarks

Let $p$ be the [[interpolation polynomial|SS1YMS2NPC]] of $f$ at the nodes.
Then $g = f - p$ has $n + 1$ distinct zeros in $[m, M]$.
Applying [[Rolle's theorem|0194DY35BG]] $n$ times gives a point $\xi \in (m, M)$ with $g^{(n)}(\xi) = 0$.
Since $p^{(n)}$ is the constant $n! \, f[x_0, \dots, x_n]$, the claim follows.

For $n = 1$ this is the [[mean value theorem|0BARQY52N5]].
Example: for $f(x) = x^3$ and the nodes $0, 1, 2$, one has $f[0, 1] = 1$, $f[1, 2] = 7$ and $f[0, 1, 2] = 3$.
Since $f''(\xi)/2 = 3\xi$, the theorem holds with $\xi = 1$.

## Explanations

### L1 human

The ordinary mean value theorem says that the slope of a chord equals the slope of the tangent somewhere in between.
This theorem says the same thing one level up: a higher divided difference equals a scaled higher derivative at some point between the nodes.

### L2 human

It turns statements about derivatives into statements about divided differences and back.
For example, if $f^{(n)} \ge 0$ on $I$, then every $n$-th divided difference of $f$ is nonnegative.
Combined with the [[Newton form|9W77FPTM9E]] of the interpolation polynomial, it gives the [[interpolation error formula|HASA2XSG66]].
