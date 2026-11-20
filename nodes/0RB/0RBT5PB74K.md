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

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$.
Let $e_1, \dots, e_k$ be an [[orthonormal family|09VYHEF2VT]] in $V$, and let $x \in V$.

1. The inequality $\sum_{i=1}^{k} |\ip{x}{e_i}|^2 \leq \norm{x}^2$ holds.
2. More precisely, $\norm{x}^2 - \sum_{i=1}^{k} |\ip{x}{e_i}|^2 = \norm{x - \sum_{i=1}^{k} \ip{x}{e_i} e_i}^2$.
3. Equality holds in part 1 if and only if $x$ lies in the [[span|0HR573CHNM]] of $e_1, \dots, e_k$.

## Remarks

### Why each hypothesis is needed

- The vectors must be unit vectors. For $u = (2, 0)$ in $\mathbb{R}^2$ and $x = (1, 0)$, $|\ip{x}{u}|^2 = 4 > 1 = \norm{x}^2$.
- The vectors must be pairwise orthogonal. For $e_1 = (1, 0)$, $f = \frac{1}{\sqrt2}(1, 1)$ and $x = f$, the sum is $\frac12 + 1 = \frac32 > 1$.
- A family that repeats a vector is not orthonormal. For $(e_1, e_1)$ and $x = e_1$, the sum is $2 > 1$.

### Consequences

- The distance from $x$ to $U = \operatorname{span}(e_1, \dots, e_k)$ satisfies $d(x, U)^2 = \norm{x}^2 - \sum_i |\ip{x}{e_i}|^2$, by part 2 and the [[closest point theorem|0MCDDSCB9Z]].
- For an [[orthonormal basis|0FWJ0VW561]] every $x$ lies in the span, so part 3 gives $\norm{x}^2 = \sum_i |\ip{x}{e_i}|^2$. This is the norm form of [[Parseval's identity|047RFCNVSK]].
- If an orthonormal family satisfies equality for every $x$, then it spans $V$, so it is an orthonormal basis.
- For each $\varepsilon > 0$, at most $\norm{x}^2 / \varepsilon$ indices $i$ satisfy $|\ip{x}{e_i}|^2 \geq \varepsilon$.

### Converse

The converse is false: the inequality for every $x$ does not make a family orthonormal.
The family with the single vector $\frac12 e_1$ in $\mathbb{R}^2$ gives $\frac14 x_1^2 \leq \norm{x}^2$ for all $x$, but its vector has norm $\frac12$.
The converse of part 3 is part of the statement, since part 3 is an equivalence.

### Generalizations

- For an infinite orthonormal family $(e_i)_{i \in I}$, the sum $\sum_{i \in I} |\ip{x}{e_i}|^2$ converges and is at most $\norm{x}^2$. Mathlib states this form.
- Only countably many $\ip{x}{e_i}$ are nonzero, by the counting consequence above with $\varepsilon = 1/m$ for $m = 1, 2, \dots$
- For [[Fourier series|G12KXDHPPS]], the inequality says that the squares of the [[Fourier coefficients|5NN2YZZR3V]] of a square integrable function have a finite sum.

## History

According to the Wikipedia article, the inequality is named for Bessel, who derived a special case of it in 1828.

## Explanations

### L1 human

Project a vector onto a few perpendicular directions of length $1$.
The squared lengths of the pieces add up to at most the squared length of the vector.
The missing amount is the squared length of the part that the directions do not reach.
If the directions reach the vector, nothing is missing.

### L2 human

Worked example: in $\mathbb{R}^3$ let $e_1 = \frac{1}{\sqrt2}(1, 1, 0)$, $e_2 = (0, 0, 1)$ and $x = (1, 2, 3)$.

1. $\ip{x}{e_1} = \frac{3}{\sqrt2}$ and $\ip{x}{e_2} = 3$.
2. The sum of squares is $\frac92 + 9 = \frac{27}{2}$, and $\norm{x}^2 = 1 + 4 + 9 = 14$. So $\frac{27}{2} \leq 14$.
3. The projection is $s = \frac{3}{\sqrt2} e_1 + 3e_2 = (\frac32, \frac32, 3)$, and $x - s = (-\frac12, \frac12, 0)$.
4. Part 2: $\norm{x - s}^2 = \frac14 + \frac14 = \frac12 = 14 - \frac{27}{2}$.
5. Since $x - s \neq 0$, the vector $x$ is not in the span, and the inequality is strict.

The typical use is to bound coefficients in an expansion without knowing the full basis.
A trap: Bessel's inequality needs an orthonormal family.
For an orthogonal family of other lengths, divide each term by $\norm{e_i}^2$ first.

### L3 human

Part 2 says that $\sum_i \ip{x}{e_i} e_i$ is the [[orthogonal projection|0B8KZRT28M]] of $x$ onto the span.
It also says that the defect in Bessel's inequality is the squared distance to the span.
In a [[Hilbert space|HM2HHE3J51]] the inequality makes the series $\sum_i \ip{x}{e_i} e_i$ converge, and equality for all $x$ characterizes a Hilbert basis.
In analysis, it gives the first fact about Fourier coefficients: they are square summable, so they tend to $0$.
