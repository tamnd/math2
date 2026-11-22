---
tag: 0RBT5PB74K
kind: statement
role: theorem
name: Bessel's inequality
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0RW9TNNT87, 0MFJJV97RJ]
uses: [09VYHEF2VT, 0KG4D8AP6G, 0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel's_inequality
    locator: Statement of the inequality
  - book: isbn:9783031410253
    locator: Chapter 6
formal:
  - system: lean4
    library: mathlib
    decl: Orthonormal.tsum_inner_products_le
    match: partial
history:
  first_stated: "Bessel, 1828, a special case"
  notes: "The Wikipedia article states that the inequality is named for Bessel, who derived a special case of it in 1828."
same_as:
  wikidata: Q794042
  wikipedia: Bessel's inequality
---

## Statement

Bessel's inequality says that the coordinates of a vector along a few orthonormal directions never carry more than the whole squared length of the vector.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot, and let $\norm{\cdot}$ be the [[induced norm|0KG4D8AP6G]].
Let $e_1, \dots, e_k$ be an [[orthonormal family|09VYHEF2VT]] in $V$, and let $x \in V$.

1. The coefficients satisfy $\sum_{i=1}^{k} \abs{\ip{x}{e_i}}^2 \leq \norm{x}^2$.
2. The gap is a squared length: $\norm{x}^2 - \sum_{i=1}^{k} \abs{\ip{x}{e_i}}^2 = \norm{x - \sum_{i=1}^{k} \ip{x}{e_i} e_i}^2$.
3. Equality holds in part 1 if and only if $x$ lies in the [[span|0HR573CHNM]] of $e_1, \dots, e_k$.

The [[proof|FHHPA8GQE8]] splits $x$ into a part along the family and a part orthogonal to it.

## Remarks

### A first computation

Take $V = \mathbb{R}^2$ with the dot product, the single unit vector $e_1 = (\tfrac35, \tfrac45)$, and $x = (2, 1)$.
The coefficient is
$$\ip{x}{e_1} = \frac{6 + 4}{5} = 2,$$
so the left side of part 1 is $4$, while $\norm{x}^2 = 4 + 1 = 5$.
The gap is $1$, and part 2 says that it is the squared length of $x - 2e_1$:
$$x - 2e_1 = \left(2 - \tfrac65, \, 1 - \tfrac85\right) = \left(\tfrac45, -\tfrac35\right), \qquad \norm{x - 2e_1}^2 = \tfrac{16}{25} + \tfrac{9}{25} = 1.$$
Check: $4 + 1 = 5$.
The inequality is strict because one direction cannot reach every vector of the plane.

### Why each hypothesis is needed

The vectors must have length $1$.
For $u = (2, 0)$ and $x = (1, 0)$ in $\mathbb{R}^2$, we get $\abs{\ip{x}{u}}^2 = 4$, which is larger than $\norm{x}^2 = 1$.
A long vector inflates its own coefficient.

The vectors must also be pairwise orthogonal.
Take $e_1 = (1, 0)$ and $f = \tfrac{1}{\sqrt2}(1, 1)$, two unit vectors at an angle of $45$ degrees, and let $x = f$.
Then $\abs{\ip{x}{e_1}}^2 + \abs{\ip{x}{f}}^2 = \tfrac12 + 1 = \tfrac32$, which is more than $\norm{x}^2 = 1$, because the two directions count the same part of $x$ twice.
The extreme case is a family that repeats a vector: for $(e_1, e_1)$ and $x = e_1$ the sum is $2$.

### What it gives you

Part 2 measures how far $x$ is from the subspace $U = \operatorname{span}(e_1, \dots, e_k)$.
The vector $\sum_i \ip{x}{e_i} e_i$ is the point of $U$ closest to $x$, by the [[best approximation theorem|0MCDDSCB9Z]], so the squared distance from $x$ to $U$ is $\norm{x}^2 - \sum_i \abs{\ip{x}{e_i}}^2$.

When the family is an [[orthonormal basis|0FWJ0VW561]], every $x$ lies in the span, and part 3 turns the inequality into the equality $\norm{x}^2 = \sum_i \abs{\ip{x}{e_i}}^2$.
That is the norm form of [[Parseval's identity|047RFCNVSK]].
Read the other way, an orthonormal family that gives equality for every $x$ spans $V$, so it is a basis.

The inequality also limits how many coefficients can be large.
If $\abs{\ip{x}{e_i}}^2 \geq \varepsilon$ for $N$ indices, then these terms alone add up to at least $N \varepsilon$, so $N \leq \norm{x}^2 / \varepsilon$.

### The converse

The inequality for every $x$ does not make a family orthonormal.
The single vector $\tfrac12 e_1$ in $\mathbb{R}^2$ gives $\abs{\ip{x}{\tfrac12 e_1}}^2 = \tfrac14 x_1^2 \leq \norm{x}^2$ for every $x$, but its length is $\tfrac12$.
Part 3 is already an equivalence, so it has no separate converse.

### The infinite form

For an infinite orthonormal family $(e_i)_{i \in I}$ in any inner product space, each finite subfamily obeys the inequality.
So the sum $\sum_{i \in I} \abs{\ip{x}{e_i}}^2$ converges and is at most $\norm{x}^2$, and this is the form that Mathlib proves.
The counting bound above, with $\varepsilon = 1/m$ for $m = 1, 2, \dots$, shows that only countably many coefficients are nonzero.
For [[Fourier series|G12KXDHPPS]], the infinite form says that the squared moduli of the [[Fourier coefficients|5NN2YZZR3V]] of a square integrable function have a finite sum, so the coefficients tend to $0$.
The [[Hilbert space|HM2HHE3J51]] version belongs to functional analysis.

### Watch out

Bessel's inequality is about orthonormal families, not orthogonal ones.
For an orthogonal family of nonzero vectors $u_i$ of other lengths, first divide each term by $\norm{u_i}^2$:
$$\sum_i \frac{\abs{\ip{x}{u_i}}^2}{\norm{u_i}^2} \leq \norm{x}^2.$$
For $u = (2, 0)$ and $x = (1, 0)$ this gives $\tfrac44 = 1 \leq 1$, and the false value $4$ from above disappears.

### Try it

First, with $e_1 = \tfrac{1}{\sqrt2}(1, 1, 0)$ in $\mathbb{R}^3$ and $x = (1, 1, 1)$, compute both sides of part 1.
The coefficient is $\tfrac{2}{\sqrt2} = \sqrt2$, so the left side is $2$ and the right side is $3$, with gap $1 = \norm{(0, 0, 1)}^2$.

Second, check that equality holds for $x = (3, 3, 0)$ and the same $e_1$.
Here $\ip{x}{e_1} = \tfrac{6}{\sqrt2} = 3\sqrt2$, so both sides are $18$, and indeed $x = 3\sqrt2\, e_1$ lies in the span, as part 3 predicts.

## History

The inequality is named after Friedrich Wilhelm Bessel, who derived a special case of it in 1828.

## Explanations

### L1 human

Shine a light straight down on a stick and look at its shadow on the floor.
The shadow is never longer than the stick.
Bessel's inequality says the same thing with several perpendicular directions at once: the squared lengths of the shadows add up to at most the squared length of the stick.
The missing amount is the squared length of the part that sticks out of the floor.
If the stick lies flat, nothing is missing.

### L2 human

Here is a typical computation in $\mathbb{R}^3$ with the dot product.
Let $e_1 = \tfrac{1}{\sqrt2}(1, 1, 0)$ and $e_2 = (0, 0, 1)$, which are orthonormal, and let $x = (1, 2, 3)$.
The coefficients are
$$\ip{x}{e_1} = \frac{1 + 2}{\sqrt2} = \frac{3}{\sqrt2}, \qquad \ip{x}{e_2} = 3.$$
Their squares add up to $\tfrac92 + 9 = \tfrac{27}{2}$, and $\norm{x}^2 = 1 + 4 + 9 = 14$, so the inequality reads $\tfrac{27}{2} \leq 14$.
The projection onto the span is
$$s = \frac{3}{\sqrt2} e_1 + 3 e_2 = \left(\tfrac32, \tfrac32, 3\right), \qquad x - s = \left(-\tfrac12, \tfrac12, 0\right).$$
Check part 2: $\norm{x - s}^2 = \tfrac14 + \tfrac14 = \tfrac12 = 14 - \tfrac{27}{2}$.
Since $x - s \neq 0$, the vector $x$ is not in the plane spanned by $e_1, e_2$, and the inequality is strict.
The same computation gives the distance $\tfrac{1}{\sqrt2}$ from $x$ to that plane without solving any system.

### L3 human

Part 2 says that $\sum_i \ip{x}{e_i} e_i$ is the [[orthogonal projection|0B8KZRT28M]] of $x$ onto the span of the family, and that the defect in the inequality is the squared distance to that span.
In a [[Hilbert space|HM2HHE3J51]] the inequality makes the series $\sum_i \ip{x}{e_i} e_i$ converge for every orthonormal family, and equality for all $x$ characterizes a Hilbert basis.
In harmonic analysis it is the first fact about Fourier coefficients: they are square summable.
The sub-area on orthogonality and least squares builds projections onto subspaces from this identity.
