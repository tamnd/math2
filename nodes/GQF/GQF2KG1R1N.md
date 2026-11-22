---
tag: GQF2KG1R1N
kind: statement
role: theorem
name: Orthogonality of the fundamental subspaces
msc: [15A03, 15A63]
topics: [8GQVME4SZZ]
audience: ug1
about: [0XJXTBCB2T]
uses: [079D68S3AW, 0F0RPPJ2TT, 0PQ2GGY1QV, 0EP73HK4C4, 0W809K6AW0, 0EX045E2BP, 0VGSYBWHV2]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Finite dimensions
  - book: isbn:9781733146678
    locator: Chapter 4
  - book: isbn:9780321982384
    locator: Section 6.1
---

## Statement

The four subspaces of a matrix pair up into two orthogonal complements: the null space is the complement of the row space, and the left null space is the complement of the column space.
Let $\mathbb{K} = \R$ or $\C$, and give $\mathbb{K}^n$ the standard [[inner product|0VGSYBWHV2]] $\ip{x}{y} = \sum_{j} x_j \overline{y_j}$, which over $\R$ is the dot product.
Let $A$ be an $m \times n$ matrix over $\mathbb{K}$, and let $A^*$ be its [[conjugate transpose|0EX045E2BP]].
Write $\operatorname{Col}$, $\operatorname{Nul}$ and $\operatorname{Row}$ for the [[column space|0F0RPPJ2TT]], the [[null space|0PQ2GGY1QV]] and the [[row space|0EP73HK4C4]], and $\perp$ for the [[orthogonal complement|079D68S3AW]].
Then:

1. $\operatorname{Nul}(A^*) = \operatorname{Col}(A)^\perp$ and $\operatorname{Col}(A) = \operatorname{Nul}(A^*)^\perp$ in $\mathbb{K}^m$.
2. $\operatorname{Nul}(A) = \operatorname{Col}(A^*)^\perp$ and $\operatorname{Col}(A^*) = \operatorname{Nul}(A)^\perp$ in $\mathbb{K}^n$.
3. Over $\R$, $A^* = A^{\mathsf{T}}$ is the [[transpose|0W809K6AW0]] and $\operatorname{Col}(A^{\mathsf{T}}) = \operatorname{Row}(A)$. So $\operatorname{Row}(A) = \operatorname{Nul}(A)^\perp$, $\operatorname{Nul}(A) = \operatorname{Row}(A)^\perp$ and $\operatorname{Col}(A) = \operatorname{Nul}(A^{\mathsf{T}})^\perp$.
4. The system $Ax = b$ has a solution if and only if $b$ is orthogonal to every $y$ with $A^* y = 0$.
5. If $Ax = b$ has a solution, then it has exactly one solution $x_r$ in $\operatorname{Col}(A^*)$, and the set of all solutions is $x_r + \operatorname{Nul}(A)$.

The [[proof|90YS11K6XD]] rests on the identity $\ip{Ax}{y} = \ip{x}{A^* y}$.

## Remarks

### The picture of Ax = b

Here is a small real case that shows all five parts.
Take
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}, \qquad A^{\mathsf{T}} = A.$$
The rows are multiples of $(1, 2)$, so $\operatorname{Row}(A) = \R(1, 2)$, and $Ax = 0$ means $x_1 + 2x_2 = 0$, so $\operatorname{Nul}(A) = \R(2, -1)$.
The two lines are orthogonal, since $(1, 2) \cdot (2, -1) = 0$, and together they fill the input plane.
Because $A$ is symmetric, the column space is also $\R(1, 2)$ and the left null space is also $\R(2, -1)$.

Part 4 now decides solvability with one dot product.
For $b = (1, 2)$ we get $b \cdot (2, -1) = 0$, so $Ax = b$ has a solution, for example $x = (1, 0)$.
For $b = (1, 0)$ we get $b \cdot (2, -1) = 2 \ne 0$, so $Ax = b$ has no solution.

For $b = (1, 2)$, part 5 picks the solution in the row space.
Write $x_r = t(1, 2)$; then $A x_r = (5t, 10t)$, and $5t = 1$ gives $x_r = (\tfrac{1}{5}, \tfrac{2}{5})$.
All solutions are $x_r + s(2, -1)$, and $x = (1, 0)$ is the one with $s = \tfrac{2}{5}$.
So $A$ sends the row space onto the column space, and it sends the null space to zero.

### Why each hypothesis is needed

The conjugate in $A^*$ is needed over $\C$.
For $A = \begin{pmatrix} 1 & i \end{pmatrix}$, the equation $x_1 + i x_2 = 0$ gives $\operatorname{Nul}(A) = \C(-i, 1)$, and the row space is $\C(1, i)$.
But $\ip{(-i, 1)}{(1, i)} = -i \cdot 1 + 1 \cdot \overline{i} = -2i \ne 0$, so $\operatorname{Nul}(A)$ is not orthogonal to the rows.
With the conjugated row, $\operatorname{Col}(A^*) = \C(1, -i)$, we get $\ip{(-i, 1)}{(1, -i)} = -i + i = 0$, as part 2 says.

The inner product must be the standard one.
For another inner product on $\mathbb{K}^n$, the matrix $A^*$ must be replaced by the matrix of the [[adjoint|0R9NMSM1ZP]] for that inner product.

### What it gives you

With the [[orthogonal decomposition|0SP7P0G7KQ]], part 3 gives $\dim \operatorname{Row}(A) + \dim \operatorname{Nul}(A) = n$, which is rank-nullity once more.
Part 1 for real matrices is the separate result on [[the complement of the column space|J4SZVFBHS5]], and the [[four fundamental subspaces|73DVECPAT6]] collect the dimensions.
Part 4 is a form of the [[Fredholm alternative|4HH8C9V8JQ]]: either $Ax = b$ has a solution, or some $y$ has $A^* y = 0$ and $\ip{b}{y} \ne 0$, but not both.
The solution $x_r$ of part 5 is the [[minimum-norm solution|QM2Y84VDX8]] of $Ax = b$, and part 1 is the reason that the [[least-squares|0BYTQ4X1HC]] residual satisfies $A^{\mathsf{T}}(b - Ax) = 0$.

### The converse and generalizations

Parts 1 to 4 are equalities and equivalences, so they need no separate converse.
In part 5 the converse also holds: every vector of $x_r + \operatorname{Nul}(A)$ solves $Ax = b$.

For a linear map $T$ between finite-dimensional inner product spaces, the same statements read $\ker T^* = (\im T)^\perp$ and $\im T^* = (\ker T)^\perp$, and the sub-area on [[adjoints|0R9NMSM1ZP]] proves them in that form.
For a bounded operator between Hilbert spaces, $\ker T^* = (\im T)^\perp$ still holds, but the second formula needs the closure of the image.

## Explanations

### L1 human

A matrix takes input vectors to output vectors.
Some input directions are sent to zero, and they form the null space.
The rows of the matrix point in the directions that the matrix can see, and every null direction is at a right angle to every row.
On the output side, the reachable outputs and the directions that no output reaches are at a right angle in the same way.

### L2 human

The typical use is to test solvability without solving.
Take $A$ with rows $(1, 0, 1)$, $(0, 1, 1)$ and $(1, 1, 2)$, and ask for which $b$ the system $Ax = b$ is solvable.
The third row is the sum of the first two, so $A^{\mathsf{T}} y = 0$ has the solution $y = (1, 1, -1)$, and the left null space is $\R(1, 1, -1)$ since the rank is $2$.
By part 4, $Ax = b$ is solvable exactly when $b_1 + b_2 - b_3 = 0$.
For $b = (1, 2, 3)$ this holds, and $x = (1, 2, 0)$ is a solution, while for $b = (1, 0, 0)$ it fails.
Watch out: over $\C$ the test uses $A^*$, not $A^{\mathsf{T}}$, because the null space is orthogonal to the conjugated rows.

### L3 human

The four subspaces and their orthogonality give a complete picture of a matrix as a map, as in Strang's textbook.
The [[singular value decomposition|000NPTMX6J]] refines it: the first $r$ right singular vectors span $\operatorname{Row}(A)$ and the rest span $\operatorname{Nul}(A)$, and the left singular vectors split $\operatorname{Col}(A)$ from $\operatorname{Nul}(A^*)$ in the same way.
In the language of homological algebra, part 1 identifies the cokernel $\mathbb{K}^m / \operatorname{Col}(A)$ with the kernel of $A^*$.
