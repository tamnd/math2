---
tag: X9HVQPWT6T
kind: example
name: Padua points
msc: [41A05, 41A63, 65D05]
instance_of: [5276MDSDQV]
uses: [07GNX8GCYP, 7V7KWNK9HN]
sources:
  - url: https://en.wikipedia.org/wiki/Padua_points
same_as:
  wikidata: Q7123977
  wikipedia: Padua points
---

## Example

Let $n \ge 1$ and consider the curve $\gamma \colon [0, \pi] \to [-1, 1]^2$,
$$\gamma(t) = \bigl(-\cos((n + 1) t), \ -\cos(n t)\bigr).$$
The *Padua points* of degree $n$ are the points $\gamma\bigl(k\pi / (n(n + 1))\bigr)$ for $k = 0, 1, \dots, n(n + 1)$.
These are the self-intersections of $\gamma$ together with its points on the boundary of the square.
For $n \ge 2$ several of these parameter values give the same point, and there are exactly $(n + 1)(n + 2)/2$ distinct Padua points.

This number is the dimension of the space of [[polynomials in two variables|07GNX8GCYP]] of total degree at most $n$.
The Padua points are a [[unisolvent point set|5276MDSDQV]] for this space.
So each choice of values at the Padua points is taken by exactly one polynomial of total degree at most $n$.

Check for $n = 1$: the parameters $0$, $\pi/2$, $\pi$ give the points $(-1, -1)$, $(1, 0)$, $(-1, 1)$.
They are not collinear, so they are unisolvent for the polynomials $a + bx + cy$.

The [[Lebesgue constant|7V7KWNK9HN]] of interpolation at the Padua points is $O(\log^2 n)$ as $n \to \infty$.

## Explanations

### L1 human

In one variable, Chebyshev nodes are a near-ideal choice of points for polynomial interpolation on an interval.
In the square, finding a good set of points that also gives a unique interpolating polynomial is much harder.
The Padua points solve this: they are the crossing points of a Lissajous-type curve that sweeps through the square, plus its touching points on the edges.
Interpolation at these points is unique and numerically well behaved.
