---
tag: SRN4T2G6AM
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

The direct way from $0$ to $x + y$ is never longer than the way through $x$, and this makes the length of an inner product space a true norm.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{x} = \sqrt{\ip{x}{x}}$.

1. For all $x, y \in V$, we have $\norm{x + y} \leq \norm{x} + \norm{y}$.
2. Equality holds if and only if $y = 0$ or $x = cy$ for a real number $c \geq 0$.
3. The induced norm is a [[norm|08NYZ2FS6B]] on $V$, and $d(x, y) = \norm{x - y}$ is a [[metric|063W5JMY85]] on $V$.

The [[proof|28BX20QZXM]] derives part 1 from the [[Cauchy-Schwarz inequality|0RFWW56Y22]].

## Remarks

### A first check in the plane

Take $x = (3, 0)$ and $y = (0, 4)$ in $\mathbb{R}^2$ with the dot product.
The sum is $(3, 4)$, and
$$\norm{x + y} = \sqrt{9 + 16} = 5 < 7 = 3 + 4 = \norm{x} + \norm{y}.$$
The gap of $2$ is the price of the corner at $x$.
Now take $y = (6, 0)$, which points the same way as $x$.
Then $\norm{x + y} = 9 = 3 + 6$, and the inequality becomes an equality, as part 2 predicts with $c = \tfrac12$.

### Why each hypothesis is needed

The equality case needs a norm that comes from an inner product.
For the [[maximum norm|J5V8HEYXCM]] on $\mathbb{R}^2$, the vectors $x = (1, 0)$ and $y = (1, 1)$ give
$$\norm{x + y}_\infty = \norm{(2, 1)}_\infty = 2 = 1 + 1 = \norm{x}_\infty + \norm{y}_\infty,$$
although $x$ is not a multiple of $y$.

Positivity of the inner product is needed even to define the norm.
For the [[Minkowski form|TFGECQ5C32]] $\beta(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$, the vector $(0, 1)$ has $\beta = -1$, so it has no real length $\sqrt{\beta(x, x)}$.

The factor $c$ in part 2 must be real and at least $0$.
For $x = -y \neq 0$ the left side is $0$ and the right side is $2\norm{y}$.
In $\mathbb{C}$ with $x = 1$ and $y = i$, the numbers are dependent over $\mathbb{C}$, but $\abs{1 + i} = \sqrt{2} < 2$.

### What it gives you

Every norm satisfies the reverse triangle inequality $\big|\norm{x} - \norm{y}\big| \leq \norm{x - y}$, which the page on the [[triangle inequality for norms|0FJZMBX0ZZ]] proves.
It says that the norm moves by at most $\norm{x - y}$ when the vector moves from $y$ to $x$, so the norm is a continuous function on $V$.
Induction on $n$ extends part 1 to $n$ vectors:
$$\norm{x_1 + \dots + x_n} \leq \norm{x_1} + \dots + \norm{x_n}.$$
Part 3 makes every inner product space a metric space, so limits, continuity and closeness make sense in spaces of polynomials and matrices as well as in $\mathbb{R}^n$.

### The converse

Every norm satisfies the triangle inequality, so the inequality alone cannot tell which norms come from inner products.
The [[parallelogram law|026HPGYGS4]] can, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].
The equality case is more selective.
For an inner product norm it holds only when $x$ and $y$ lie on one ray from $0$, while the maximum norm has equality for the independent pair above.

### Generalizations

In a general normed space the triangle inequality is an axiom.
For the $p$-norms on $\mathbb{R}^n$ it is the Minkowski inequality, which the topic on [[Cauchy-Schwarz, Hölder and Minkowski inequalities|MEY67W00T7]] treats.
In a [[Hilbert space|HM2HHE3J51]] the same proof works without change, since it uses only the axioms of an inner product.

## History

Euclid proved the plane version in the *Elements*, Book I, Proposition 20: in a triangle, any two sides together are longer than the third side.

## Explanations

### L1 human

A straight path is never longer than a path with a corner.
If you walk along the arrow $x$ and then along $y$, you arrive at the tip of $x + y$.
The direct distance is $\norm{x + y}$, and the walk has length $\norm{x} + \norm{y}$.
For $(3, 0)$ and $(0, 4)$ the direct distance is $5$ and the walk is $7$.
The two are equal only when both arrows point the same way.

### L2 human

Here is a check in a space of functions.
On polynomials, use $\ip{p}{q} = \int_0^1 p(t) q(t) \, dt$, and take $p = 1$ and $q = t$.
First compute the two lengths:
$$\norm{p}^2 = \int_0^1 1 \, dt = 1, \qquad \norm{q}^2 = \int_0^1 t^2 \, dt = \frac13,$$
so $\norm{p} = 1$ and $\norm{q} = 1/\sqrt{3} \approx 0.577$.
Then expand the length of the sum:
$$\norm{1 + t}^2 = \int_0^1 (1 + 2t + t^2) \, dt = 1 + 1 + \frac13 = \frac73,$$
so $\norm{1 + t} \approx 1.528$.
Since $1.528 < 1.577$, the inequality is strict, as it must be, because $t$ is not a multiple of $1$.
For $q = 2$ instead, $\norm{1 + 2} = 3 = \norm{1} + \norm{2}$, and equality holds.
The typical use is to chain estimates: if $f$ is close to $g$ and $g$ is close to $h$, then $f$ is close to $h$.

Watch out over $\mathbb{C}$.
The vectors $x$ and $ix$ are dependent, but $\norm{x + ix} = \abs{1 + i}\norm{x} = \sqrt{2}\norm{x} < 2\norm{x}$ for $x \neq 0$.
Equality needs a real factor $c \geq 0$, not only dependence.

### L3 human

The triangle inequality turns each inner product space into a normed space and so into a metric space.
The equality case says that the unit ball of an induced norm is strictly convex: its boundary sphere contains no segment.
The maximum norm has a square as its unit ball, with flat sides, and that is why it has more equality cases.
The logic runs one way: the Cauchy-Schwarz inequality gives the triangle inequality, and the triangle inequality gives the norm.
The next sub-area uses this metric in the [[best approximation theorem|0MCDDSCB9Z]], which finds the closest point of a subspace.
