---
tag: 09DZ8CD1AK
kind: statement
role: theorem
name: Coordinates in an orthonormal basis
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0S9GGTR0EX, 04CYQHN6MC]
uses: [0FWJ0VW561, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: Basic formula
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Statement

In an orthonormal basis, each coordinate of a vector is one inner product, and the squared length of the vector is the sum of the squared coordinates.
Let $V$ be a finite-dimensional [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with an inner product that is linear in the first slot.
Let $(e_1, \dots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $V$.
Then, for each $v \in V$:

1. $v = \sum_{i=1}^{n} \ip{v}{e_i}\, e_i$, so the [[coordinate vector|04CYQHN6MC]] of $v$ is $(\ip{v}{e_1}, \dots, \ip{v}{e_n})$;
2. $\norm{v}^2 = \sum_{i=1}^{n} \abs{\ip{v}{e_i}}^2$, where $\norm{\cdot}$ is the [[induced norm|0KG4D8AP6G]].

## Remarks

### A first use

Take the orthonormal basis $e_1 = \tfrac13(1, 2, 2)$, $e_2 = \tfrac13(2, 1, -2)$, $e_3 = \tfrac13(2, -2, 1)$ of $\mathbb{R}^3$ and the vector $v = (3, 0, 3)$.
Part 1 says that the coordinates are three dot products:
$$v \cdot e_1 = \tfrac{3 + 6}{3} = 3, \qquad v \cdot e_2 = \tfrac{6 - 6}{3} = 0, \qquad v \cdot e_3 = \tfrac{6 + 3}{3} = 3.$$
Check: $3 e_1 + 3 e_3 = (1, 2, 2) + (2, -2, 1) = (3, 0, 3)$.
Part 2 says that $3^2 + 0^2 + 3^2 = 18$ is the squared length, and indeed $\norm{v}^2 = 9 + 0 + 9 = 18$.
In a basis that is not orthonormal, the same coordinates would need a $3 \times 3$ linear system.

### Why each hypothesis is needed

The basis must be normalized.
For the orthogonal basis $(1, 1)$, $(1, -1)$ of $\mathbb{R}^2$ and $v = (3, 1)$, the formula gives $2v$, as the [[orthogonal basis that is not orthonormal|72YCTDMG60]] shows.

The family must span $V$.
For the orthonormal family $(e_1)$ in $\mathbb{R}^2$ and $v = (1, 1)$, the sum is $\ip{v}{e_1} e_1 = (1, 0) \neq v$, and part 2 fails too, since $1 < 2 = \norm{v}^2$.

Over $\mathbb{C}$ the order of the slots matters.
With $\ip{e_i}{v}$ in place of $\ip{v}{e_i}$, each coordinate is replaced by its conjugate, and the [[orthonormal basis of $\mathbb{C}^2$|V2B3V8T8TX]] then gives $-v$ for $v = (0, 1)$.
With the convention of physics or of Mathlib, which is linear in the second slot, the same coordinate is written $\ip{e_i}{v}$, and it has the same value as our $\ip{v}{e_i}$.

### What it gives you

The coordinates need no linear system, since each one is a single inner product.
The coordinate map $V \to \mathbb{K}^n$, $v \mapsto (\ip{v}{e_i})_i$, preserves norms by part 2, and by the [[polarization identity|05FKHRT0B4]] it then preserves inner products; that is [[Parseval's identity|047RFCNVSK]].
If $T \colon V \to V$ is linear, part 1 applied to $T e_j$ shows that the entry $(i, j)$ of the matrix of $T$ in this basis is $\ip{T e_j}{e_i}$.
If $v$ is orthogonal to every $e_i$, then part 1 gives $v = 0$.

### The converse

The converse of part 1 holds for a basis.
Suppose a basis $(e_1, \dots, e_n)$ satisfies part 1 for every $v$.
For $v = e_j$ we get $e_j = \sum_i \ip{e_j}{e_i} e_i$, and coordinates in a basis are unique, so $\ip{e_j}{e_i} = \delta_{ij}$ and the basis is orthonormal.
For part 2, suppose that a finite orthonormal family satisfies part 2 for every $v$, without the assumption that it is a basis.
Then it spans $V$, by the equality case of [[Bessel's inequality|0RBT5PB74K]].

### Generalizations and Fourier coefficients

For an orthogonal basis $(u_1, \dots, u_n)$ of nonzero vectors, the formula becomes
$$v = \sum_{i=1}^{n} \frac{\ip{v}{u_i}}{\norm{u_i}^2}\, u_i.$$
For an orthonormal family that does not span $V$, the sum $\sum_i \ip{v}{e_i} e_i$ is the [[orthogonal projection|0B8KZRT28M]] of $v$ onto the span.
In a [[Hilbert space|HM2HHE3J51]] with an orthonormal basis, part 1 becomes a convergent series.
For periodic functions and the basis $e^{ikt}$ this series is the [[Fourier series|G12KXDHPPS]], and the numbers $\ip{v}{e_i}$ are the [[Fourier coefficients|5NN2YZZR3V]].
That is the model for the whole theorem: every coordinate in an orthonormal basis is a Fourier coefficient.

## Explanations

### L1 human

In an orthonormal basis, each coordinate of a vector is one inner product.
For the usual axes $(1, 0)$ and $(0, 1)$ of the plane, the coordinates of $(3, 4)$ are $3$ and $4$.
After a turn of the axes, the coordinates are still inner products, now with the turned axes.
In every case the squared length of the vector, here $9 + 16 = 25$, is the sum of the squared coordinates, as in the Pythagorean theorem.

### L2 human

Here is the model case of Fourier coefficients.
Let $V$ be the span of $e^{-it}$, $1$ and $e^{it}$ in the complex functions on $[-\pi, \pi]$, with
$$\ip{f}{g} = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) \overline{g(t)} \, dt.$$
For integers $j$ and $k$, the inner product of $e^{ijt}$ with $e^{ikt}$ is $\frac{1}{2\pi}\int_{-\pi}^{\pi} e^{i(j - k)t}\, dt$, which is $1$ for $j = k$ and $0$ for $j \neq k$.
So the three functions form an orthonormal basis of $V$.
Take $f(t) = \cos t = \tfrac12 e^{it} + \tfrac12 e^{-it}$.
The coefficient of $e^{it}$ is
$$\ip{f}{e^{it}} = \frac{1}{2\pi} \int_{-\pi}^{\pi} \cos t \, e^{-it} \, dt = \frac{1}{2\pi} \int_{-\pi}^{\pi} \left(\tfrac12 + \tfrac12 e^{-2it}\right) dt = \tfrac12.$$
In the same way $\ip{f}{e^{-it}} = \tfrac12$ and $\ip{f}{1} = 0$, so part 1 recovers the formula for $\cos t$.
For part 2, $\norm{f}^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} \cos^2 t \, dt = \tfrac12$, and $\abs{\tfrac12}^2 + 0 + \abs{\tfrac12}^2 = \tfrac12$.
This is the typical use in signal processing, where each coefficient measures the amount of one frequency in a signal.

### L3 human

The theorem says that an orthonormal basis turns $V$ into $\mathbb{K}^n$ with the standard inner product, by an isometry.
The coordinate functionals $v \mapsto \ip{v}{e_i}$ are the [[dual basis|0ZD2CF6ZS0]] of $(e_1, \dots, e_n)$.
Under the [[Riesz representation|04GYPXDXNH]] the functional $\ip{\cdot}{e_i}$ corresponds to $e_i$, so an orthonormal basis is its own dual basis.
In infinite dimension the formula is the expansion in a Hilbert basis, and Fourier series on $[-\pi, \pi]$ are the model case.
