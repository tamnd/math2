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

Each free variable of the reduced form gives one vector of a basis of the null space, so the null space has dimension $n - \operatorname{rank} A$.
Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
Let $R$ be the [[reduced row echelon form|0NNR68BFRY]] of $A$, with [[pivot columns|0BCMGDHZGR]] $p_1 < \dots < p_r$ and free columns $f_1 < \dots < f_k$, so that $k = n - r$.
For $l = 1, \dots, k$, let $s_l \in F^n$ be the vector with entry $1$ in position $f_l$, entry $0$ in the other free positions, and entry $-R_{i f_l}$ in the pivot position $p_i$ for $i = 1, \dots, r$.
Then the following hold.

1. The [[null space|0PHDYNR24D]] $\operatorname{Null}(A)$ is a [[subspace|00YC1D652K]] of $F^n$.
2. The vectors $s_1, \dots, s_k$ form a basis of $\operatorname{Null}(A)$.
3. The [[dimension|03GSZ8RTZJ]] is $\dim \operatorname{Null}(A) = n - \operatorname{rank} A$, where $\operatorname{rank} A$ is the [[rank|0ZC9YTXZRY]] of $A$.

## Remarks

### Why each hypothesis is needed

The entries of $s_l$ must be read from the reduced form, because only there does each pivot row involve one pivot variable.
In the echelon form $\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix}$, copying the negatives of column 3 gives $(-1, -1, 1)$, but its product with the first row is $-1 - 1 + 1 = -1 \ne 0$.
The reduced form $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ gives the correct vector $(0, -1, 1)$.

The entries must lie in a field, because the reduction divides by the pivots.
Over the ring $\mathbb{Z}/4$, the $1 \times 1$ matrix $(2)$ cannot be scaled to a pivot $1$.
Its null space $\{0, 2\}$ has $2$ elements, while a free module over $\mathbb{Z}/4$ has $4^k$ elements, so the null space has no basis at all.

### What it gives you

The number of free variables is $n - \operatorname{rank} A$, so it does not depend on the order of the row operations.
Adding the rank gives $\operatorname{rank} A + \dim \operatorname{Null}(A) = n$, the [[rank-nullity theorem for matrices|TR48YQGCCA]].
If $n > m$, then $Ax = 0$ has a nonzero solution, because $\operatorname{rank} A \le m < n$ leaves at least one free variable.
Applied to $A^{\mathsf{T}}$, the theorem gives a basis of the left null space, of dimension $m - \operatorname{rank} A$.

For a worked use, see the [[3 by 4 example|GG03BSSZ43]]: the free columns 2 and 4 give $s_1 = (-2, 1, 0, 0)$ and $s_2 = (-1, 0, -2, 1)$, and the nullity is $2 = 4 - 2$.

### The converse

Every basis of $\operatorname{Null}(A)$ has $n - \operatorname{rank} A$ vectors, but most bases are not of the form $s_1, \dots, s_k$.
For example, $s_1 + s_2, s_2$ is another basis.
The vectors $s_l$ are singled out as the only basis whose entries at the free positions are the unit vectors: $s_l$ has $1$ at $f_l$ and $0$ at the other free positions.

### Generalizations

For a linear map $T$ with matrix $A$ in some bases, the coordinate map of the domain carries $\ker T$ onto $\operatorname{Null}(A)$.
So the same vectors, read as coordinates, give a basis of $\ker T$.

## Explanations

### L1 human

Solve $Ax = 0$ by row reduction, and write the pivot variables in terms of the free variables.
Set one free variable to $1$ and the others to $0$.
Each such choice gives one basis vector of the null space.
For $x_1 + 2x_2 = 0$, the only free variable is $x_2$, and the basis vector is $(-2, 1)$.

### L2 human

The free variables can take any values, and they determine the pivot variables.
So the solutions correspond one to one, and linearly, to the lists $t \in F^k$ of values of the free variables.
The basis vectors $s_l$ are the solutions for the unit lists $e_1, \dots, e_k$.
Their independence is visible at the free positions, where $s_l$ has a $1$ and the others have $0$.
The [[proof|K0ETX150T8]] makes this exact.
Watch out: the count $n - r$ uses the number $n$ of columns, not the number $m$ of equations.
