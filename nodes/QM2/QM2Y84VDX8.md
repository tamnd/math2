---
tag: QM2Y84VDX8
kind: statement
role: theorem
name: Minimum-norm solution of an underdetermined system
msc: [15A06, 15A09]
topics: [8GQVME4SZZ]
audience: ug1
about: [QJ0P26J9BV]
uses: [0EX045E2BP, 0EP73HK4C4, 0PQ2GGY1QV, 0EWQEYRVA8, 0EB9N0S33C, 0PSRCMCM5X, 0Q8HZTJC7G]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
    locator: Minimum norm solution to a linear system
  - book: isbn:9781733146678
    locator: Chapter 4
---

## Statement

A consistent system with more unknowns than conditions has many solutions, and exactly one of them is shortest: the one that lies in the row space.

Let $\mathbb{K} = \R$ or $\C$ with the standard inner product, and let $A$ be an $m \times n$ matrix over $\mathbb{K}$ with [[conjugate transpose|0EX045E2BP]] $A^*$.
Let $b \in \mathbb{K}^m$, and assume that the system $Ax = b$ has at least one solution.
Then the following hold.

1. Among all solutions of $Ax = b$ there is exactly one solution $x_0$ of smallest norm.
2. The vector $x_0$ is the only solution in $\operatorname{Col}(A^*)$, which over $\R$ is the [[row space|0EP73HK4C4]] of $A$.
3. Every solution has the form $x = x_0 + z$ with $z$ in the [[null space|0PQ2GGY1QV]] $\operatorname{Nul}(A)$, and then $\norm{x}^2 = \norm{x_0}^2 + \norm{z}^2$.
4. For every solution $x$, the vector $x_0$ is the [[orthogonal projection|0Q8HZTJC7G]] of $x$ onto $\operatorname{Col}(A^*)$.
5. Assume in addition that $A$ has full row rank, that is, its [[rank|0EWQEYRVA8]] is $m$. Then $A A^*$ is [[invertible|0EB9N0S33C]], the system $Ax = b$ has a solution for every $b \in \mathbb{K}^m$, and
$$x_0 = A^* (A A^*)^{-1} b.$$
6. Under the hypothesis of part 5, the matrix $A^* (A A^*)^{-1}$ is the [[Moore-Penrose inverse|0PSRCMCM5X]] $A^+$ of $A$, so $x_0 = A^+ b$.

The [[proof|CA0AYVS1XD]] combines the orthogonality of $\operatorname{Nul}(A)$ and $\operatorname{Col}(A^*)$ with the Pythagorean theorem.

## Remarks

### A first case: one equation

Take the single equation $x_1 + 2x_2 + 2x_3 = 9$ in $\R^3$.
Its solutions form a plane, and the shortest solution is the point of the plane closest to the origin.
Here $A = (1 \ 2 \ 2)$ has rank $1$, so part 5 applies with $A A^{\mathsf{T}} = 1 + 4 + 4 = 9$:
$$x_0 = A^{\mathsf{T}} \cdot \tfrac{1}{9} \cdot 9 = (1, 2, 2).$$
Check: $1 + 4 + 4 = 9$, and $\norm{x_0} = 3$.
The solution $(9, 0, 0)$ that you might guess first has norm $9$.
In general, for one equation $a^{\mathsf{T}} x = \beta$ with $a \ne 0$, the formula gives $x_0 = \frac{\beta}{a^{\mathsf{T}} a} a$ and $\norm{x_0} = \abs{\beta} / \norm{a}$, the distance from the origin to a hyperplane.
The [[example with two equations|SAXMQJ4PKE]] works a case where $A A^{\mathsf{T}}$ is a $2 \times 2$ matrix.

### Why the row space

Why should the shortest solution lie in the row space?
Every solution is $x_0 + z$ with $z$ in the null space, and the null space is orthogonal to the row space.
So adding $z$ adds a perpendicular piece, and by the Pythagorean theorem a perpendicular piece can only add length.
The shortest solution is the one with no null space piece at all.
Geometrically, the solution set is a flat $x_0 + \operatorname{Nul}(A)$, and $x_0$ is its point closest to $0$.

### Why each hypothesis is needed

The system must have a solution.
If $Ax = b$ has none, parts 1 to 4 say nothing, and the natural replacement is the least-squares solution of least norm, which is $A^+ b$.

Full row rank is needed for the formula in part 5, but not for parts 1 to 4.
For $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ the rows are dependent, and $A A^{\mathsf{T}} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$ is singular, so the formula has no meaning.
For $b = (2, 2)$ the solutions are still the points with $x_1 + x_2 = 2$, and the only one in the row space $\R(1, 1)$ is $x_0 = (1, 1)$.

The norm must come from the inner product.
For the norm $\norm{x}_1 = \abs{x_1} + \abs{x_2}$ and the equation $x_1 + x_2 = 1$, every solution with $x_1, x_2 \ge 0$ has $\norm{x}_1 = 1$, so the smallest norm is reached at infinitely many points.

### Watch out

Two formulas look alike and belong to opposite cases.
The matrix $A^{\mathsf{T}} (A A^{\mathsf{T}})^{-1}$ needs independent rows, and it picks the shortest exact solution of a system with too few equations.
The matrix $(A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$ needs independent columns, and it gives the [[least-squares|0BYTQ4X1HC]] solution of a system with too many equations.
For a $2 \times 3$ matrix of rank $2$, the $3 \times 3$ matrix $A^{\mathsf{T}} A$ has rank at most $2$, so only the first formula can work.

### Generalizations

For every $A$ and $b$, the vector $A^+ b$ is the least-squares solution of least norm; see the [[Moore-Penrose inverse|0YY8VX28JR]] and the [[least-squares solution from a reduced singular value decomposition|SBP2PCHH9M]].
The present theorem is the case where the least-squares solutions are exact solutions.

## Explanations

### L1 human

A system with more unknowns than equations usually has infinitely many solutions.
For example, $x + y = 2$ is solved by $(2, 0)$, by $(0, 2)$, by $(1, 1)$ and by many more points.
These solutions form a line, and one point of the line is closest to the origin.
Here that point is $(1, 1)$, with length $\sqrt 2$, while $(2, 0)$ has length $2$.
The theorem says that such a shortest solution always exists, and it says how to find it.

### L2 human

Take $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ and $b = (2, 2)$.
The rows are independent, so we solve $A A^{\mathsf{T}} y = b$ and put $x_0 = A^{\mathsf{T}} y$.
The [[worked example|SAXMQJ4PKE]] does this and finds
$$x_0 = \left( \tfrac{2}{3}, \tfrac{4}{3}, \tfrac{2}{3} \right), \qquad \norm{x_0}^2 = \tfrac{8}{3}.$$
Other solutions, such as $(2, 0, 2)$ with squared norm $8$ and $(0, 2, 0)$ with squared norm $4$, are longer.
So among the many solutions of a system with free variables, the theorem picks one natural solution that does not depend on which variable we call free.
Watch out: when the rows are dependent, $A A^{\mathsf{T}}$ is singular, and you must use the pseudoinverse or remove the redundant rows first.

### L3 human

The map $b \mapsto x_0$ is linear on $\operatorname{Col}(A)$, and it is the inverse of the bijection $A|_{\operatorname{Col}(A^*)} \colon \operatorname{Col}(A^*) \to \operatorname{Col}(A)$.
This is how the four fundamental subspaces describe $A^+$: it inverts $A$ from the column space back to the row space, and it is zero on $\operatorname{Nul}(A^*)$.
The theorem is dual to [[least squares|0BYTQ4X1HC]]: there we project $b$ onto a column space, and here we project a solution onto a row space.
The sub-area on positive operators and singular values builds $A^+$ for every matrix from the singular value decomposition.
