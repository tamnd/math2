---
tag: J5V8HEYXCM
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

On $\mathbb{R}^2$ let $\norm{x}_\infty = \max(\abs{x_1}, \abs{x_2})$, the maximum norm.
We show that it is a [[norm|08NYZ2FS6B]], and that no inner product induces it.

1. Homogeneity holds, since $\max(\abs{ax_1}, \abs{ax_2}) = \abs{a}\max(\abs{x_1}, \abs{x_2})$.
   Definiteness holds, since the maximum is $0$ only if $x_1 = x_2 = 0$.
2. The triangle inequality holds, because for $k = 1, 2$ we have
$$\abs{x_k + y_k} \leq \abs{x_k} + \abs{y_k} \leq \norm{x}_\infty + \norm{y}_\infty,$$
   and the maximum over $k$ of the left side is $\norm{x + y}_\infty$.
3. Now take $x = (1, 0)$ and $y = (0, 1)$, so that $\norm{x}_\infty = \norm{y}_\infty = 1$.
4. The diagonals are $x + y = (1, 1)$ and $x - y = (1, -1)$, so $\norm{x + y}_\infty = \norm{x - y}_\infty = 1$.
5. The two sides of the [[parallelogram law|026HPGYGS4]] are
$$\norm{x + y}_\infty^2 + \norm{x - y}_\infty^2 = 1 + 1 = 2, \qquad 2\norm{x}_\infty^2 + 2\norm{y}_\infty^2 = 2 + 2 = 4.$$
6. Every norm induced by an inner product satisfies the parallelogram law.
   Since $2 \neq 4$, no inner product on $\mathbb{R}^2$ induces $\norm{\cdot}_\infty$.

## Remarks

A norm, even a simple one, need not come from an inner product.
The picture explains why.
The unit ball of $\norm{\cdot}_\infty$ is the square $[-1, 1]^2$, with flat sides and corners, while the unit ball of an induced norm on $\mathbb{R}^2$ is an ellipse.

The failure does not depend on the size of the space, as long as there are two coordinates.
On $\mathbb{R}^n$ with $n \geq 2$, the vectors $e_1$ and $e_2$ break the law in the same way.
On $\mathbb{R}^1$ the maximum norm is $\abs{x}$, which the inner product $xy$ induces, so the example needs dimension at least $2$.

The sup norm $\max_{t \in [0, 1]} \abs{f(t)}$ on continuous functions fails in the same way.
For $f(t) = t$ and $g(t) = 1 - t$, the functions $f$, $g$, $f + g = 1$ and $f - g = 2t - 1$ all have sup norm $1$, so again the law would need $2 = 4$.

## Explanations

### L1 human

The maximum norm measures a vector by its largest coordinate, ignoring signs.
For the vectors $(1, 0)$ and $(0, 1)$, the sum $(1, 1)$ and the difference $(1, -1)$ both have size $1$.
In the usual picture of the plane, the diagonals of the unit square have length $\sqrt{2}$, not $1$.
The parallelogram law notices the difference: $1 + 1$ is not $2 + 2$.

### L2 human

To test whether a norm comes from an inner product, try the parallelogram law on simple vectors.
Take two basis vectors, compute the four norms $\norm{x + y}$, $\norm{x - y}$, $\norm{x}$ and $\norm{y}$, and compare $\norm{x + y}^2 + \norm{x - y}^2$ with $2\norm{x}^2 + 2\norm{y}^2$.
For the maximum norm and $e_1, e_2$ the comparison is $2$ against $4$, so the norm is not induced.
The typical use is to show that a normed space, such as the continuous functions with the sup norm, is not an inner product space.

Watch out: a pair that satisfies the law proves nothing.
For $x = (1, 0)$ and $y = (2, 0)$ the maximum norm gives
$$\norm{(3, 0)}_\infty^2 + \norm{(-1, 0)}_\infty^2 = 9 + 1 = 10 = 2 \cdot 1 + 2 \cdot 4.$$
On the line through $e_1$ the maximum norm is just the absolute value, so the law holds there.
