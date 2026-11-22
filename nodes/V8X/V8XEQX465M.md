---
tag: V8XEQX465M
kind: example
name: The Fredholm alternative for a singular 2 x 2 matrix
msc: ["15A06"]
topics: [S6559D61BP]
audience: ug1
illustrates: [4HH8C9V8JQ]
uses: [4HH8C9V8JQ, 0PQ2GGY1QV, 0W809K6AW0, 0EWQEYRVA8]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_alternative
    locator: Linear algebra
---

## Example

For a singular $2 \times 2$ matrix, the transposed system gives the correct test for solvability, and the null space of $A$ itself gives a wrong one.
Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix}, \qquad A^\top = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix}$$
over $\mathbb{R}$, with the [[transpose|0W809K6AW0]] $A^\top$.

1. Row 2 of $A$ is $3$ times row 1, so the [[rank|0EWQEYRVA8]] of $A$ is $1$.
   The matrix is square and singular, so case (b) of part 3 of the [[Fredholm alternative|4HH8C9V8JQ]] holds.
2. Case (b) directly: $A(-2, 1) = (-2 + 2,\ -6 + 6) = (0, 0)$, so $x = (-2, 1)$ is a nonzero solution of $Ax = 0$.
3. The [[null space|0PQ2GGY1QV]] of $A^\top$.
   The equation $A^\top y = (y_1 + 3y_2,\ 2y_1 + 6y_2) = 0$ gives $y_1 = -3y_2$, so the null space is spanned by $y = (-3, 1)$.
4. Check: $A^\top(-3, 1) = (-3 + 3,\ -6 + 6) = (0, 0)$.
5. By part 1 of the theorem, $Ax = b$ is solvable if and only if $y^\top b = -3b_1 + b_2 = 0$, that is, $b_2 = 3b_1$.
6. Take $b = (1, 2)$.
   Then $-3 \cdot 1 + 2 = -1 \ne 0$, so there is no solution.
7. Direct check: the equations are $x_1 + 2x_2 = 1$ and $3x_1 + 6x_2 = 2$.
   Three times the first gives $3x_1 + 6x_2 = 3 \ne 2$, so the system has no solution.
8. Take $b = (2, 6)$.
   Then $-3 \cdot 2 + 6 = 0$, so a solution exists.
9. Direct check: $x = (2, 0)$ gives $Ax = (2 + 0,\ 6 + 0) = (2, 6)$.
10. The trap.
    The null space of $A$ is spanned by $(-2, 1)$, by step 2, and the wrong test "$(-2, 1) \cdot b = 0$" means $b_2 = 2b_1$.
11. For $b = (1, 2)$ the wrong test gives $-2 + 2 = 0$ and predicts a solution, but step 7 shows there is none.
12. For $b = (2, 6)$ the wrong test gives $-4 + 6 = 2 \ne 0$ and predicts no solution, but step 9 gives one.
13. So the test must use the null space of $A^\top$, not the null space of $A$.

## Remarks

The column space of $A$ is spanned by the first column $(1, 3)$, which satisfies $b_2 = 3b_1$, as step 5 requires.
It is orthogonal to $(-3, 1)$, since $-3 \cdot 1 + 1 \cdot 3 = 0$.
For a symmetric matrix $A^\top = A$, so the two null spaces agree, and then the wrong test happens to give the right answer.
All solutions for $b = (2, 6)$ are $x = (2, 0) + t(-2, 1)$ with $t \in \mathbb{R}$.

## Explanations

### L1 human

The matrix sends every vector onto the line $b_2 = 3b_1$.
A right side off this line, like $(1, 2)$, cannot be reached.
The test vector $(-3, 1)$ comes from the transposed system, and it is orthogonal to this line.

### L2 human

The null space of $A$ describes the non-uniqueness of solutions, and the null space of $A^\top$ describes the obstructions to existence.
Here both are lines, but they are different lines, spanned by $(-2, 1)$ and $(-3, 1)$.
Only the second one is orthogonal to the column space.
