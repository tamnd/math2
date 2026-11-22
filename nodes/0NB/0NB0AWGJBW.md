---
tag: 0NB0AWGJBW
kind: concept
name: Inner product
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
uses: [000AYPA9AJ, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Convention variant
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
inventory: [HE1J3Q8VXR]
---

## Summary

An inner product is a rule that pairs two vectors and returns a number, in the way the [[dot product|0S52TNNTH9]] does in $\mathbb{R}^n$.
Once a space has such a rule, it has lengths, angles and right angles, even when its vectors are polynomials or matrices.
Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let $V$ be a [[vector space|000AYPA9AJ]] over $\mathbb{K}$.
An *inner product* on $V$ is a map $V \times V \to \mathbb{K}$, $(x, y) \mapsto \ip{x}{y}$, such that for all $x, y, z \in V$ and all $a, b \in \mathbb{K}$:
$$\ip{ax + by}{z} = a\ip{x}{z} + b\ip{y}{z}, \qquad \ip{y}{x} = \overline{\ip{x}{y}}, \qquad \ip{x}{x} > 0 \text{ for } x \neq 0.$$
The three conditions are linearity in the first slot, conjugate symmetry (the bar is the [[complex conjugate|0FTH2E9TAS]]) and positive definiteness.
Over $\mathbb{R}$ the bar does nothing, and an inner product is a symmetric bilinear map with $\ip{x}{x} > 0$ for $x \neq 0$.
The [[formal definition|0VGSYBWHV2]] states the same axioms.

## Motivation

The dot product gives the length of a vector and the angle between two vectors.
If you look at the proofs of its rules, they use only three facts: symmetry, linearity in each factor, and $v \cdot v > 0$ for $v \neq 0$.
So any rule with these three properties brings the whole geometry along.
This is why we can speak of the distance between two functions, or of two matrices at a right angle, and use pictures from the plane to reason about them.

Least squares fitting, Fourier series and quantum mechanics all live on this idea.
A Fourier coefficient is an inner product of a signal with a sine wave, and the probability of a measurement in quantum mechanics is the squared size of an inner product of two complex vectors.
In linear algebra the inner product returns in orthogonal projections, in the adjoint of a map and in the spectral theorems of the later sub-areas.

## Notation

Most books write $\ip{x}{y}$, and you will also see $(x, y)$, $\langle x \mid y \rangle$ and, on $\mathbb{R}^n$, $x \cdot y$.
In math2 a complex inner product is linear in the first slot and conjugate-linear in the second, as in most mathematics books.
Physics books, following the bra-ket notation of Dirac, make it linear in the second slot and conjugate-linear in the first.
Mathlib follows the physics order, so its value on the pair $(x, y)$ is our $\ip{y}{x}$.
When two inner products are present, a subscript names each one, as in $\ip{x}{y}_A$.

## Remarks

### A first computation

Start in $\mathbb{R}^2$ with the rule
$$\ip{x}{y} = 2x_1 y_1 + x_2 y_2.$$
It is symmetric and linear in each slot, because each term is a product of one entry of $x$ and one entry of $y$.
It is positive, because $\ip{x}{x} = 2x_1^2 + x_2^2$ is a sum of squares with positive weights, and it is $0$ only when $x_1 = x_2 = 0$.
So it is an inner product, but a new one.
For $x = (1, 1)$ and $y = (1, -2)$ we get
$$\ip{x}{y} = 2 \cdot 1 \cdot 1 + 1 \cdot (-2) = 0,$$
so these two vectors are at a right angle for the new rule, although their dot product is $1 - 2 = -1$.
Lengths change too: $\ip{x}{x} = 2 + 1 = 3$, so $x$ has length $\sqrt{3}$ instead of $\sqrt{2}$.

### Why complex vectors need a conjugate

Over $\mathbb{C}$ the plain formula $x_1 y_1 + x_2 y_2$ breaks down.
The vector $(1, i)$ would get the square length $1 + i^2 = 0$, and $(i, 0)$ would get $-1$, as the [[bilinear non-example|3W8AFC4A9P]] shows.
The cure is to conjugate the entries of the second vector, which gives the [[standard inner product on $\mathbb{C}^n$|TFZ8DYVJ1J]]:
$$\ip{x}{y} = x_1 \overline{y_1} + \dots + x_n \overline{y_n}, \qquad \ip{x}{x} = \abs{x_1}^2 + \dots + \abs{x_n}^2.$$
Now $(1, i)$ gets $1 \cdot 1 + i \cdot \overline{i} = 1 + 1 = 2$.
The price is that symmetry becomes conjugate symmetry.
For $x = (1 + i, 2)$ and $y = (i, 1 - i)$, multiply each entry of $x$ by the conjugate of the matching entry of $y$ and add:
$$\ip{x}{y} = (1 + i)(-i) + 2(1 + i) = (1 - i) + (2 + 2i) = 3 + i.$$
In the other order the same work gives $3 - i$, the conjugate.

### Matrices and polynomials

The same idea works on spaces that do not look like $\mathbb{K}^n$.
On $2 \times 2$ complex matrices, the [[trace inner product|JVH9RZ7QAB]] is $\ip{A}{B} = \tr(B^* A)$, and it equals $\sum_{j, k} a_{jk} \overline{b_{jk}}$, the standard inner product of the four entries.
For $A = I_2$ it gives $\ip{A}{A} = 1 + 0 + 0 + 1 = 2$.
On real polynomials of degree at most $2$, the [[integral inner product|W6NJ22XGWT]] is
$$\ip{p}{q} = \int_0^1 p(t) q(t) \, dt.$$
For $p = 1$ and $q = t$ it gives $\int_0^1 t \, dt = \tfrac12$, and for $q$ with itself it gives $\int_0^1 t^2 \, dt = \tfrac13$.
Positivity holds because a nonzero polynomial cannot vanish on a whole interval.
On $\mathbb{C}^n$, every [[positive definite matrix|0KX66CZMBB]] $A$ gives an inner product $\ip{x}{y} = y^* A x$, and every inner product on $\mathbb{C}^n$ arises this way.

### The rules you can use

Three more rules follow from the axioms, and you will use them all the time.
The inner product is conjugate-linear in the second slot, $\ip{x}{ay + z} = \overline{a}\ip{x}{y} + \ip{x}{z}$: apply conjugate symmetry, then linearity in the first slot, then conjugate symmetry again.
The zero vector pairs to zero with everything, since $\ip{0}{y} = \ip{0 \cdot 0}{y} = 0 \cdot \ip{0}{y}$.
The number $\ip{x}{x}$ is always real, since conjugate symmetry with $y = x$ gives $\ip{x}{x} = \overline{\ip{x}{x}}$.

A vector that is orthogonal to everything is zero: if $\ip{x}{y} = 0$ for all $y$, take $y = x$ and use positivity.
Over $\mathbb{R}$ an inner product is the same thing as a positive definite [[symmetric bilinear form|0AXZNE5XNH]], and over $\mathbb{C}$ it is a positive definite [[Hermitian form|48P4A1CX85]].
The size of $\ip{x}{y}$ is bounded by the [[Cauchy-Schwarz inequality|0RFWW56Y22]], $\abs{\ip{x}{y}} \le \norm{x} \, \norm{y}$, for the [[induced norm|0MFJJV97RJ]].

### What it is not

The [[Minkowski form|TFGECQ5C32]] $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ is symmetric and bilinear, but positivity fails: it gives $1 - 1 = 0$ on $(1, 1)$.
The form $x_1 y_1$ on $\mathbb{R}^2$ fails in a milder way, because it is never negative but gives $0$ on $(0, 1)$.
The product of lengths $\norm{x} \, \norm{y}$ is not an inner product, because it is not additive.
With $x = (1, 0)$, $x' = (-1, 0)$ and $y = (1, 0)$, the pair $(x + x', y)$ gives $0$, while the pairs $(x, y)$ and $(x', y)$ give $1 + 1 = 2$.

### Watch out

The first trap is the missing conjugate.
It is tempting to write $\ip{x}{2i y} = 2i\ip{x}{y}$, but the scalar leaves the second slot conjugated, so $\ip{x}{2iy} = -2i\ip{x}{y}$.
A formula copied from a physics book has the conjugate on the other slot, so check the convention before you use it.

The second trap is to test positivity on basis vectors only.
The form $x_1 y_1 - 2x_1 y_2 - 2x_2 y_1 + x_2 y_2$ gives $1$ on $(1, 0)$ and on $(0, 1)$, but on $(1, 1)$ it gives
$$1 - 2 - 2 + 1 = -2.$$
Positivity is a condition on every vector, and you usually prove it by writing $\ip{x}{x}$ as a sum of squares.

### History

The physics convention, linear in the second slot, comes from the bra-ket notation that Dirac introduced for quantum mechanics.
Von Neumann gave the abstract axioms of a complex inner product space with a complete norm, the Hilbert space, in the late 1920s, also for quantum mechanics.

### Try it

First, is $\ip{x}{y} = x_1 y_1 + x_1 y_2 + x_2 y_1 + 2x_2 y_2$ an inner product on $\mathbb{R}^2$?
Yes: it is symmetric and bilinear, and $\ip{x}{x} = (x_1 + x_2)^2 + x_2^2$ is $0$ only when $x_2 = 0$ and $x_1 = 0$.

Second, compute $\ip{(1, i)}{(i, i)}$ for the standard inner product on $\mathbb{C}^2$.
It is $1 \cdot \overline{i} + i \cdot \overline{i} = -i + 1 = 1 - i$.

Third, suppose $\ip{x}{y} = 3$ in a complex inner product space; find $\ip{ix}{y}$ and $\ip{x}{iy}$.
The first is $3i$ and the second is $\overline{i} \cdot 3 = -3i$.

## Explanations

### L1 human

An inner product is a rule that takes two vectors and gives one number, like the dot product of arrows in the plane.
The number of a vector with itself is the square of its length, so it must be positive for every vector that is not zero.
Take the rule "two times the product of the first entries, plus the product of the second entries".
The vector $(1, 1)$ with itself gives $2 \cdot 1 + 1 = 3$, so its length is $\sqrt{3}$ for this rule, and not $\sqrt{2}$ as for the dot product.
So one space can carry several inner products, and each one gives its own lengths and its own right angles.

### L2 human

Here is a typical question: for which numbers $c$ is
$$\ip{x}{y} = x_1 y_1 + c(x_1 y_2 + x_2 y_1) + x_2 y_2$$
an inner product on $\mathbb{R}^2$?
Symmetry and linearity hold for every $c$, because the formula is a sum of products of one entry of $x$ and one entry of $y$, and swapping $x$ and $y$ swaps the two middle terms.
So everything depends on positivity.
Complete the square:
$$\ip{x}{x} = x_1^2 + 2c\, x_1 x_2 + x_2^2 = (x_1 + c x_2)^2 + (1 - c^2) x_2^2.$$
When $\abs{c} < 1$ both coefficients are positive, and the sum is $0$ only when $x_2 = 0$ and then $x_1 = 0$.
When $\abs{c} \ge 1$ positivity fails: for $x = (-c, 1)$ the first square is $0$ and the value is $1 - c^2 \le 0$.
For example, $c = 1$ and $x = (-1, 1)$ give $1 - 2 + 1 = 0$.
So the answer is $-1 < c < 1$.
The problem shows the usual shape of such a check: the algebraic axioms are routine, and the real work is to show that $\ip{x}{x}$ is a positive quantity.

### L3 human

On a real space an inner product is a positive definite symmetric bilinear form, and on a complex space it is a positive definite Hermitian form, so inner products are a special case of the [[bilinear and sesquilinear forms|DYAK7YMK7B]] of a later sub-area.
Each inner product gives a map $V \to V^*$, $y \mapsto \ip{\cdot}{y}$, which is linear over $\mathbb{R}$ and conjugate-linear over $\mathbb{C}$.
In finite dimension the [[Riesz representation theorem|04GYPXDXNH]] shows that this map is a bijection.
On $\mathbb{K}^n$ every inner product is $\ip{x}{y} = y^* A x$ for one positive definite matrix $A$ with entries $a_{jk} = \ip{e_k}{e_j}$, so $A$ is the transpose of the [[Gram matrix|00SPJSDT3Z]] of the standard basis.
Every inner product space of dimension $n$ has an orthonormal basis, so it is isometric to $\mathbb{K}^n$ with the standard inner product.
In infinite dimension the picture changes, and completeness becomes an extra condition: a complete inner product space is a [[Hilbert space|HM2HHE3J51]], the subject of functional analysis.
