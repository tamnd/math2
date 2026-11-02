---
tag: CCPS738AH8
kind: statement
role: theorem
name: Haar's uniqueness theorem
msc: [41A52, 41A50]
uses: [NY5AK617TR, 7N4988HN3P, XAARVNKXF1, 0TVJZYB6SH, 0S1FJ8VEX9]
about: [NY5AK617TR, 7N4988HN3P]
sources:
  - url: https://en.wikipedia.org/wiki/Equioscillation_theorem
---

## Statement

Let $K$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]] with at least $n$ points.
Let $C(K)$ be the space of continuous functions $K \to \R$ with the supremum norm.
Let $V \subseteq C(K)$ be a linear subspace of dimension $n \ge 1$.
Then the following are equivalent.

1. Every $f \in C(K)$ has exactly one [[best approximation|7N4988HN3P]] from $V$ in the supremum norm.
2. $V$ is a Haar subspace: every basis of $V$ is a [[Chebyshev system|NY5AK617TR]], that is, every nonzero $v \in V$ has at most $n - 1$ zeros in $K$.

## Remarks

The idea of the proof: best approximations always exist, since $V$ is finite-dimensional.
If $V$ is Haar and $v_1, v_2$ are both best, then so is $(v_1 + v_2)/2$.
Its error attains the norm only at points where $v_1 - v_2$ vanishes.
For a Haar subspace the error of a best approximation attains its norm at $n + 1$ or more points, too many zeros for $v_1 - v_2 \ne 0$.
Conversely, if a nonzero $v \in V$ vanishes at $n$ points, one builds a continuous $f$ that has $0$ and all small multiples of a suitable element of $V$ as best approximations.

Example: the polynomials of degree at most $n - 1$ on $[a, b]$ form a Haar subspace, so best [[uniform approximation|XAARVNKXF1]] of a continuous function by polynomials of a fixed degree is unique.

Non-example: on $[-1, 1]$, the span of $1$ and $x^2$ is not Haar, since $x^2 - 1$ has two zeros.
Correspondingly $f(x) = x$ has many best approximations from it.
For every $g = a + c x^2$, the error $x - g$ takes the values $1 - a - c$ and $-1 - a - c$ at $\pm 1$, which differ by $2$, so $\norm{x - g}_\infty \ge 1$.
For $\abs{c} \le 1/2$, the error $h(x) = x - c(x^2 - 1)$ has $h' = 1 - 2cx \ge 0$ on $[-1, 1]$ and $h(\pm 1) = \pm 1$, so $\norm{h}_\infty = 1$.
Hence every $c(x^2 - 1)$ with $\abs{c} \le 1/2$ is a best approximation of $x$.

## Explanations

### L1 human

In the uniform norm, best approximations are not always unique.
Haar's theorem says exactly when they are: when no nonzero function of the approximating space has too many zeros.
Polynomials of a fixed degree pass this test, which is why the best uniform polynomial approximation is unique.

### L2 human

The theorem explains the special role of polynomials and of Chebyshev systems in uniform approximation.
For Haar subspaces the best approximation is characterized by alternation of the error at $n + 1$ points, which generalizes the equioscillation theorem.
The Mairhuber–Curtis theorem shows that Haar subspaces of dimension at least $2$ do not exist on open sets in several variables.
So best uniform approximation by multivariate polynomials of a fixed degree is not always unique.
