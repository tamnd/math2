---
tag: SAXMQJ4PKE
kind: example
name: The minimum-norm solution of two equations in three unknowns
msc: [15A06]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [QJ0P26J9BV]
illustrates: [QM2Y84VDX8]
uses: [0W809K6AW0, 0PQ2GGY1QV, 0EP73HK4C4]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
    locator: Minimum norm solution to a linear system
  - book: isbn:9781733146678
    locator: Chapter 4
---

## Example

Consider the underdetermined system
$$x_1 + x_2 = 2, \qquad x_2 + x_3 = 2,$$
with matrix and right side
$$A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \qquad b = \begin{pmatrix} 2 \\ 2 \end{pmatrix}.$$
The two rows are not multiples of each other, so $A$ has rank $2$, and the formula $x_0 = A^{\mathsf{T}} (A A^{\mathsf{T}})^{-1} b$ of the [[minimum-norm theorem|QM2Y84VDX8]] applies.

1. Multiply $A$ by its [[transpose|0W809K6AW0]]:
$$A A^{\mathsf{T}} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \det (A A^{\mathsf{T}}) = 4 - 1 = 3, \qquad (A A^{\mathsf{T}})^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}.$$
2. Solve $A A^{\mathsf{T}} y = b$:
$$y = \frac{1}{3} \begin{pmatrix} 4 - 2 \\ -2 + 4 \end{pmatrix} = \begin{pmatrix} 2/3 \\ 2/3 \end{pmatrix}.$$
3. Combine the rows of $A$ with these weights:
$$x_0 = A^{\mathsf{T}} y = \tfrac{2}{3} (1, 1, 0) + \tfrac{2}{3} (0, 1, 1) = \left( \tfrac{2}{3}, \tfrac{4}{3}, \tfrac{2}{3} \right).$$
4. Check that $x_0$ solves the system: $\tfrac{2}{3} + \tfrac{4}{3} = 2$ and $\tfrac{4}{3} + \tfrac{2}{3} = 2$.
5. Its squared length is $\norm{x_0}^2 = \tfrac{4 + 16 + 4}{9} = \tfrac{8}{3}$.
6. The [[null space|0PQ2GGY1QV]] of $A$ comes from $x_1 = -x_2$ and $x_3 = -x_2$, so $\operatorname{Nul}(A) = \R (1, -1, 1)$.
7. The dot product $x_0 \cdot (1, -1, 1) = \tfrac{2 - 4 + 2}{3} = 0$ shows that $x_0$ is orthogonal to the null space, so it lies in the [[row space|0EP73HK4C4]].
8. Every solution is $x_0 + t (1, -1, 1)$ with $t \in \R$, and since the two pieces are orthogonal,
$$\norm{x_0 + t (1, -1, 1)}^2 = \tfrac{8}{3} + 3t^2.$$
9. For $t = \tfrac{4}{3}$ we get the solution $(2, 0, 2)$, and indeed $\norm{(2, 0, 2)}^2 = 8 = \tfrac{8}{3} + \tfrac{16}{3}$.
10. For $t = -\tfrac{2}{3}$ we get the solution $(0, 2, 0)$, and indeed $\norm{(0, 2, 0)}^2 = 4 = \tfrac{8}{3} + \tfrac{4}{3}$.

So the solutions form a line in $\R^3$, and $x_0 = (\tfrac{2}{3}, \tfrac{4}{3}, \tfrac{2}{3})$ is its point closest to the origin.

## Remarks

Row reduction with the free variable $x_3$ set to $0$ gives the solution $(0, 2, 0)$.
It is a correct solution, but it is not the shortest one, because step 10 shows a null space piece $-\tfrac{2}{3} (1, -1, 1)$ inside it.
A different choice of free variable gives a different particular solution, while $x_0$ does not depend on any such choice.

What changes when $b$ changes?
The matrix $(A A^{\mathsf{T}})^{-1}$ stays the same, so $x_0$ depends linearly on $b$.
For $b = (1, 0)$, for example, $y = \tfrac{1}{3} (2, -1)$ and $x_0 = \tfrac{1}{3} (2, 1, -1)$.
Check: $\tfrac{2}{3} + \tfrac{1}{3} = 1$ and $\tfrac{1}{3} - \tfrac{1}{3} = 0$, and $(2, 1, -1) \cdot (1, -1, 1) = 0$.

If a third equation $x_1 - x_3 = 0$ is added, the system keeps the same solutions, because the new row is the first row minus the second and the right sides agree, $2 - 2 = 0$.
The new $3 \times 3$ matrix $A A^{\mathsf{T}}$ is singular, so the formula fails, but the shortest solution is still $x_0$.

## Explanations

### L1 human

The two equations describe a line of solutions in space.
Some points on the line are far from the origin, such as $(2, 0, 2)$.
One point is closest to the origin, and that point is the minimum-norm solution.
Here it is $(\tfrac{2}{3}, \tfrac{4}{3}, \tfrac{2}{3})$, at distance $\sqrt{8/3}$, which is about $1.63$.

### L2 human

The method has two steps: solve the small system $A A^{\mathsf{T}} y = b$, then put $x_0 = A^{\mathsf{T}} y$.
The first step is a $2 \times 2$ system even though there are three unknowns, because there are only two equations.
The check has two parts as well: $x_0$ solves $Ax = b$, and $x_0$ is orthogonal to the null space.
The typical use is to choose one solution of an underdetermined system in a way that does not depend on which variable we call free.
Watch out: the solution from row reduction with the free variables set to $0$ is usually not the shortest one, as $(0, 2, 0)$ shows.
