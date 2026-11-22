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

In every inner product space, the squares of the two diagonals of a parallelogram add up to the squares of its four sides.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Then, for all $x, y \in V$,
$$\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2.$$

The [[proof|6FE43HC13F]] expands both squares.
Conversely, by the [[Jordan-von Neumann theorem|46WGVM5VS6]], a norm that satisfies this law comes from exactly one inner product.

## Remarks

### A rectangle and a slanted parallelogram

Put the sides $x = (3, 0)$ and $y = (0, 4)$ at the origin of $\mathbb{R}^2$.
The diagonals are $x + y = (3, 4)$ and $x - y = (3, -4)$, each of length $5$, so
$$\norm{x + y}^2 + \norm{x - y}^2 = 25 + 25 = 50 = 2 \cdot 9 + 2 \cdot 16.$$
The law does not need a right angle.
For $x = (2, 1)$ and $y = (1, 3)$ the diagonals are $(3, 4)$ and $(1, -2)$, and
$$25 + 5 = 30 = 2 \cdot 5 + 2 \cdot 10.$$
Check: $\norm{x}^2 = 4 + 1 = 5$ and $\norm{y}^2 = 1 + 9 = 10$.

### Why the hypothesis is needed

The only hypothesis is that the norm comes from an inner product, and it cannot be dropped.
For the [[maximum norm on $\mathbb{R}^2$|J5V8HEYXCM]] and $x = (1, 0)$, $y = (0, 1)$, both diagonals $(1, 1)$ and $(1, -1)$ have norm $1$.
So the left side is $1 + 1 = 2$, while the right side is $2 + 2 = 4$.
For the [[taxicab norm|WW2RB40VYX]] $\abs{x_1} + \abs{x_2}$ and the same vectors, both diagonals have norm $2$.
Then the left side is $4 + 4 = 8$ and the right side is again $4$.
The sup norm $\max_{t \in [0, 1]} \abs{f(t)}$ on continuous functions fails in the same way for $f(t) = t$ and $g(t) = 1 - t$.
All four functions $f$, $g$, $f + g = 1$ and $f - g = 2t - 1$ have sup norm $1$, so again $2 \neq 4$.

### What it gives you

The computations above show that the maximum norm and the taxicab norm come from no inner product.
More generally, the $p$-norm $(\abs{x_1}^p + \dots + \abs{x_n}^p)^{1/p}$ on $\mathbb{R}^n$ with $n \geq 2$ satisfies the law only for $p = 2$.

The law also gives the length of a median.
In the triangle with corners $0$, $x$ and $y$, the median from $0$ ends at the midpoint $\tfrac12(x + y)$, and dividing the law by $4$ gives
$$\norm{\tfrac12(x + y)}^2 = \frac{\norm{x}^2 + \norm{y}^2}{2} - \frac{\norm{x - y}^2}{4}.$$
This is Apollonius's formula for the median.

If you subtract the two expansions instead of adding them, you get $\norm{x + y}^2 - \norm{x - y}^2 = 4\ip{x}{y}$ over $\mathbb{R}$, which is the real [[polarization identity|05FKHRT0B4]].

### The converse

The converse is true, and it is the [[Jordan-von Neumann theorem|46WGVM5VS6]].
If a norm on a real or complex vector space satisfies the law for all $x$ and $y$, then exactly one inner product induces it, and the polarization identity gives that inner product.
So the parallelogram law is the exact line between inner product spaces and other normed spaces.

### Watch out

One pair of vectors that breaks the law proves that a norm comes from no inner product.
One pair that satisfies the law proves nothing.
The maximum norm satisfies it for $x = (1, 0)$ and $y = (2, 0)$, since $\norm{x + y}_\infty^2 + \norm{x - y}_\infty^2 = 9 + 1 = 10 = 2 + 8$.
The law must hold for all pairs.

### Generalizations

For $n$ vectors, add $\norm{\pm x_1 \pm \dots \pm x_n}^2$ over all $2^n$ choices of signs.
Each mixed term $\ip{x_j}{x_k}$ with $j \neq k$ appears with each sign equally often, so the sum is $2^n(\norm{x_1}^2 + \dots + \norm{x_n}^2)$.
In a [[Hilbert space|HM2HHE3J51]] the law holds with the same proof, and it is the main step in the proof that a closed convex set has a unique closest point.

## History

The law takes its name from the parallelogram of plane geometry, where it says that the four sides and the two diagonals have the same sum of squares.

## Explanations

### L1 human

Draw a parallelogram with sides $x$ and $y$ from one corner.
Its two diagonals are $x + y$ and $x - y$.
The law says that the squares of the two diagonals add up to the squares of the four sides.
For a $3$ by $4$ rectangle, each diagonal is $5$, so the diagonals give $25 + 25 = 50$, and the four sides give $9 + 16 + 9 + 16 = 50$.
If you push the rectangle sideways, one diagonal gets longer and the other gets shorter, and the total stays the same.

### L2 human

Here is a check in $\mathbb{C}^2$ with the standard inner product $\ip{x}{y} = x_1\overline{y_1} + x_2\overline{y_2}$.
Take $x = (1, i)$ and $y = (1, 0)$.
The squared norms are sums of squared moduli:
$$\norm{x}^2 = 1 + \abs{i}^2 = 2, \qquad \norm{y}^2 = 1.$$
The diagonals are $x + y = (2, i)$ and $x - y = (0, i)$, so
$$\norm{x + y}^2 + \norm{x - y}^2 = (4 + 1) + (0 + 1) = 6 = 2 \cdot 2 + 2 \cdot 1.$$
The complex case needs no change, because the cross terms $\ip{x}{y} + \ip{y}{x}$ cancel whether they are real or not.
The typical use goes the other way: you test a norm with one pair, and a failure shows that the norm comes from no inner product.

### L3 human

The law separates inner product spaces from all other normed spaces, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].
It involves only two vectors, so a norm comes from an inner product as soon as its restriction to each plane does.
In finite dimension, the unit ball of a norm that satisfies the law is an ellipsoid.
In convex analysis the law makes the norm uniformly convex.
In a Hilbert space this gives closest points in closed convex sets, which is the base of the [[orthogonal projection|0B8KZRT28M]] in infinite dimension.
