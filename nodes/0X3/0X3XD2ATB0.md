---
tag: 0X3XD2ATB0
kind: definition
name: Laurent series
msc: [30B10]
defines: 0GXMPDNYX3
uses: [0VARVQ9ZW1]
sources:
  - url: https://en.wikipedia.org/wiki/Laurent_series
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Laurent_series
    locator: Convergence
---

## Definition

Let $c \in \mathbb{C}$ and let $(a_n)_{n \in \mathbb{Z}}$ be complex numbers.
The Laurent series with center $c$ and coefficients $a_n$ is the series
$$\sum_{n = -\infty}^{\infty} a_n (z - c)^n$$
in the complex variable $z$.
It converges at a point $z \neq c$ if both series $\sum_{n \ge 0} a_n (z - c)^n$ and $\sum_{n \ge 1} a_{-n} (z - c)^{-n}$ converge. Its sum at $z$ is then the sum of the two limits.

## Remarks

A [[power series|0VARVQ9ZW1]] is a Laurent series with $a_n = 0$ for each $n < 0$.
If the series converges on a nonempty open set, then it converges absolutely on an [[annulus|0AJ0YVK743]] $r < |z - c| < R$, and uniformly on each smaller closed annulus.
For example, $e^{1/z} = \sum_{n \ge 0} \frac{1}{n!} z^{-n}$ for each $z \neq 0$.
The part with negative powers is the [[principal part|0NDV5R6Z6X]].

## Explanations

### L1 human

A Laurent series is like a power series, but it can also have negative powers of $z - c$.
The negative powers allow it to describe functions that blow up at $c$, such as $1/z$ or $e^{1/z}$.
