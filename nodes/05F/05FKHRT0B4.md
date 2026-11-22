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

The induced norm determines the inner product, so a linear map that keeps lengths also keeps inner products.
Let $V$ be an [[inner product space|01EK923SKP]] with the [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$, and let $x, y \in V$.

1. If $V$ is a real space, then
$$\ip{x}{y} = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2\right) = \frac12\left(\norm{x + y}^2 - \norm{x}^2 - \norm{y}^2\right).$$
2. If $V$ is a complex space, with the inner product linear in the first slot and conjugate-linear in the second, then
$$\ip{x}{y} = \frac14 \sum_{k=0}^{3} i^k \norm{x + i^k y}^2 = \frac14\left(\norm{x + y}^2 - \norm{x - y}^2 + i\norm{x + iy}^2 - i\norm{x - iy}^2\right).$$
3. Let $W$ be a second inner product space over the same field, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]] with $\norm{Tx} = \norm{x}$ for all $x \in V$.
   Then $\ip{Tx}{Ty} = \ip{x}{y}$ for all $x, y \in V$.

The [[proof|EMX1YRTN0N]] expands the squared norms.

## Remarks

### Two quick checks

In $\mathbb{R}^2$ with the dot product, take $x = (1, 2)$ and $y = (3, 1)$.
The diagonals are $(4, 3)$ and $(-2, 1)$, with squared lengths $25$ and $5$, so part 1 gives
$$\ip{x}{y} = \frac14(25 - 5) = 5.$$
Check: $1 \cdot 3 + 2 \cdot 1 = 5$.

In $\mathbb{C}$ with $\ip{z}{w} = z\overline{w}$, take $x = 1$ and $y = i$, so that $\ip{x}{y} = \overline{i} = -i$.
The four squared norms are $\abs{1 + i}^2 = 2$, $\abs{1 - i}^2 = 2$, $\abs{1 + i \cdot i}^2 = 0$ and $\abs{1 - i \cdot i}^2 = 4$.
Part 2 gives
$$\frac14\big(2 - 2 + i \cdot 0 - i \cdot 4\big) = -i,$$
which is the expected value.

### Why each hypothesis is needed

The norm must be induced by an inner product.
For the [[maximum norm on $\mathbb{R}^2$|J5V8HEYXCM]], the formula of part 1 still defines a function of $x$ and $y$, but it is not bilinear, by the [[Jordan-von Neumann theorem|46WGVM5VS6]].

Over $\mathbb{C}$, the real formula is not enough, because it gives only $\operatorname{Re}\ip{x}{y}$.
For $x = 1$ and $y = i$ it gives $\frac14(2 - 2) = 0$, but $\ip{1}{i} = -i$.

In part 3, $T$ must be linear.
The map $f(x) = \norm{x}\,e_1$ on $\mathbb{R}^2$ keeps norms, but $f(e_1) = f(e_2) = e_1$, so $\ip{f(e_1)}{f(e_2)} = 1$ while $\ip{e_1}{e_2} = 0$.
A conjugate-linear map is not enough either.
The [[conjugation on $\mathbb{C}^n$|MMSPCWKJQY]] keeps norms, but $\ip{\overline{x}}{\overline{y}} = \overline{\ip{x}{y}}$, which differs from $\ip{x}{y}$ whenever $\ip{x}{y}$ is not real.

### What it gives you

The norm determines the inner product, so two inner products with the same induced norm are equal.
A linear map that keeps norms is a [[linear isometry|07SJXTWVQW]], and by part 3 it also keeps angles and orthogonality, so it sends [[orthonormal families|0RW9TNNT87]] to orthonormal families.
For a square real matrix $Q$ with $\norm{Qx} = \norm{x}$ for all $x$, part 3 gives $\ip{Qe_j}{Qe_k} = \ip{e_j}{e_k}$, so the columns of $Q$ are orthonormal and $Q$ is an [[orthogonal matrix|0W02QESPJQ]].
The same argument makes a complex matrix with this property a [[unitary matrix|0AR68JTMDT]].
The [[Jordan-von Neumann theorem|46WGVM5VS6]] uses parts 1 and 2 as the definition of the inner product that it builds from a norm.

### The converse

Part 3 has a true converse: a linear map that keeps inner products keeps norms, because $\norm{Tx}^2 = \ip{Tx}{Tx} = \ip{x}{x} = \norm{x}^2$.
For parts 1 and 2, the converse question is whether the formulas turn every norm into an inner product.
They do not, and the [[parallelogram law|026HPGYGS4]] is the exact condition for them to work.

### Watch out for the convention

Books of physics make the inner product linear in the second slot and conjugate-linear in the first, and so does Mathlib.
Their inner product of $x$ and $y$ is our $\ip{y}{x}$, the conjugate of ours.
So their complex formula is
$$\frac14\sum_{k=0}^{3} i^{-k}\norm{x + i^k y}^2,$$
with $i^{-k}$ in place of $i^k$.
If you copy a formula from such a book, check the convention first, or you get the conjugate of the value you want.

### Generalizations

Let $\beta$ be a symmetric bilinear form over a field in which $2 \neq 0$, with [[quadratic form|0RBQS1JJCR]] $Q(x) = \beta(x, x)$.
Then $Q$ determines $\beta$ by $\beta(x, y) = \frac12\big(Q(x + y) - Q(x) - Q(y)\big)$, by the same expansion as part 1.
For a [[Hermitian form|48P4A1CX85]] $h$, the complex formula with $h(x, x)$ in place of $\norm{x}^2$ recovers $h$.

## Explanations

### L1 human

If we know the length of every vector, we also know every inner product, and so every angle.
In the real case we need only the lengths of the two diagonals $x + y$ and $x - y$ of the parallelogram with sides $x$ and $y$.
For $x = (1, 2)$ and $y = (3, 1)$, the diagonals $(4, 3)$ and $(-2, 1)$ have squared lengths $25$ and $5$.
A quarter of the difference is $\frac14(25 - 5) = 5$, and that is the dot product $3 + 2$.

### L2 human

Here is a typical use: show that the rotation $R(x_1, x_2) = (x_1 \cos\theta - x_2 \sin\theta, \, x_1 \sin\theta + x_2 \cos\theta)$ of $\mathbb{R}^2$ keeps dot products.
The map is linear, so by part 3 it is enough to check lengths.
Expand the squared length of $Rx$:
$$\norm{Rx}^2 = (x_1 \cos\theta - x_2 \sin\theta)^2 + (x_1 \sin\theta + x_2 \cos\theta)^2 = (x_1^2 + x_2^2)(\cos^2\theta + \sin^2\theta) = \norm{x}^2.$$
The cross terms $\mp 2x_1x_2\cos\theta\sin\theta$ cancel.
So $Rx \cdot Ry = x \cdot y$ for all $x$ and $y$, and the rotation keeps every angle.
One computation with one vector replaced a computation with two vectors, and that is the usual gain.

### L3 human

Polarization is the passage from a quadratic object to the symmetric bilinear or sesquilinear object that it determines.
In linear algebra it says that the norm, a function of one vector, carries all the information of the inner product.
So the orthogonal group is exactly the group of linear maps that keep lengths, and the unitary group is the complex analogue.
The same idea works for quadratic forms over fields in which $2 \neq 0$, for Hermitian forms, and for homogeneous polynomials of higher degree, where a form of degree $d$ determines a symmetric $d$-linear form when $d!$ is invertible.
