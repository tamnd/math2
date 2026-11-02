---
tag: ZMT8JF21R6
kind: example
name: Runge's phenomenon
msc: [41A05, 65D05]
illustrates: [SS1YMS2NPC]
uses: [HASA2XSG66, HYK8J56PSH, 08VZ57PT26]
sources:
  - url: https://en.wikipedia.org/wiki/Runge%27s_phenomenon
same_as:
  wikidata: Q1990319
  wikipedia: Runge's phenomenon
---

## Example

Let $f(x) = \dfrac{1}{1 + 25 x^2}$ on $[-1, 1]$.
For $n \ge 1$ let $p_n$ be the [[interpolation polynomial|SS1YMS2NPC]] of degree at most $n$ of $f$ at the equally spaced nodes $x_i = -1 + 2i/n$, $i = 0, \dots, n$.
Then
$$\max_{x \in [-1, 1]} \abs{f(x) - p_n(x)} \to \infty \quad \text{as } n \to \infty.$$
The error stays small in the middle of the interval but grows without bound near the end points, where $p_n$ oscillates more and more.

The function $f$ is smooth, in fact analytic on all of $\R$, so the failure is not due to a lack of differentiability.
The [[interpolation error formula|HASA2XSG66]] explains it.
The derivatives $f^{(n+1)}$ grow roughly like $(n + 1)! \, 5^{n+1}$ on $[-1, 1]$, because $f$ has complex poles at $\pm i/5$, close to the interval.
This growth outweighs the factor $\frac{1}{(n+1)!} \max \abs{\prod_i (x - x_i)}$ for equally spaced nodes, which is largest near the end points.

With [[Chebyshev nodes|HYK8J56PSH]] instead of equally spaced nodes, the interpolation polynomials of the same $f$ converge [[uniformly|08VZ57PT26]] to $f$ on $[-1, 1]$.

## Explanations

### L1 human

One might think that fitting a polynomial through more and more points of a nice curve always gives a better and better fit.
Runge's example shows that this is false.
For a simple bell-shaped curve and equally spaced points, the fitted polynomial develops wild wiggles near the ends of the interval.
The wiggles get bigger as more points are used.
The cure is to put more points near the ends, as Chebyshev nodes do, or to use piecewise polynomials such as [[splines|84TJ8KQ926]].
