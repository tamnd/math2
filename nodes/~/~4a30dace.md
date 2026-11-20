---
tag: ~4a30dace
kind: example
name: The maximum norm on R2 does not come from an inner product
msc: ["46C05", "46B20"]
topics: [1D4JTZ9VS3]
audience: ug1
not_instance_of:
  - target: 0MFJJV97RJ
    note: the maximum norm on R^2 fails the parallelogram law at x = (1, 0), y = (0, 1), so no inner product induces it
  - target: 0QVNCJXRY3
    note: the normed space (R^2, maximum norm) carries no inner product whose induced norm is the maximum norm
uses: [08NYZ2FS6B, 026HPGYGS4]
sources:
  - url: https://en.wikipedia.org/wiki/Norm_(mathematics)
    locator: "Maximum norm (special case of: infinity norm, uniform norm, or supremum norm)"
  - url: https://en.wikipedia.org/wiki/Parallelogram_law
    locator: Normed vector spaces satisfying the parallelogram law
---

## Example

On $\mathbb{R}^2$ let $\norm{x}_\infty = \max(|x_1|, |x_2|)$, the maximum norm.
It is a [[norm|08NYZ2FS6B]], but we show that no inner product induces it.

1. The norm axioms hold. Homogeneity: $\max(|ax_1|, |ax_2|) = |a|\max(|x_1|, |x_2|)$. Definiteness: the maximum is $0$ only if $x_1 = x_2 = 0$.
2. The triangle inequality holds, because $|x_k + y_k| \leq |x_k| + |y_k| \leq \norm{x}_\infty + \norm{y}_\infty$ for $k = 1, 2$.
3. Let $x = (1, 0)$ and $y = (0, 1)$. Then $\norm{x}_\infty = \norm{y}_\infty = 1$.
4. We have $x + y = (1, 1)$ and $x - y = (1, -1)$, so $\norm{x + y}_\infty = \norm{x - y}_\infty = 1$.
5. The left side of the [[parallelogram law|026HPGYGS4]] is $1^2 + 1^2 = 2$, and the right side is $2 \cdot 1^2 + 2 \cdot 1^2 = 4$.
6. Every norm induced by an inner product satisfies the parallelogram law. Since $2 \neq 4$, no inner product on $\mathbb{R}^2$ induces $\norm{\cdot}_\infty$.

## Remarks

The example shows that a norm, even a simple one, need not come from an inner product.
The unit ball of $\norm{\cdot}_\infty$ is the square $[-1, 1]^2$, with flat sides, while the unit ball of an induced norm is an ellipse.
On $\mathbb{R}^n$ for any $n \geq 2$, the vectors $e_1$ and $e_2$ break the law in the same way.
On $\mathbb{R}^1$ the maximum norm is $|x|$, which the inner product $xy$ induces, so the example needs dimension at least $2$.
The sup norm $\max_{t \in [0, 1]} |f(t)|$ on continuous functions fails the law in the same way, for example with $f(t) = t$ and $g(t) = 1 - t$.

## Explanations

### L1 human

The maximum norm measures a vector by its largest coordinate, in absolute value.
For the vectors $(1, 0)$ and $(0, 1)$, the sum $(1, 1)$ and the difference $(1, -1)$ both have size $1$.
In a true Euclidean picture, the diagonals of the unit square have length $\sqrt{2}$, not $1$.
The parallelogram law detects this: $1 + 1$ is not $2 + 2$.

### L2 human

To test whether a norm comes from an inner product, try the parallelogram law on simple vectors.

1. Take two basis vectors, here $x = (1, 0)$ and $y = (0, 1)$.
2. Compute the four norms $\norm{x + y}$, $\norm{x - y}$, $\norm{x}$ and $\norm{y}$.
3. Compare $\norm{x + y}^2 + \norm{x - y}^2$ with $2\norm{x}^2 + 2\norm{y}^2$. Here $2 \neq 4$, so the norm is not induced.

The typical use is to show that a normed space, such as the continuous functions with the sup norm, is not an inner product space.
A trap: a pair that satisfies the law proves nothing.
For $x = (1, 0)$ and $y = (2, 0)$ the maximum norm gives $9 + 1 = 10 = 2 + 8$.
