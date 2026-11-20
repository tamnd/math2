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

Let $V$ be an inner product space over $\mathbb{R}$ or $\mathbb{C}$, and let $v_1, \dots, v_k \in V$ be [[linearly independent|0EVHJFTG9Z]].
The Gram-Schmidt process sets $u_1 = v_1$ and $u_j = v_j - \sum_{i < j} \frac{\ip{v_j}{u_i}}{\ip{u_i}{u_i}} u_i$, and then $e_j = u_j / \norm{u_j}$.
The result $(e_1, \dots, e_k)$ is an [[orthonormal family|09VYHEF2VT]] with $\operatorname{span}(e_1, \dots, e_j) = \operatorname{span}(v_1, \dots, v_j)$ for each $j$, where span is the [[linear span|0HR573CHNM]].
The [[formal definition|A1Y41YZFB6]] states the recursion, and the [[Gram-Schmidt theorem|0WXBGBTA3D]] proves these properties.
The process matters because it turns any basis into an orthonormal basis, and so it proves that orthonormal bases exist.

## Motivation

Coordinates, lengths and projections are simple in an orthonormal basis, but the bases that we meet first are rarely orthonormal.
In $\mathbb{R}^2$, to make $v_2$ perpendicular to $v_1$, we subtract from $v_2$ its shadow on the line of $v_1$.
In higher dimension we repeat this step: from each new vector we subtract its shadows on all earlier directions.
The process does this in a fixed order, and it keeps the spans of the first $j$ vectors at each stage.

## Notation

- Books write the process with the $u_i$, as above, or with the $e_i$: $u_j = v_j - \sum_{i < j}\ip{v_j}{e_i} e_i$. Both give the same vectors.
- Some books write the name with an en dash, and some books speak of "orthogonalization" or "orthonormalization".
- Mathlib has `InnerProductSpace.gramSchmidt` for the vectors $u_j$ and `InnerProductSpace.gramSchmidtNormed` for the $e_j$.

## Remarks

### Examples

- In $\mathbb{R}^2$, $v_1 = (1, 1)$ and $v_2 = (1, 0)$ give $u_2 = (\frac12, -\frac12)$, so $e_1 = \frac{1}{\sqrt2}(1, 1)$ and $e_2 = \frac{1}{\sqrt2}(1, -1)$.
- In $\mathbb{R}^3$, the [[process on $(1, 1, 0)$, $(1, 0, 1)$, $(0, 1, 1)$|2D1189E3N9]] gives $\frac{1}{\sqrt2}(1, 1, 0)$, $\frac{1}{\sqrt6}(1, -1, 2)$ and $\frac{1}{\sqrt3}(-1, 1, 1)$.
- On polynomials with $\int_{-1}^1 pq$, the process on $1, x, x^2, x^3$ gives multiples of the [[Legendre polynomials|JPDVZM20EX]].
- If $v_1, \dots, v_k$ are already orthonormal, the process returns them unchanged, by part 4 of the [[Gram-Schmidt theorem|0WXBGBTA3D]].

### Non-examples

- The process does not apply to a [[dependent family|6SWBRH6W8X]]: for $(1, 2)$ and $(2, 4)$ it gives $u_2 = 0$, which cannot be normalized.
- Dividing each $v_j$ by its norm is not the process: $(1, 1)$ and $(1, 0)$ become $\frac{1}{\sqrt2}(1, 1)$ and $(1, 0)$, which are not orthogonal.
- Subtracting projections onto the old vectors $v_i$ instead of the new $u_i$ is not the process. For $(1, 0, 0)$, $(1, 1, 0)$, $(1, 1, 1)$ it gives a third vector $(-1, 0, 1)$, which is not orthogonal to $(1, 0, 0)$.

### Basic properties

- The $e_j$ are orthonormal, and $\operatorname{span}(e_1, \dots, e_j) = \operatorname{span}(v_1, \dots, v_j)$ for each $j$, by the [[Gram-Schmidt theorem|0WXBGBTA3D]].
- Also $\ip{v_j}{e_j} = \norm{u_j} > 0$. With the spans, this fixes the $e_j$ uniquely.
- Applied to a basis, the process gives an orthonormal basis. So every finite-dimensional inner product space [[has an orthonormal basis|0Y85GYEGSF]].
- In matrix form, the process writes $A = QR$ with orthonormal columns in $Q$ and $R$ upper triangular with positive diagonal. This is the [[QR decomposition|0ERWG4NXQ9]].
- The output depends on the order: $(1, 0)$, $(1, 1)$ give the standard basis, while $(1, 1)$, $(1, 0)$ give $\frac{1}{\sqrt2}(1, 1)$, $\frac{1}{\sqrt2}(1, -1)$.
- Classical and modified variants. The classical process computes all coefficients $\ip{v_j}{e_i}$ from the original $v_j$, and then subtracts. The modified process starts with $w = v_j$ and replaces $w$ by $w - \ip{w}{e_i} e_i$ for $i = 1, \dots, j - 1$, one direction at a time.
- In exact arithmetic the two variants give the same $u_j$. After the first $i - 1$ subtractions, $\ip{w}{e_i} = \ip{v_j}{e_i}$, because $e_i$ is orthogonal to $e_1, \dots, e_{i-1}$.
- On a computer, rounding errors make the computed $e_i$ only nearly orthogonal. The modified variant computes each coefficient from the current vector, so it also removes errors of the earlier subtractions.
- According to the Wikipedia article, the classical variant is numerically unstable, and the modified variant introduces smaller errors.

### History

The process is named after Gram and Schmidt.
According to the Wikipedia article, Laplace was familiar with the method before Gram and Schmidt.

### Common errors

- Students subtract projections onto the old vectors $v_i$. The projections must be onto the new vectors $u_i$, which are orthogonal.
- Students forget to normalize, or they normalize $u_j$ but still use the formula $\ip{v_j}{u_i} u_i$ without the division by $\ip{u_i}{u_i}$.
- Over $\mathbb{C}$, students compute the coefficient as $\ip{u_i}{v_j}$ with our convention. This gives the conjugate, and the result is not orthogonal.

## Explanations

### L1 human

The Gram-Schmidt process straightens a set of vectors into a set of perpendicular unit vectors.
Take the first vector and scale it to length $1$.
From the second vector remove its part along the first direction, and scale the rest.
From the third vector remove its parts along the first two directions, and so on.

### L2 human

Worked example: $v_1 = (1, 0, 1)$ and $v_2 = (0, 1, 1)$ in $\mathbb{R}^3$.

1. $u_1 = (1, 0, 1)$, and $u_1 \cdot u_1 = 2$.
2. $v_2 \cdot u_1 = 1$, so $u_2 = (0, 1, 1) - \frac12(1, 0, 1) = (-\frac12, 1, \frac12)$.
3. Check: $u_2 \cdot u_1 = -\frac12 + \frac12 = 0$. Also $u_2 \cdot u_2 = \frac14 + 1 + \frac14 = \frac32$.
4. So $e_1 = \frac{1}{\sqrt2}(1, 0, 1)$ and $e_2 = \frac{1}{\sqrt6}(-1, 2, 1)$.
5. The plane spanned by $e_1$ and $e_2$ is the plane spanned by $v_1$ and $v_2$.

The typical use is to build an orthonormal basis of a subspace that is given by a spanning set.
A trap: a dependent input gives $u_j = 0$ at some step, and the division by $\norm{u_j}$ fails.

### L3 human

Each step of the process applies the [[orthogonal projection|0B8KZRT28M]] onto the orthogonal complement of the span of the earlier vectors.
In matrix language, the process is the [[QR decomposition|0ERWG4NXQ9]], and in numerical work Householder reflections often replace it.
On spaces of functions, the process applied to $1, x, x^2, \dots$ gives the classical orthogonal polynomials, such as the Legendre polynomials.
The same recursion works for a countable independent family in an infinite-dimensional inner product space.
