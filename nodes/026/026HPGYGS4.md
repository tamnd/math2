---
tag: 026HPGYGS4
kind: statement
role: theorem
name: Parallelogram law
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0MFJJV97RJ]
uses: [01EK923SKP, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelogram_law
    locator: The parallelogram law in inner product spaces
  - url: https://en.wikipedia.org/wiki/Parallelogram_law
    locator: Normed vector spaces satisfying the parallelogram law
  - book: isbn:9783031410253
    locator: Chapter 6
formal:
  - system: lean4
    library: mathlib
    decl: parallelogram_law_with_norm
    match: exact
same_as:
  wikidata: Q919125
  wikipedia: Parallelogram law
---

## Statement

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Then, for all $x, y \in V$,
$$\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2.$$

The [[proof|6FE43HC13F]] expands both squares.
Conversely, by the [[Jordan-von Neumann theorem|46WGVM5VS6]], a norm that satisfies this law comes from a unique inner product.

## Remarks

### Why each hypothesis is needed

The only hypothesis is that the norm comes from an inner product, and it cannot be dropped.
For the [[maximum norm on $\mathbb{R}^2$|J5V8HEYXCM]], $x = (1, 0)$ and $y = (0, 1)$ give $1 + 1 = 2$ on the left and $2 + 2 = 4$ on the right.
For the [[taxicab norm|WW2RB40VYX]] $|x_1| + |x_2|$ and the same vectors, the left side is $4 + 4 = 8$ and the right side is $4$.

### Consequences

- The maximum norm and the taxicab norm on $\mathbb{R}^2$ come from no inner product, by the computations above.
- More generally, the $p$-norm $(|x_1|^p + \dots + |x_n|^p)^{1/p}$ on $\mathbb{R}^n$ with $n \geq 2$ satisfies the law only for $p = 2$.
- Apollonius's formula for the median of a triangle follows. For the triangle with vertices $0$, $x$ and $y$, the median from $0$ is $\frac{x + y}{2}$, and $\norm{\frac{x + y}{2}}^2 = \frac{\norm{x}^2 + \norm{y}^2}{2} - \frac{\norm{x - y}^2}{4}$.
- The real polarization identity follows from the same expansion: $\norm{x + y}^2 - \norm{x - y}^2 = 4\ip{x}{y}$ over $\mathbb{R}$.

### Converse

The converse is true, and it is the [[Jordan-von Neumann theorem|46WGVM5VS6]].
If a norm on a real or complex vector space satisfies the law for all $x$ and $y$, then exactly one inner product induces it.
The [[polarization identity|05FKHRT0B4]] gives this inner product.

### Generalizations

- For $n$ vectors, the sum of $\norm{\pm x_1 \pm \dots \pm x_n}^2$ over all $2^n$ choices of signs is $2^n(\norm{x_1}^2 + \dots + \norm{x_n}^2)$, because all mixed terms cancel.
- In a [[Hilbert space|HM2HHE3J51]] the law holds with the same proof. It is the main step of the proof that a closed convex set has a unique closest point.

## History

The theorem is named after the parallelogram of plane geometry.
There it says that the sum of the squares of the four sides equals the sum of the squares of the two diagonals.

## Explanations

### L1 human

Draw a parallelogram with sides $x$ and $y$.
Its two diagonals are $x + y$ and $x - y$.
The law says: the squares of the two diagonals add up to the squares of the four sides.
For a $3 \times 4$ rectangle, each diagonal is $5$, so the left side is $25 + 25 = 50$, and the four sides give $9 + 16 + 9 + 16 = 50$.

### L2 human

Worked example: we check the law in $\mathbb{C}^2$ with the standard inner product.

1. Let $x = (1, i)$ and $y = (1, 0)$. Then $\norm{x}^2 = 1 + 1 = 2$ and $\norm{y}^2 = 1$.
2. We have $x + y = (2, i)$, with $\norm{x + y}^2 = 4 + 1 = 5$.
3. We have $x - y = (0, i)$, with $\norm{x - y}^2 = 0 + 1 = 1$.
4. The left side is $5 + 1 = 6$, and the right side is $2 \cdot 2 + 2 \cdot 1 = 6$.

The typical use is the test of a norm.
One pair of vectors that breaks the law shows that the norm comes from no inner product.
A trap: one pair that satisfies the law proves nothing.
The maximum norm satisfies it for $x = (1, 0)$ and $y = (2, 0)$, since $9 + 1 = 2 + 8$.

### L3 human

The law is the identity that separates inner product spaces from all other normed spaces, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].
It involves only two vectors, so a norm comes from an inner product as soon as its restriction to each plane does.
Geometrically, the unit ball of a norm that satisfies the law is an ellipsoid.
In convex analysis the law gives uniform convexity.
In a Hilbert space this gives closest points in closed convex sets, the base of the [[orthogonal projection|0B8KZRT28M]] in infinite dimension.
