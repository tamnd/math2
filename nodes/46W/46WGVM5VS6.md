---
tag: 46WGVM5VS6
kind: statement
role: theorem
name: Jordan–von Neumann theorem
msc: [46C15, 39B52]
uses: [03J5RAKB30, 0QVNCJXRY3, 0MFJJV97RJ]
about: [0QVNCJXRY3, 03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelogram_law
---

## Statement

Let $\mathbb{K}$ be $\R$ or $\C$, and let $(V, \norm{\cdot})$ be a [[normed vector space|03J5RAKB30]] over $\mathbb{K}$.
Then the following are equivalent.

1. There is an inner product $\ip{\cdot}{\cdot}$ on $V$ whose [[induced norm|0MFJJV97RJ]] is $\norm{\cdot}$, that is, $\norm{x}^2 = \ip{x}{x}$ for all $x \in V$.
2. The norm satisfies the parallelogram law: $\norm{x + y}^2 + \norm{x - y}^2 = 2 \norm{x}^2 + 2 \norm{y}^2$ for all $x, y \in V$.

When these hold, the inner product is unique and is given by the polarization identity.
For $\mathbb{K} = \R$ it is
$$\ip{x}{y} = \frac{1}{4} \left( \norm{x + y}^2 - \norm{x - y}^2 \right),$$
and for $\mathbb{K} = \C$, with $\ip{\cdot}{\cdot}$ linear in the first argument, it is
$$\ip{x}{y} = \frac{1}{4} \sum_{k=0}^{3} i^k \norm{x + i^k y}^2.$$

## Remarks

The direction from 1 to 2 is the [[parallelogram law|026HPGYGS4]] in an [[inner product space|0QVNCJXRY3]].
For the converse in the real case, define $\ip{x}{y}$ by the polarization formula.
Symmetry and $\ip{x}{x} = \norm{x}^2$ are immediate.
The parallelogram law gives $\ip{x + x'}{y} = \ip{x}{y} + \ip{x'}{y}$, so $t \mapsto \ip{tx}{y}$ is an [[additive function|KF719SZD5T]] of $t \in \R$.
It is continuous, because the norm is continuous, so it equals $t \ip{x}{y}$.
The norm $\abs{x_1} + \abs{x_2}$ on $\R^2$ fails the parallelogram law for $x = (1, 0)$, $y = (0, 1)$, since $4 + 4 \ne 2 + 2$, so it comes from no inner product.

## Explanations

### L1 human

Some ways of measuring length come from an inner product, which also measures angles, and some do not.
This theorem gives a simple test: a length comes from an inner product exactly when it obeys the parallelogram law.
So one identity about four sides and two diagonals decides whether the space has a full Euclidean geometry.

### L2 human

The theorem shows that among the spaces $L^p([0, 1])$ with $1 \le p \le \infty$, only $L^2([0, 1])$ has a norm that comes from an inner product.
For $p \ne 2$ the parallelogram law fails for the indicator functions of $[0, 1/2]$ and $(1/2, 1]$.
It is a characterization of Hilbert spaces among Banach spaces, because completeness is not affected.
The proof is a functional equation argument: the parallelogram law is the [[quadratic functional equation|7MZGZFQ347]] for $f(x) = \norm{x}^2$, and continuity turns additivity into linearity.
The law only involves two vectors at a time, so a norm is an inner product norm as soon as its restriction to every two-dimensional subspace is.
