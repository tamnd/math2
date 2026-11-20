---
tag: 05FKHRT0B4
kind: statement
role: theorem
name: Polarization identity
msc: ["46C05", "15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0NB0AWGJBW, 0MFJJV97RJ]
uses: [01EK923SKP, 0KG4D8AP6G, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Polarization identities
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Isometries
  - book: isbn:9783031410253
    locator: Chapter 6
same_as:
  wikidata: Q1817177
  wikipedia: Polarization identity
---

## Statement

Let $V$ be an [[inner product space|01EK923SKP]] with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$, and let $x, y \in V$.

1. If $V$ is a real space, then
$$\ip{x}{y} = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right) = \frac12\left(\norm{x + y}^2 - \norm{x}^2 - \norm{y}^2\right).$$
2. If $V$ is a complex space, with the inner product linear in the first argument, then
$$\ip{x}{y} = \frac14 \sum_{k=0}^{3} i^k \norm{x + i^k y}^2 = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2 + i\norm{x + iy}^2 - i\norm{x - iy}^2\right).$$
3. Let $W$ be a second inner product space over the same field, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]] with $\norm{Tx} = \norm{x}$ for all $x \in V$. Then $\ip{Tx}{Ty} = \ip{x}{y}$ for all $x, y \in V$.

The [[proof|EMX1YRTN0N]] expands the squared norms.

## Remarks

### Why each hypothesis is needed

- The norm must be induced by an inner product. For the [[maximum norm on $\mathbb{R}^2$|J5V8HEYXCM]], the formula of part 1 gives a function that is not bilinear, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].
- Over $\mathbb{C}$, the real formula is not enough. It gives only $\operatorname{Re}\ip{x}{y}$: for $x = 1$ and $y = i$ in $\mathbb{C}$, it gives $\frac14(2 - 2) = 0$, but $\ip{1}{i} = \overline{i} = -i$.
- In part 3, $T$ must be linear. The map $f(x) = \norm{x}\,e_1$ on $\mathbb{R}^2$ keeps norms, but $f(e_1) = f(e_2) = e_1$, so $\ip{f(e_1)}{f(e_2)} = 1 \neq 0 = \ip{e_1}{e_2}$.
- In part 3, the conjugate-linear [[conjugation on $\mathbb{C}^n$|MMSPCWKJQY]] keeps norms, but $\ip{\overline{x}}{\overline{y}} = \overline{\ip{x}{y}}$, which differs from $\ip{x}{y}$ when the inner product is not real.

### Consequences

- The norm determines the inner product. Two inner products with the same induced norm are equal.
- A linear map that keeps norms is a [[linear isometry|07SJXTWVQW]], and by part 3 it keeps angles and orthogonality too. It sends [[orthonormal families|0RW9TNNT87]] to orthonormal families.
- A square real matrix $Q$ with $\norm{Qx} = \norm{x}$ for all $x$ is an [[orthogonal matrix|0W02QESPJQ]]. A complex one is a [[unitary matrix|0AR68JTMDT]]. The reason is that part 3 gives $\ip{Qe_j}{Qe_k} = \ip{e_j}{e_k}$.
- The [[Jordan-von Neumann theorem|46WGVM5VS6]] uses part 1 and part 2 as the definition of the inner product built from a norm.

### Converse

Part 3 has a true converse: a linear map that keeps inner products keeps norms, because $\norm{Tx}^2 = \ip{Tx}{Tx} = \ip{x}{x}$.
For parts 1 and 2, the converse question is whether every norm has an inner product given by these formulas.
It is false in general, and the [[parallelogram law|026HPGYGS4]] is the exact condition.

### Generalizations

- For a symmetric bilinear form $\beta$ over a field in which $2 \neq 0$, the [[quadratic form|0RBQS1JJCR]] $Q(x) = \beta(x, x)$ determines $\beta$ by $\beta(x, y) = \frac12(Q(x + y) - Q(x) - Q(y))$.
- For a [[Hermitian form|48P4A1CX85]] $h$, the same complex formula with $h(x, x)$ in place of $\norm{x}^2$ recovers $h$.
- With the physics convention of linearity in the second argument, the inner product is the conjugate of ours, so the formula becomes $\frac14\sum_{k=0}^{3} i^{-k}\norm{x + i^k y}^2$.

## Explanations

### L1 human

If we know the length of every vector, we also know every inner product, and so every angle.
In the real case we only need the lengths of the two diagonals $x + y$ and $x - y$ of a parallelogram.
For $x = (1, 2)$ and $y = (3, 1)$ in the plane, the diagonals are $(4, 3)$ and $(-2, 1)$, with squared lengths $25$ and $5$.
Then $\frac14(25 - 5) = 5$, which is the dot product $3 + 2$.

### L2 human

Worked example: the complex formula in $\mathbb{C}$ with $\ip{z}{w} = z\overline{w}$.

1. Let $x = 1$ and $y = i$. We expect $\ip{x}{y} = 1 \cdot \overline{i} = -i$.
2. The four terms are $\norm{1 + i}^2 = 2$, $\norm{1 - i}^2 = 2$, $\norm{1 + i \cdot i}^2 = \norm{0}^2 = 0$ and $\norm{1 - i \cdot i}^2 = \norm{2}^2 = 4$.
3. The formula gives $\frac14(2 - 2 + i \cdot 0 - i \cdot 4) = -i$.
4. So the formula returns the expected value.

The typical use is to prove that a linear map keeps inner products: one checks only the norms.
A trap: a book with the physics convention puts the conjugate on the other side, and its complex formula has $i^{-k}$ in place of $i^k$.

### L3 human

Polarization is the passage from a quadratic object to the symmetric bilinear object that it determines.
In linear algebra it says that the norm, a function of one vector, carries all the information of the inner product.
So the orthogonal group is the group of linear maps that keep lengths.
The same holds for the unitary group.
The same idea appears for quadratic forms over fields where $2 \neq 0$, for Hermitian forms, and for homogeneous polynomials of higher degree.
