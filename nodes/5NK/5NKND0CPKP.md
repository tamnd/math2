---
tag: 5NKND0CPKP
kind: statement
role: proposition
name: Basis of the null space from the free variables
msc: ["15A03", "15A06"]
topics: [S6559D61BP]
audience: ug1
about: [0PHDYNR24D, 0ZC9YTXZRY]
uses: [0PHDYNR24D, 0ZC9YTXZRY, 00YC1D652K, 03GSZ8RTZJ, 0NNR68BFRY, 0BCMGDHZGR]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L1144
    locator: src/section3-5.xml:1144
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Computation by Gaussian elimination
  - book: isbn:9780321982384
    locator: Section 4.2
---

## Statement

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
Let $R$ be the [[reduced row echelon form|0NNR68BFRY]] of $A$, with [[pivot columns|0BCMGDHZGR]] $p_1 < \dots < p_r$ and free columns $f_1 < \dots < f_k$, so $k = n - r$.
For $l = 1, \dots, k$, let $s_l \in F^n$ be the vector with

- entry $1$ in position $f_l$, and entry $0$ in the other free positions $f_{l'}$, $l' \ne l$;
- entry $-R_{i f_l}$ in the pivot position $p_i$, for $i = 1, \dots, r$.

Then:

1. The [[null space|0PHDYNR24D]] $\operatorname{Null}(A)$ is a [[subspace|00YC1D652K]] of $F^n$.
2. The vectors $s_1, \dots, s_k$ form a basis of $\operatorname{Null}(A)$.
3. $\dim \operatorname{Null}(A) = n - \rank A$, where $\rank A$ is the [[rank|0ZC9YTXZRY]] of $A$.

## Remarks

### Why each hypothesis is needed

- The vectors must be read from the reduced form, or from the solved equations. The entries of a non-reduced echelon form do not give the $s_l$ directly.
- The entries must lie in a field. Over the ring $\mathbb{Z}/4$, the $1 \times 1$ matrix $(2)$ cannot be scaled to a pivot $1$.
  Its null space $\{0, 2\}$ has $2$ elements, which is not a power of $4$, so it is not free and has no basis.

### Consequences

- The number of free variables is $n - \rank A$, so it does not depend on the order of the row operations.
- $\rank A + \dim \operatorname{Null}(A) = n$, the [[rank-nullity theorem for matrices|TR48YQGCCA]].
- If $n > m$, then $Ax = 0$ has a nonzero solution, since $\rank A \le m < n$.
- The null space of $A^\top$, the left null space, has a basis from the free variables of $A^\top$, and its dimension is $m - \rank A$.

### Converse

Every basis of $\operatorname{Null}(A)$ has $n - \rank A$ vectors, but most bases are not of the form $s_1, \dots, s_k$.
The vectors $s_l$ are the only basis with entry $\delta_{l l'}$ in each free position $f_{l'}$.

### Generalizations

For a linear map $T$ with matrix $A$ in some bases, the coordinate map identifies $\ker T$ with $\operatorname{Null}(A)$.
So the same vectors give a basis of $\ker T$ in coordinates.

## Explanations

### L1 human

Solve $Ax = 0$ by row reduction, and write the pivot variables in terms of the free variables.
Set one free variable to $1$ and the others to $0$.
Each such choice gives one basis vector of the null space.

### L2 human

The free variables can take any values, and they determine the pivot variables.
So the solutions are in one-to-one linear correspondence with $F^k$, where $k$ is the number of free variables.
The basis vectors $s_l$ are the images of the standard unit vectors of $F^k$.
Their independence is visible at the free positions, where $s_l$ has a $1$ and the others have $0$.
