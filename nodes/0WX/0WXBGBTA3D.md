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

The Gram-Schmidt process never breaks down on an independent list, and its output is orthonormal and spans the same subspaces as the input, step by step.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot, and let $v_1, \dots, v_k \in V$ be [[linearly independent|0EVHJFTG9Z]].
Let $u_1, \dots, u_k$ and $e_1, \dots, e_k$ be the vectors of the [[Gram-Schmidt process|A1Y41YZFB6]].
Then, for each $j$ with $1 \leq j \leq k$:

1. the vector $u_j$ is defined and nonzero, and $u_1, \dots, u_j$ are pairwise [[orthogonal|0TS7VZJBWD]];
2. $\operatorname{span}(e_1, \dots, e_j) = \operatorname{span}(u_1, \dots, u_j) = \operatorname{span}(v_1, \dots, v_j)$, where span is the [[linear span|0HR573CHNM]];
3. the family $(e_1, \dots, e_k)$ is [[orthonormal|09VYHEF2VT]];
4. $\ip{v_j}{e_j} = \norm{u_j}$, a positive real number;
5. if $v_1, \dots, v_m$ are orthonormal for some $m \leq k$, then $e_j = u_j = v_j$ for all $j \leq m$.

The [[proof|EG3D04CHCW]] is an induction on $j$.

## Remarks

### Why each hypothesis is needed

Independence is what keeps every $u_j$ nonzero.
For the [[dependent family|6SWBRH6W8X]] $(1, 2), (2, 4)$ in $\mathbb{R}^2$, the process gives $u_2 = 0$, so $e_2$ is not defined.

Positive definiteness of the inner product is needed as well.
For the form $\beta(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ and $v_1 = (1, 1)$, we get $\beta(u_1, u_1) = 1 - 1 = 0$, so the coefficient $\beta(v_2, u_1)/\beta(u_1, u_1)$ has a zero denominator, although $v_1$ is not zero.

Part 5 needs the first $m$ vectors to be orthonormal, not just orthogonal.
For the orthogonal vectors $(2, 0)$ and $(0, 3)$, the process keeps $u_1 = (2, 0)$ and $u_2 = (0, 3)$, but it rescales them to $e_1 = (1, 0) \neq v_1$ and $e_2 = (0, 1) \neq v_2$.

### What it gives you

Apply the process to a basis of a finite-dimensional space, and part 3 gives an orthonormal basis, so every such space [[has an orthonormal basis|0Y85GYEGSF]].
Part 5 does more: extend an orthonormal family to a basis, run the process, and the family stays at the front, so every orthonormal family extends to an orthonormal basis.

Parts 2 and 4 give the [[QR decomposition|0ERWG4NXQ9]].
Since $v_j$ lies in $\operatorname{span}(e_1, \dots, e_j)$, its expansion in the orthonormal family is $v_j = \sum_{i \leq j} \ip{v_j}{e_i} e_i$.
So the matrix of the $v_j$ is the matrix of the $e_j$ times an upper triangular matrix with the positive diagonal entries $\ip{v_j}{e_j} = \norm{u_j}$.
For $v_1 = (1, 1)$ and $v_2 = (1, 0)$ this reads
$$v_1 = \sqrt2\, e_1, \qquad v_2 = \tfrac{1}{\sqrt2}\, e_1 + \tfrac{1}{\sqrt2}\, e_2, \qquad e_1 = \tfrac{1}{\sqrt2}(1, 1), \quad e_2 = \tfrac{1}{\sqrt2}(1, -1).$$
Check: $\tfrac{1}{\sqrt2} e_1 + \tfrac{1}{\sqrt2} e_2 = \tfrac12(1, 1) + \tfrac12(1, -1) = (1, 0)$.

### The converse: uniqueness

The output is the only orthonormal family with the two properties of parts 2 and 4.
Let $(f_1, \dots, f_k)$ be orthonormal with $\operatorname{span}(f_1, \dots, f_j) = \operatorname{span}(v_1, \dots, v_j)$ and $\ip{v_j}{f_j} > 0$ for each $j$.
Then $f_j$ lies in $\operatorname{span}(e_1, \dots, e_j)$ and is orthogonal to $\operatorname{span}(f_1, \dots, f_{j-1}) = \operatorname{span}(e_1, \dots, e_{j-1})$, so $f_j = c e_j$ with $\abs{c} = 1$.
The condition $\ip{v_j}{f_j} = \overline{c}\,\norm{u_j} > 0$ forces $c = 1$, so $f_j = e_j$.
Without the sign condition, each $e_j$ can be replaced by $c_j e_j$ with $\abs{c_j} = 1$, which is $\pm e_j$ over $\mathbb{R}$.

### Generalizations

For a dependent list, the rule "skip $u_j$ when it is $0$" gives an orthonormal basis of the span of the list, and Mathlib's version keeps $u_j = 0$ at those places.
For a countable independent family in any inner product space, the same recursion gives an orthonormal sequence with the same initial spans.

## Explanations

### L1 human

The Gram-Schmidt process really does produce perpendicular unit vectors, and it never gets stuck as long as the input vectors are independent.
At each stage, the first $j$ new vectors reach exactly the same places as the first $j$ old vectors.
So nothing is lost: the process only straightens and rescales.
If the first vectors are already perpendicular and of length $1$, the process leaves them alone.

### L2 human

Here is a check of part 4 and part 5 on one example.
Take $v_1 = (1, 0, 0)$, $v_2 = (0, 1, 0)$ and $v_3 = (1, 1, 2)$ in $\mathbb{R}^3$.
The first two are orthonormal, so part 5 predicts $e_1 = v_1$ and $e_2 = v_2$, and indeed $v_2 \cdot u_1 = 0$ gives $u_2 = v_2$.
For the third vector,
$$u_3 = (1, 1, 2) - 1 \cdot (1, 0, 0) - 1 \cdot (0, 1, 0) = (0, 0, 2), \qquad e_3 = (0, 0, 1).$$
Part 4 says $\ip{v_3}{e_3} = \norm{u_3}$, and both sides are $2$.
The typical use is the existence of orthonormal bases that contain given orthonormal vectors, and the QR decomposition.
Watch out: the span property holds for the initial segments $v_1, \dots, v_j$ only; here $\operatorname{span}(e_3) \neq \operatorname{span}(v_3)$.

### L3 human

The theorem says that every flag $\operatorname{span}(v_1) \subset \operatorname{span}(v_1, v_2) \subset \cdots$ of subspaces has an orthonormal basis adapted to it, unique once the positivity condition of part 4 is imposed.
In matrix form, every invertible matrix is $QR$ with $Q$ unitary and $R$ upper triangular with positive diagonal, and the two factors are unique.
In the language of Lie groups this is the Iwasawa decomposition of $\mathrm{GL}_n(\mathbb{R})$ and $\mathrm{GL}_n(\mathbb{C})$.
