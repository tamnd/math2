---
tag: 0YK27TJ4WF
kind: definition
name: Order of a pole
msc: [30D30]
defines: 073MWACF1K
uses: [0WPQYW8MTE, 064N002TX4]
sources:
  - url: https://en.wikipedia.org/wiki/Zeros_and_poles
    locator: Definitions
---

## Definition

Let $c$ be a [[pole|0WPQYW8MTE]] of $f$.
The order of the pole $c$ is the unique integer $m \ge 1$ with the following property. On some punctured disc $0 < |z - c| < \delta$,
$$f(z) = \frac{g(z)}{(z - c)^m},$$
where $g$ is [[holomorphic|0DG0Z72CQD]] on the disc $|z - c| < \delta$ and $g(c) \neq 0$.
A pole of order $1$ is a simple pole.

## Remarks

The order of the pole of $f$ at $c$ is the [[order of the zero|064N002TX4]] of $1/f$ at $c$.
In the Laurent series $\sum a_n (z - c)^n$ of $f$ at $c$, the order is $m$ if and only if $a_{-m} \neq 0$ and $a_n = 0$ for each $n < -m$.
Many authors give a pole of order $m$ the signed order $-m$. Then zeros have positive order and poles have negative order.
For example, $\frac{1}{\sin^2 z}$ has a pole of order $2$ at each point $k\pi$ with $k \in \mathbb{Z}$.

## Explanations

### L1 human

The order of a pole says how fast the function goes to infinity at the point.
Near a pole of order $m$, the function behaves like a constant times $1/(z - c)^m$.
