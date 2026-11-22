---
tag: 0RW9TNNT87
kind: concept
name: Orthonormal family
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
specializes: [01TXN7ETH2]
uses: [0Y2X7P2WB7, 0MFJJV97RJ]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormality
    locator: Definition
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L545
    locator: src/section6-3.xml:545
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
same_as:
  wikidata: Q1411166
  wikipedia: Orthonormality
---

## Summary

An orthonormal family is a set of coordinate axes for an inner product space: vectors of length $1$ that meet at right angles, two by two.
With such axes, the coefficient of a vector along each axis is a single inner product, and lengths add up as in the Pythagorean theorem.
Let $V$ be an inner product space over $\mathbb{R}$ or $\mathbb{C}$.
A family $(e_i)_{i \in I}$ of vectors of $V$ is *orthonormal* when, for all $i, j \in I$,
$$\ip{e_i}{e_j} = \delta_{ij} = \begin{cases} 1 & \text{if } i = j, \\ 0 & \text{if } i \neq j. \end{cases}$$
In words, each $e_i$ is a unit vector for the [[induced norm|0MFJJV97RJ]], and any two different members are [[orthogonal|0Y2X7P2WB7]].
The [[formal definition|09VYHEF2VT]] states the same condition.

## Motivation

In $\mathbb{R}^n$ the standard basis vectors have length $1$ and meet at right angles.
That is why the coordinates of $x$ are the dot products $x \cdot e_j$, and why the length of $x$ comes from its coordinates by the Pythagorean theorem.
In a general basis neither fact holds, and you must solve a linear system to find the coordinates.
The property that makes the simple formulas work is exactly $\ip{e_i}{e_j} = \delta_{ij}$, so it gets a name.

Orthonormal families appear wherever a signal or a state is split into independent parts.
The sines and cosines of Fourier analysis, the axes of a rotated frame in mechanics and the columns of an orthogonal matrix in numerical work are all orthonormal families.
Later in the area they return as [[orthonormal bases|0S9GGTR0EX]], in the [[Gram-Schmidt process|0VT6P0GNQR]] that produces them, and in the orthogonal projections of the sub-area on least squares.

## Notation

We write $(e_1, \dots, e_k)$ for a finite family, $(e_i)_{i \in I}$ in general, and $\delta_{ij}$ for the Kronecker delta.
Some books say *orthonormal set* or *orthonormal list*.
A family may repeat a vector in general, but an orthonormal family never does, since two equal unit vectors have inner product $1$, not $0$.
An *orthogonal* family only asks $\ip{e_i}{e_j} = 0$ for $i \neq j$, with no condition on lengths, so do not mix the two words.
In Mathlib, `Orthonormal 𝕜 v` says that each `v i` has norm $1$ and that `v i` and `v j` are orthogonal for $i \neq j$.

## Remarks

### Testing a family in the plane

Take $e_1 = (\tfrac35, \tfrac45)$ and $e_2 = (-\tfrac45, \tfrac35)$ in $\mathbb{R}^2$ with the dot product.
Check the lengths first:
$$\norm{e_1}^2 = \tfrac{9}{25} + \tfrac{16}{25} = 1, \qquad \norm{e_2}^2 = \tfrac{16}{25} + \tfrac{9}{25} = 1.$$
Then check the one pair:
$$e_1 \cdot e_2 = -\tfrac{12}{25} + \tfrac{12}{25} = 0.$$
So the family is orthonormal.
It is the standard basis turned by the angle whose cosine is $\tfrac35$.
The same two tests work for any family: compute $\ip{e_i}{e_i}$ for each $i$ and $\ip{e_i}{e_j}$ for each pair.

### More examples

Over $\mathbb{C}$ the conjugate enters the test.
For $f_1 = \tfrac{1}{\sqrt2}(1, i)$ and $f_2 = \tfrac{1}{\sqrt2}(1, -i)$ with the standard inner product, the pair gives
$$\ip{f_1}{f_2} = \tfrac12\left(1 \cdot \overline{1} + i \cdot \overline{-i}\right) = \tfrac12 (1 + i \cdot i) = 0,$$
and each $\ip{f_j}{f_j} = \tfrac12(1 + 1) = 1$, as the [[orthonormal basis of $\mathbb{C}^2$|V2B3V8T8TX]] checks in full.

The space need not be a space of columns.
For the [[trace inner product|JVH9RZ7QAB]] $\ip{A}{B} = \tr(B^* A)$ on $M_2(\mathbb{C})$, the four [[matrix units|A4HTT7JFD1]] are orthonormal, because $\tr(E_{lm}^* E_{jk}) = \tr(E_{ml} E_{jk})$ is $1$ when $(j, k) = (l, m)$ and $0$ otherwise.
On polynomials with $\ip{p}{q} = \int_{-1}^{1} p(x) q(x) \, dx$, the pair $\tfrac{1}{\sqrt2}$ and $\sqrt{\tfrac32}\, x$ is orthonormal:
$$\int_{-1}^{1} \tfrac12 \, dx = 1, \qquad \int_{-1}^{1} \tfrac32 x^2 \, dx = 1, \qquad \int_{-1}^{1} \tfrac{\sqrt3}{2} x \, dx = 0.$$
The [[Legendre polynomials|JPDVZM20EX]] continue this family.

### What fails in a non-example

The vectors $(1, 1)$ and $(1, -1)$ are orthogonal, since $1 - 1 = 0$, but each has norm $\sqrt2$, so the [[family is not orthonormal|72YCTDMG60]].
Dividing each vector by $\sqrt2$ repairs it.
The unit vectors $(1, 0)$ and $\tfrac{1}{\sqrt2}(1, 1)$ fail the other test, since their dot product is $\tfrac{1}{\sqrt2} \neq 0$.
Orthonormality also depends on the inner product.
For $\ip{x}{y} = 2x_1 y_1 + x_2 y_2$ on $\mathbb{R}^2$, the standard basis is not orthonormal, because $\ip{e_1}{e_1} = 2$.

### What you get from orthonormality

The first gain is that an orthonormal family is [[linearly independent|0JWM6GJNQW]], so in a space of dimension $n$ it has at most $n$ members.
The second gain is the coefficient formula.
If $v = \sum_j a_j e_j$, take the inner product with $e_k$: every term with $j \neq k$ vanishes, and $\ip{v}{e_k} = a_k$.
The [[Pythagorean theorem|0BVTDM872V]] then gives $\norm{v}^2 = \sum_j \abs{a_j}^2$.
For an arbitrary $v$ that need not lie in the span, [[Bessel's inequality|0RBT5PB74K]] gives $\sum_j \abs{\ip{v}{e_j}}^2 \le \norm{v}^2$.
In $\mathbb{K}^n$, the columns of an $n \times k$ matrix $Q$ are orthonormal exactly when $Q^* Q = I_k$, by the [[criterion for orthonormal columns|83QE4F4E4V]].
An orthonormal family with $\dim V$ members is an [[orthonormal basis|0S9GGTR0EX]].

### Watch out

Three slips are common.
The first is to call a family orthonormal when it is only orthogonal, as with $(1, 1)$ and $(1, -1)$ above.
The second is to test only neighboring pairs.
In $\mathbb{R}^3$, the family $(1, 0, 0)$, $(0, 1, 0)$, $(1, 0, 0)$ passes the tests for the pairs $(1, 2)$ and $(2, 3)$, but the pair $(1, 3)$ gives $1$, so you must test every pair.
The third is to forget the conjugate over $\mathbb{C}$: without it, $\tfrac{1}{\sqrt2}(1, i)$ seems to give $\tfrac12(1 + i^2) = 0$ with itself, while the correct value is $1$.

### History

The [[Gram-Schmidt process|0VT6P0GNQR]], which turns any independent family into an orthonormal one, is named after Jørgen Gram and Erhard Schmidt.
Laplace used the same method before either of them.

### Try it

First, find a unit vector along $(1, 2)$ and a unit vector orthogonal to it.
Divide by the norm $\sqrt5$ to get $\tfrac{1}{\sqrt5}(1, 2)$, and take $\tfrac{1}{\sqrt5}(-2, 1)$, whose dot product with the first is $\tfrac{-2 + 2}{5} = 0$.

Second, decide whether $\tfrac{1}{\sqrt2}(1, i)$ and $\tfrac{1}{\sqrt2}(i, 1)$ are orthonormal in $\mathbb{C}^2$.
Each has norm $1$, and $\ip{(1, i)}{(i, 1)} = 1 \cdot \overline{i} + i \cdot \overline{1} = -i + i = 0$, so the answer is yes.

Third, write $(5, 0)$ in terms of $e_1 = (\tfrac35, \tfrac45)$ and $e_2 = (-\tfrac45, \tfrac35)$.
The coefficients are $(5, 0) \cdot e_1 = 3$ and $(5, 0) \cdot e_2 = -4$, and indeed $3 e_1 - 4 e_2 = (\tfrac{9 + 16}{5}, \tfrac{12 - 12}{5}) = (5, 0)$.

## Explanations

### L1 human

Think of an orthonormal family as a set of rulers of length $1$ laid at right angles to each other.
The usual axes $(1, 0)$ and $(0, 1)$ of the plane are one set.
Turn both rulers together and you get another set, such as $(0.6, 0.8)$ and $(-0.8, 0.6)$.
To find how far a vector reaches along one ruler, you take one inner product with that ruler.
For the vector $(5, 0)$ and the first turned ruler, this gives $5 \cdot 0.6 = 3$.

### L2 human

Here is a typical test in $\mathbb{R}^3$: are $e_1 = \tfrac13(1, 2, 2)$, $e_2 = \tfrac13(2, 1, -2)$ and $e_3 = \tfrac13(2, -2, 1)$ orthonormal?
Each vector has squared entries that add to $9$, so after the factor $\tfrac19$ each norm is $1$.
The three pairs give
$$e_1 \cdot e_2 = \tfrac{2 + 2 - 4}{9} = 0, \qquad e_1 \cdot e_3 = \tfrac{2 - 4 + 2}{9} = 0, \qquad e_2 \cdot e_3 = \tfrac{4 - 2 - 2}{9} = 0.$$
So the family is orthonormal, and the matrix with columns $e_1, e_2, e_3$ satisfies $Q^{\mathsf{T}} Q = I_3$.
Now take $v = (3, 3, 0)$.
Its coefficients are $v \cdot e_1 = 3$, $v \cdot e_2 = 3$ and $v \cdot e_3 = 0$, so $v = 3e_1 + 3e_2$.
Check: $(1, 2, 2) + (2, 1, -2) = (3, 3, 0)$, and $3^2 + 3^2 = 18 = \norm{v}^2$.
The coefficients came from three dot products, with no linear system to solve, and that is the reason to prefer orthonormal families.

### L3 human

An orthonormal family $(e_1, \dots, e_k)$ is the same as a linear map $\mathbb{K}^k \to V$, $a \mapsto \sum_j a_j e_j$, that preserves inner products.
In matrix language this is the condition $Q^* Q = I_k$, and for square $Q$ it gives the [[orthogonal matrices|0W02QESPJQ]] and the [[unitary matrices|0AR68JTMDT]].
The concept specializes [[orthogonality for a bilinear form|01TXN7ETH2]] to a positive definite form, with the extra condition of unit length.
In a [[Hilbert space|HM2HHE3J51]], infinite orthonormal families such as $t \mapsto e^{2\pi i k t}$ on $[0, 1]$ lead to [[Fourier series|G12KXDHPPS]], where the finite sums become convergent series.
