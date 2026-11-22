---
tag: 0VT6P0GNQR
kind: concept
name: Gram-Schmidt process
msc: ["15A63", "65F25"]
topics: [1D4JTZ9VS3]
audience: ug1
uses: [09VYHEF2VT, 0EVHJFTG9Z, 0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Description
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Numerical stability
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
same_as:
  wikidata: Q475239
  wikipedia: Gram–Schmidt process
---

## Summary

The Gram-Schmidt process turns any list of independent vectors into a list of perpendicular unit vectors that spans the same spaces, one vector at a time.
From each new vector it removes the parts that point along the directions already built, and then it scales what is left to length $1$.
Let $V$ be an inner product space over $\mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot, and let $v_1, \dots, v_k \in V$ be [[linearly independent|0EVHJFTG9Z]].
The process sets $u_1 = v_1$ and, for $j = 2, \dots, k$,
$$u_j = v_j - \sum_{i=1}^{j-1} \frac{\ip{v_j}{u_i}}{\ip{u_i}{u_i}}\, u_i, \qquad e_j = \frac{u_j}{\norm{u_j}}.$$
The result $(e_1, \dots, e_k)$ is an [[orthonormal family|09VYHEF2VT]] with $\operatorname{span}(e_1, \dots, e_j) = \operatorname{span}(v_1, \dots, v_j)$ for each $j$, where span is the [[linear span|0HR573CHNM]].
The [[formal definition|A1Y41YZFB6]] states the recursion, and the [[Gram-Schmidt theorem|0WXBGBTA3D]] proves these properties.

## Motivation

Coordinates, lengths and projections are easy in an orthonormal basis, because each coordinate is one inner product.
The bases that we meet first, such as the columns of a matrix or the powers $1, x, x^2$, are rarely orthonormal.
So we need a way to straighten a given basis without losing the subspaces that it describes.

In the plane the idea is a picture.
To make $v_2$ perpendicular to $v_1$, subtract from $v_2$ its shadow on the line through $v_1$.
In higher dimension we repeat this: from each new vector we subtract its shadows on all the directions built so far.
The process proves that every finite-dimensional inner product space [[has an orthonormal basis|0Y85GYEGSF]], and in matrix form it is the [[QR decomposition|0ERWG4NXQ9]] used in least squares.
It returns in the sub-area on orthogonality and least squares, and in the spectral theorems.

## Notation

Many books write the recursion with the normalized vectors, $u_j = v_j - \sum_{i < j}\ip{v_j}{e_i} e_i$.
This gives the same $u_j$, because $\frac{\ip{v_j}{u_i}}{\ip{u_i}{u_i}} u_i = \ip{v_j}{e_i} e_i$.
The order of the slots matters over $\mathbb{C}$: with our convention the coefficient is $\ip{v_j}{e_i}$, while books that are linear in the second slot write $\ip{e_i}{v_j}$, which is the same number in their notation.
Mathlib has `InnerProductSpace.gramSchmidt` for the vectors $u_j$ and `InnerProductSpace.gramSchmidtNormed` for the $e_j$.

## Remarks

### A first computation

Take $v_1 = (1, 1)$ and $v_2 = (1, 0)$ in $\mathbb{R}^2$ with the dot product.
Keep the first vector, $u_1 = (1, 1)$, with $u_1 \cdot u_1 = 2$.
The shadow of $v_2$ on $u_1$ has coefficient $\frac{v_2 \cdot u_1}{u_1 \cdot u_1} = \frac12$, so
$$u_2 = (1, 0) - \tfrac12 (1, 1) = \left(\tfrac12, -\tfrac12\right).$$
Check: $u_1 \cdot u_2 = \tfrac12 - \tfrac12 = 0$.
Normalizing gives $e_1 = \tfrac{1}{\sqrt2}(1, 1)$ and $e_2 = \tfrac{1}{\sqrt2}(1, -1)$, and both have length $1$.

### Larger examples

In $\mathbb{R}^3$ the [[process on $(1, 1, 0)$, $(1, 0, 1)$, $(0, 1, 1)$|2D1189E3N9]] gives
$$e_1 = \tfrac{1}{\sqrt2}(1, 1, 0), \qquad e_2 = \tfrac{1}{\sqrt6}(1, -1, 2), \qquad e_3 = \tfrac{1}{\sqrt3}(-1, 1, 1).$$
Check: $(1, 1, 0) \cdot (1, -1, 2) = 0$, $(1, 1, 0) \cdot (-1, 1, 1) = 0$ and $(1, -1, 2) \cdot (-1, 1, 1) = -1 - 1 + 2 = 0$.

The process works in any inner product space, not only in $\mathbb{R}^n$.
On polynomials with $\ip{p}{q} = \int_{-1}^{1} p(t) q(t)\, dt$, it turns $1, t, t^2, t^3$ into $1$, $t$, $t^2 - \tfrac13$ and $t^3 - \tfrac35 t$, which are multiples of the [[Legendre polynomials|JPDVZM20EX]].
If $v_1, \dots, v_k$ are already orthonormal, every coefficient is $0$ and every norm is $1$, so the process returns the list unchanged.

### What the process guarantees

The [[Gram-Schmidt theorem|0WXBGBTA3D]] gives four facts.
The $e_j$ are orthonormal, and the first $j$ of them span the same subspace as $v_1, \dots, v_j$.
Each $u_j$ is nonzero, since otherwise $v_j$ would lie in the span of the earlier vectors.
The number $\ip{v_j}{e_j}$ equals $\norm{u_j}$, a positive real number, and together with the spans this fixes each $e_j$ uniquely.

Applied to a basis, the process gives an orthonormal basis.
In matrix form, if the $v_j$ are the columns of $A$, it writes $A = QR$ with orthonormal columns in $Q$ and $R$ upper triangular with positive diagonal entries $r_{jj} = \norm{u_j}$.
The output depends on the order of the input: $(1, 0), (1, 1)$ gives the standard basis, while $(1, 1), (1, 0)$ gives the basis of the first computation.

### What it is not

The process needs independence.
For the [[dependent family|6SWBRH6W8X]] $(1, 2), (2, 4)$ it gives $u_2 = (2, 4) - \tfrac{10}{5}(1, 2) = 0$, which cannot be normalized.

Normalizing each $v_j$ on its own is not the process.
The vectors $(1, 1)$ and $(1, 0)$ become $\tfrac{1}{\sqrt2}(1, 1)$ and $(1, 0)$, which have length $1$ but meet at $45$ degrees.

Subtracting shadows on the old vectors $v_i$ instead of the new $u_i$ is not the process either.
For $(1, 0, 0), (1, 1, 0), (1, 1, 1)$ that rule gives the third vector $(1, 1, 1) - (1, 0, 0) - (1, 1, 0) = (-1, 0, 1)$, which is not orthogonal to $(1, 0, 0)$.

### Classical and modified Gram-Schmidt

The classical process computes all coefficients $\ip{v_j}{e_i}$ from the original vector $v_j$ and then subtracts them at once.
The modified process starts with $w = v_j$ and, for $i = 1, \dots, j - 1$ in turn, replaces $w$ by $w - \ip{w}{e_i} e_i$, so each coefficient comes from the current, partly reduced vector.

In exact arithmetic both give the same $u_j$.
After the first $i - 1$ subtractions, $w$ differs from $v_j$ by a combination of $e_1, \dots, e_{i-1}$, and these are orthogonal to $e_i$, so $\ip{w}{e_i} = \ip{v_j}{e_i}$.
For $v_3 = (0, 1, 1)$ in the $\mathbb{R}^3$ example, the modified steps are
$$w = (0, 1, 1) - \tfrac{1}{\sqrt2} e_1 = \left(-\tfrac12, \tfrac12, 1\right), \qquad w - \tfrac{1}{\sqrt6} e_2 = \left(-\tfrac23, \tfrac23, \tfrac23\right),$$
and $\ip{v_3}{e_2} = \tfrac{1}{\sqrt6}$ as well, so the classical process gives the same vector.

On a computer the two variants differ.
With rounding, the classical variant can lose orthogonality badly when the input vectors are nearly dependent, and the modified variant loses much less.

### Watch out

Over $\mathbb{C}$ the order of the slots in the coefficient matters.
With our convention the coefficient is $\ip{v_j}{u_i} / \ip{u_i}{u_i}$, and the other order gives its conjugate.
Take $v_1 = (1, 0)$ and $v_2 = (i, 1)$ in $\mathbb{C}^2$.
The correct coefficient is $\ip{v_2}{v_1} = i$, and $u_2 = (i, 1) - i(1, 0) = (0, 1)$ is orthogonal to $v_1$.
The wrong coefficient $\ip{v_1}{v_2} = \overline{i} = -i$ gives $(i, 1) + i(1, 0) = (2i, 1)$, and $\ip{(2i, 1)}{(1, 0)} = 2i \neq 0$.
A second common slip is to use $\ip{v_j}{u_i} u_i$ without the division by $\ip{u_i}{u_i}$ when the $u_i$ are not yet normalized.

### History

The process is named after Jørgen Pedersen Gram and Erhard Schmidt.
The Wikipedia article states that Laplace knew the method before them.

### Try it

First, apply the process to $(3, 4)$ and $(1, 0)$ in $\mathbb{R}^2$.
The coefficient is $\tfrac{3}{25}$, so $u_2 = (1, 0) - \tfrac{3}{25}(3, 4) = \left(\tfrac{16}{25}, -\tfrac{12}{25}\right)$, and the output is $\tfrac15(3, 4)$ and $\tfrac15(4, -3)$.

Second, what does the process do with $(2, 0)$ and $(5, 3)$?
It gives $u_2 = (5, 3) - \tfrac{10}{4}(2, 0) = (0, 3)$, so the output is the standard basis $(1, 0), (0, 1)$.

## Explanations

### L1 human

Imagine a few sticks that point in different directions, but not at right angles.
Keep the first stick and cut it to length $1$.
Look at the second stick, remove the part that runs along the first one, and cut what is left to length $1$.
For the third stick, remove the parts along the first two, and so on.
At the end you have sticks at right angles, all of length $1$, that reach the same places as the old ones.

### L2 human

Here is a complex computation, where the order of the slots matters.
In $\mathbb{C}^2$ with $\ip{x}{y} = x_1 \overline{y_1} + x_2 \overline{y_2}$, apply the process to $v_1 = (1, i)$ and $v_2 = (0, 1)$.
First $u_1 = (1, i)$, with $\ip{u_1}{u_1} = 1 + i\overline{i} = 2$.
The coefficient needs $v_2$ in the first slot:
$$\ip{v_2}{u_1} = 0 \cdot 1 + 1 \cdot \overline{i} = -i, \qquad u_2 = (0, 1) - \frac{-i}{2}(1, i) = \left(\tfrac{i}{2}, \tfrac12\right).$$
Check: $\ip{u_2}{u_1} = \tfrac{i}{2} \cdot 1 + \tfrac12 \cdot \overline{i} = \tfrac{i}{2} - \tfrac{i}{2} = 0$.
Since $\ip{u_2}{u_2} = \tfrac14 + \tfrac14 = \tfrac12$, the output is $e_1 = \tfrac{1}{\sqrt2}(1, i)$ and $e_2 = \tfrac{1}{\sqrt2}(i, 1)$.
The typical use is the same in every space: given a spanning set of a subspace, produce an orthonormal basis of it, and then compute projections by single inner products.

### L3 human

Each step of the process applies the [[orthogonal projection|0B8KZRT28M]] onto the orthogonal complement of the span of the earlier vectors, so the output is the orthonormal basis adapted to the flag $\operatorname{span}(v_1) \subset \operatorname{span}(v_1, v_2) \subset \cdots$.
In matrix language this is the [[QR decomposition|0ERWG4NXQ9]], and in numerical work Householder reflections often replace it because they keep orthogonality even better.
On spaces of functions with a weight, the process applied to $1, x, x^2, \dots$ gives the classical families of orthogonal polynomials.
The same recursion works for a countable independent family in an infinite-dimensional inner product space, and in a Hilbert space it produces orthonormal sequences.
