---
tag: A1Y41YZFB6
kind: definition
name: Gram-Schmidt process
msc: ["15A63", "65F25"]
topics: [1D4JTZ9VS3]
audience: ug1
defines: 0VT6P0GNQR
uses: [01EK923SKP, 0EVHJFTG9Z, 0KG4D8AP6G, 0JW13B48YP]
sources:
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Description
  - book: isbn:9783031410253
    locator: Chapter 6
formal:
  - system: lean4
    library: mathlib
    decl: InnerProductSpace.gramSchmidt
    match: variant
---

## Definition

The Gram-Schmidt process is the recursion that builds, from an independent list of vectors, an orthogonal list and then an orthonormal list.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with the inner product linear in the first slot, and let $v_1, \dots, v_k \in V$ be [[linearly independent|0EVHJFTG9Z]].
The Gram-Schmidt process applied to $(v_1, \dots, v_k)$ produces vectors $u_1, \dots, u_k$ and $e_1, \dots, e_k$ by recursion on $j$:
$$u_1 = v_1, \qquad u_j = v_j - \sum_{i=1}^{j-1} \frac{\ip{v_j}{u_i}}{\ip{u_i}{u_i}}\, u_i \quad (2 \leq j \leq k),$$
$$e_j = \frac{u_j}{\norm{u_j}} \quad (1 \leq j \leq k),$$
where $\norm{\cdot}$ is the [[induced norm|0KG4D8AP6G]].
The family $(u_1, \dots, u_k)$ is the orthogonal output, and $(e_1, \dots, e_k)$ is the orthonormal output.

## Notation

Each term $\frac{\ip{v_j}{u_i}}{\ip{u_i}{u_i}} u_i$ is the [[vector projection|0JW13B48YP]] of $v_j$ onto the line spanned by $u_i$.
Many books write the recursion with the normalized vectors, $u_j = v_j - \sum_{i < j} \ip{v_j}{e_i} e_i$, which gives the same $u_j$ because $\frac{\ip{v_j}{u_i}}{\ip{u_i}{u_i}} u_i = \ip{v_j}{e_i} e_i$.
Books that are linear in the second slot, as in physics, write the coefficient as $\ip{u_i}{v_j} / \ip{u_i}{u_i}$, and it is the same number in their notation.
Mathlib defines `InnerProductSpace.gramSchmidt 𝕜 f` for a family `f` indexed by a well-ordered type, and `gramSchmidtNormed` for the normalized version.
Mathlib does not assume independence, and for a dependent family it returns $0$ at the places where $v_j$ lies in the span of the earlier vectors, so it is a variant of the definition above.

## Remarks

The hypothesis of independence is what makes the recursion meaningful.
The [[Gram-Schmidt theorem|0WXBGBTA3D]] shows that each $u_i$ is nonzero, so $\ip{u_i}{u_i} > 0$ and the divisions are allowed.
Without independence a zero vector can appear, as the [[dependent family|6SWBRH6W8X]] $(1, 2), (2, 4)$ shows: there $u_2 = 0$ and $e_2$ is not defined.
Positive definiteness of the inner product matters too, since for the form $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ the vector $v_1 = (1, 1)$ already gives the forbidden value $\ip{u_1}{u_1} = 0$.

A small case: for $v_1 = (1, 1)$ and $v_2 = (1, 0)$ in $\mathbb{R}^2$, the recursion gives $u_2 = (1, 0) - \tfrac12(1, 1) = (\tfrac12, -\tfrac12)$, and $u_1 \cdot u_2 = 0$.
The output depends on the order of $v_1, \dots, v_k$, so the list is ordered and not a set.
The concept page on the [[Gram-Schmidt process|0VT6P0GNQR]] gives more examples, the classical and modified variants, and the uses.

## Explanations

### L1 human

The Gram-Schmidt process takes independent vectors one at a time.
From each vector it removes the parts that point along the new vectors already built.
What is left is perpendicular to all of them, and we scale it to length $1$.

### L2 human

To run the process by hand, keep a table of the $u_i$ and of the numbers $\ip{u_i}{u_i}$.

1. Put $u_1 = v_1$ and compute $\ip{u_1}{u_1}$.
2. For $j = 2$, compute $\ip{v_2}{u_1}$, then $u_2 = v_2 - \frac{\ip{v_2}{u_1}}{\ip{u_1}{u_1}} u_1$, then $\ip{u_2}{u_2}$.
3. Continue in the same way, so that step $j$ needs the $j - 1$ inner products $\ip{v_j}{u_i}$.
4. Check that each new $u_j$ is orthogonal to the earlier ones, and normalize at the end.

Watch out: over $\mathbb{C}$ the vector $v_j$ must stand in the first slot of $\ip{v_j}{u_i}$, because the other order gives the conjugate coefficient and the result is not orthogonal.

### L3 human

The recursion says $u_j = v_j - P_{j-1} v_j$, where $P_{j-1}$ is the [[orthogonal projection|0B8KZRT28M]] onto $\operatorname{span}(v_1, \dots, v_{j-1})$.
Mathlib writes it as $v_j$ minus the sum of the projections onto the lines spanned by the earlier $u_i$, which is the same vector because those lines are orthogonal.
In matrix form the process gives the [[QR decomposition|0ERWG4NXQ9]] of the matrix with columns $v_1, \dots, v_k$.
