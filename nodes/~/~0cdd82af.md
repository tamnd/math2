---
tag: ~0cdd82af
kind: statement
role: theorem
name: Triangle inequality for the induced norm
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0MFJJV97RJ]
uses: [0RFWW56Y22, 0KG4D8AP6G, 08NYZ2FS6B, 063W5JMY85]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Norm properties
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Statement

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{x} = \sqrt{\ip{x}{x}}$.

1. For all $x, y \in V$, $\norm{x + y} \leq \norm{x} + \norm{y}$.
2. Equality holds if and only if $y = 0$ or $x = cy$ for a real number $c \geq 0$.
3. The induced norm is a [[norm|08NYZ2FS6B]] on $V$, and $d(x, y) = \norm{x - y}$ is a [[metric|063W5JMY85]] on $V$.

The [[proof|~a7229cf0]] derives part 1 from the [[Cauchy-Schwarz inequality|0RFWW56Y22]].

## Remarks

### Why each hypothesis is needed

- The norm must come from an inner product for the equality case. For the [[maximum norm|~4a30dace]] on $\mathbb{R}^2$, $x = (1, 0)$ and $y = (1, 1)$ give $\norm{x + y}_\infty = 2 = \norm{x}_\infty + \norm{y}_\infty$, although $x$ is not a multiple of $y$.
- Positivity of the inner product is needed. For the [[Minkowski form|TFGECQ5C32]] there is no real "norm" $\sqrt{\beta(x, x)}$ at $x = (0, 1)$, since $\beta(x, x) = -1$.
- The constant $c$ in part 2 must be real and nonnegative. For $x = -y \neq 0$, the left side is $0$ and the right side is $2\norm{y}$. In $\mathbb{C}$, $x = 1$ and $y = i$ give $|1 + i| = \sqrt{2} < 2$.

### Consequences

- The reverse triangle inequality $\big|\norm{x} - \norm{y}\big| \leq \norm{x - y}$ follows, as for every norm. The theorem on [[triangle inequality for norms|0FJZMBX0ZZ]] proves it.
- The norm is continuous on $V$, by the reverse triangle inequality.
- For $n$ vectors, $\norm{x_1 + \dots + x_n} \leq \norm{x_1} + \dots + \norm{x_n}$, by induction on $n$.
- In $\mathbb{R}^n$ with the dot product, the sum of two sides of a triangle is at least the third side.

### Converse

The inequality holds for every norm, so it does not characterize the norms that come from inner products.
The [[parallelogram law|026HPGYGS4]] does characterize them, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].
The equality case is special to inner product norms and other strictly convex norms.
For the maximum norm, equality holds for some independent pairs, as above.

### Generalizations

- In every normed space the inequality is an axiom. For the $p$-norms on $\mathbb{R}^n$ it is the Minkowski inequality, which the topic [[Cauchy-Schwarz, Hölder and Minkowski inequalities|MEY67W00T7]] treats.
- In a [[Hilbert space|HM2HHE3J51]] the same proof works without change.

## Explanations

### L1 human

A straight path is never longer than a path with a corner.
If we walk along the vector $x$ and then along $y$, we arrive at $x + y$.
The direct distance $\norm{x + y}$ is at most the length $\norm{x} + \norm{y}$ of the two walks.
For $x = (3, 0)$ and $y = (0, 4)$ in the plane, the direct distance is $5$, and the two walks have length $7$.
The two are equal only when both walks go in the same direction.

### L2 human

Worked example: we check the inequality for polynomials with $\ip{p}{q} = \int_0^1 p(t) q(t) \, dt$.

1. Let $p = 1$ and $q = t$. Then $\norm{p} = 1$ and $\norm{q} = 1/\sqrt{3} \approx 0.577$.
2. The sum is $1 + t$, with $\norm{1 + t}^2 = 1 + 2 \cdot \frac12 + \frac13 = \frac73$, so $\norm{1 + t} \approx 1.528$.
3. Since $1.528 \leq 1 + 0.577 = 1.577$, the inequality holds, and it is strict, because $t$ is not a multiple of $1$.
4. For $q = 2$, a nonnegative multiple of $p$, we get $\norm{1 + 2} = 3 = \norm{1} + \norm{2}$, so equality holds.

The typical use is to bound an error.
If $f$ is close to $g$ and $g$ is close to $h$, then $f$ is close to $h$.
A trap: over $\mathbb{C}$, equality needs a real nonnegative factor.
The vectors $x$ and $ix$ are dependent, but $\norm{x + ix} = \sqrt{2}\norm{x} < 2\norm{x}$ for $x \neq 0$.

### L3 human

The triangle inequality makes the induced norm a norm, so each inner product space is a normed space and a metric space.
The equality case says that the unit ball of an induced norm is strictly convex: its boundary contains no segment.
Every norm satisfies the inequality, but only the norms that satisfy the parallelogram law come from inner products.
The maximum norm is a norm whose unit ball has flat sides.
The chain of results is one way: the Cauchy-Schwarz inequality gives the triangle inequality, and the triangle inequality gives the norm.
