---
tag: 0WXBGBTA3D
kind: statement
role: theorem
name: The Gram-Schmidt process gives an orthonormal family with the same spans
msc: ["15A63", "65F25"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0VT6P0GNQR, 0RW9TNNT87]
uses: [A1Y41YZFB6, 0TS7VZJBWD, 09VYHEF2VT, 0HR573CHNM, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Statement

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $v_1, \dots, v_k \in V$ be [[linearly independent|0EVHJFTG9Z]].
Let $u_1, \dots, u_k$ and $e_1, \dots, e_k$ be the vectors of the [[Gram-Schmidt process|A1Y41YZFB6]].
Then, for each $j$ with $1 \leq j \leq k$:

1. the vector $u_j$ is defined and nonzero, and $u_1, \dots, u_j$ are pairwise [[orthogonal|0TS7VZJBWD]];
2. $\operatorname{span}(e_1, \dots, e_j) = \operatorname{span}(u_1, \dots, u_j) = \operatorname{span}(v_1, \dots, v_j)$, where span is the [[linear span|0HR573CHNM]];
3. the family $(e_1, \dots, e_k)$ is [[orthonormal|09VYHEF2VT]];
4. $\ip{v_j}{e_j} = \norm{u_j}$, a positive real number;
5. if $v_1, \dots, v_m$ are orthonormal for some $m \leq k$, then $e_j = u_j = v_j$ for all $j \leq m$.

## Remarks

### Why each hypothesis is needed

- Independence is needed. For the [[dependent family|6SWBRH6W8X]] $(1, 2)$, $(2, 4)$ in $\mathbb{R}^2$, the process gives $u_2 = 0$, so $e_2$ is not defined.
- Positive definiteness is needed. For the form $\beta(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ and $v_1 = (1, 1)$, $\beta(u_1, u_1) = 0$, so the coefficient $\beta(v_2, u_1)/\beta(u_1, u_1)$ is not defined.
- Part 5 needs orthonormality of the first $m$ vectors. For the orthogonal vectors $(2, 0)$, $(0, 3)$, the process gives $e_1 = (1, 0) \neq v_1$.

### Consequences

- Each finite-dimensional inner product space [[has an orthonormal basis|0Y85GYEGSF]]: apply the process to a basis.
- By part 5, each orthonormal family extends to an orthonormal basis: extend it to a basis, then apply the process.
- Parts 2 and 4 give the [[QR decomposition|0ERWG4NXQ9]]: $v_j = \sum_{i \leq j} \ip{v_j}{e_i} e_i$, with positive diagonal coefficients $\ip{v_j}{e_j}$.

### Converse

The orthonormal family in the theorem is unique in the following sense.
Let $(f_1, \dots, f_k)$ be orthonormal with $\operatorname{span}(f_1, \dots, f_j) = \operatorname{span}(v_1, \dots, v_j)$ and $\ip{v_j}{f_j} > 0$ for each $j$.
Then $f_j$ lies in $\operatorname{span}(e_1, \dots, e_j)$ and is orthogonal to $e_1, \dots, e_{j-1}$, so $f_j = c e_j$ with $|c| = 1$.
The condition $\ip{v_j}{f_j} = \overline{c}\,\norm{u_j} > 0$ forces $c = 1$, so $f_j = e_j$.
Without the sign condition, each $e_j$ can be replaced by $c_j e_j$ with $|c_j| = 1$.

### Generalizations

- For a dependent family, the process with the rule "skip $u_j$ when it is $0$" gives an orthonormal basis of the span. Mathlib's version keeps $u_j = 0$ at these places.
- For a countable independent family in any inner product space, the same recursion gives an orthonormal sequence with the same initial spans.

## Explanations

### L1 human

The Gram-Schmidt process really does produce perpendicular unit vectors.
At each stage, the first $j$ new vectors span the same space as the first $j$ old vectors.
So nothing is lost: the process only straightens the vectors.
If the first vectors are already perpendicular unit vectors, the process keeps them.

### L2 human

Worked example: we check part 4 on $v_1 = (1, 1)$, $v_2 = (1, 0)$ in $\mathbb{R}^2$.

1. $u_1 = (1, 1)$, so $e_1 = \frac{1}{\sqrt2}(1, 1)$ and $\ip{v_1}{e_1} = \sqrt2 = \norm{u_1}$.
2. $u_2 = (1, 0) - \frac12(1, 1) = (\frac12, -\frac12)$, with $\norm{u_2} = \frac{1}{\sqrt2}$.
3. $e_2 = (\frac{1}{\sqrt2}, -\frac{1}{\sqrt2})$ and $\ip{v_2}{e_2} = \frac{1}{\sqrt2} = \norm{u_2}$.
4. So $v_1 = \sqrt2\, e_1$ and $v_2 = \frac{1}{\sqrt2} e_1 + \frac{1}{\sqrt2} e_2$, a triangular system.

The typical use is the existence of orthonormal bases and the QR decomposition.
A trap: the span property holds for the initial segments $v_1, \dots, v_j$ only, not for other subsets of the $v_i$.

### L3 human

The theorem says that the flag $\operatorname{span}(v_1) \subset \operatorname{span}(v_1, v_2) \subset \cdots$ has an orthonormal basis adapted to it.
In matrix form, every invertible matrix is $QR$ with $Q$ unitary and $R$ upper triangular with positive diagonal, and the factors are unique.
In the language of Lie groups this is the Iwasawa decomposition of $GL_n$.
